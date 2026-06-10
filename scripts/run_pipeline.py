
# run_pipeline.py

import subprocess
import os

def run_script(script_path):
    try:
        print(f"Running {script_path}...")
        subprocess.run(['python', script_path], check=True)
        print(f"Successfully ran {script_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}")
    except FileNotFoundError:
        print(f"Error: Python interpreter not found or script not at {script_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Example of how you might call other scripts
    # run_script(os.path.join(base_dir, 'etl_pipeline.py'))
    # run_script(os.path.join(base_dir, 'live_nav_fetch.py'))
    # run_script(os.path.join(base_dir, 'compute_metrics.py'))
    # run_script(os.path.join(base_dir, 'recommender.py'))

    print("Master pipeline script created. Add your script execution logic here.")
