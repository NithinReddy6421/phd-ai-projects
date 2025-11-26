# Script-style notebook for analysis of sparse reconstruction
import numpy as np
from utils import compute_reprojection_errors
errors = compute_reprojection_errors('out/sparse')
print('Mean reprojection error:', sum(errors)/len(errors))