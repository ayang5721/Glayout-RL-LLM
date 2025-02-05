# This file contains the enforcer function for the reinforcement learning model.

# Given a gds layout 

import subprocess

script_path = "run_drc.sh"
result = subprocess.run(["bash", script_path], capture_output=True, text=True)

print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
