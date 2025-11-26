#!/usr/bin/env python3
"""End-to-end SfM orchestration script (spherical-aware).
This script demonstrates how to prepare images, call COLMAP, and process sparse outputs.
Replace COLMAP call sections with your local COLMAP installation paths.
"""
import argparse, os, subprocess, shutil
from colmap_runner import run_colmap_sparse, run_colmap_dense
from utils import prepare_images, compute_reprojection_errors

def main(args):
    os.makedirs(args.output, exist_ok=True)
    db_path = os.path.join(args.output, 'database.db')
    sparse_dir = os.path.join(args.output, 'sparse')
    prepare_images(args.data_dir, args.output)
    if args.run_colmap:
        run_colmap_sparse(args.output, db_path, sparse_dir)
        run_colmap_dense(args.output, sparse_dir)
    # post-processing
    errors = compute_reprojection_errors(sparse_dir)
    print('Reprojection errors (sample):', errors[:5])

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--data_dir', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--run_colmap', default=False, action='store_true')
    args = p.parse_args()
    main(args)