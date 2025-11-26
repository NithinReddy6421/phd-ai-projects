# Example experiment script for agriculture yield experiments
import yaml, subprocess
cfg = yaml.safe_load(open('configs/default.yaml'))
print('Run training with config:', cfg['output']['model_path'])