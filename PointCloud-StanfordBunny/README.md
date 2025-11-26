# PointCloud-StanfordBunny

Research-focused point cloud processing and analysis for the Stanford Bunny dataset.

## Contents
- `clean_pointcloud.py` - noise removal, outlier filtering, voxel downsampling with Open3D
- `mesh_from_pointcloud.py` - Poisson/ball-pivoting meshing workflow
- `analysis/curvature_analysis.py` - curvature and surface property scripts
- `notebooks/visualization.py` - example visualization script
- `requirements.txt`

## Quick start
1. Place `bun_zipper.ply` or `bun.ply` in `data/` (do NOT commit large data to repo)
2. `pip install -r requirements.txt`
3. `python clean_pointcloud.py --input data/bun.ply --output out/clean.ply`