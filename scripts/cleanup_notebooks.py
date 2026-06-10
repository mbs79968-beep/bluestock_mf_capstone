
import os
import json
import re
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

# --- Configuration for cleanup ---
def get_notebook_intro(notebook_name):
    return f"# Mutual Fund Analytics Platform\n\n## Objective\nBriefly explain the purpose of the notebook `{notebook_name}`.\n\n## Author\nBhawani Meena\n\n## Tools Used\nList the major libraries used in this notebook.\n"

KEY_FINDINGS_MARKDOWN = "## Key Findings\nSummarize the important results generated in this notebook.\n"

SECTION_KEYWORDS = {
    'Data Loading': ['pd\.read_csv', 'spark\.read', 'load_data', 'db_connection'],
    'Data Cleaning': ['fillna', 'dropna', 'drop_duplicates', 'astype', 'to_datetime', 'replace', 'clean_data', 'handle_missing'],
    'Exploratory Data Analysis': ['describe', 'value_counts', 'groupby', 'corr', 'sns\.', 'plt\.', 'plot_'],
    'Feature Engineering': ['feature_engineer', 'apply', 'lambda', 'get_dummies', 'scaler', 'transform_features'],
    'Performance Analysis': ['calculate_returns', 'performance_metrics', 'sharpe_ratio', 'alpha', 'beta'],
    'Risk Analytics': ['calculate_risk', 'max_drawdown', 'volatility', 'risk_score'],
    'Visualization': ['matplotlib\.pyplot', 'seaborn', 'plot_'],
    'Conclusion': ['summary', 'final_results', 'conclusion']
}

# --- Helper Functions ---
def remove_debug_prints(code_string):
    debug_patterns_to_remove = [
        r'print\s*\(df\.head\(\)\)',
        r'print\s*\(df\.columns\)',
        r'print\s*\(df\.info\(\)\)',
        r'print\s*\( *"[tT]est" *\)',
        r'print\s*\( *"[cC]hecking" *\)',
        r'print\s*\( *f"[tT]est.*" *\)',
        r'print\s*\( *f"[cC]hecking.*" *\)'
    ]
    for pattern in debug_patterns_to_remove:
        code_string = re.sub(pattern, '', code_string)
    return code_string.strip()

def add_docstrings(code_string):
    lines = code_string.splitlines()
    new_lines = []
    in_function = False
    for i, line in enumerate(lines):
        if line.strip().startswith('def ') and not in_function:
            in_function = True
            new_lines.append(line)
            indent = len(line) - len(line.lstrip())
            tq = chr(34)*3
            doc = f"{tq}\n{' '*(indent+4)}Description of function\n\n{' '*(indent+4)}Returns:\n{' '*(indent+8)}...\n{' '*(indent+4)}{tq}"
            new_lines.append(' ' * (indent + 4) + doc)
        elif in_function and not line.strip():
            in_function = False
            new_lines.append(line)
        else:
            new_lines.append(line)
    return "\n".join(new_lines)

def apply_cleanup_to_cell_source(cell_source):
    cleaned_source = remove_debug_prints(cell_source)
    cleaned_source = add_docstrings(cleaned_source)
    return cleaned_source.strip()

def get_section_heading(cell_source):
    for heading, keywords in SECTION_KEYWORDS.items():
        for keyword in keywords:
            if re.search(keyword, cell_source, re.IGNORECASE):
                return f"## {heading}"
    return None

def process_notebook(notebook_path, output_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    cleaned_cells = []
    cleaned_cells.append(new_markdown_cell(get_notebook_intro(os.path.basename(notebook_path))))
    last_head = None
    for cell in nb.cells:
        if cell.cell_type == 'code':
            head = get_section_heading(cell.source)
            if head and head != last_head:
                cleaned_cells.append(new_markdown_cell(head))
                last_head = head
            cell.source = apply_cleanup_to_cell_source(cell.source)
            if cell.source.strip(): cleaned_cells.append(cell)
        else: cleaned_cells.append(cell)
    cleaned_cells.append(new_markdown_cell(KEY_FINDINGS_MARKDOWN))
    nb.cells = cleaned_cells
    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print(f"Processed: {os.path.basename(output_path)}")

def cleanup_all_notebooks(base_dir):
    nb_dir = os.path.join(base_dir, 'notebooks')
    out_dir = os.path.join(base_dir, 'notebooks_cleaned')
    if not os.path.exists(out_dir): os.makedirs(out_dir)
    for f in os.listdir(nb_dir):
        if f.endswith('.ipynb'):
            process_notebook(os.path.join(nb_dir, f), os.path.join(out_dir, f'CLEANED_{f}'))
    print("Cleanup Complete!")
