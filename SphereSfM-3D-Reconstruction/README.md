# SphereSfM-3D-Reconstruction

Research-grade pipeline template for Structure-from-Motion (SfM) on spherical images.

**Contents**
- `pipeline.py` - example end-to-end pipeline orchestration script (feature extraction -> matching -> COLMAP calls -> sparse to dense flow)
- `colmap_runner.py` - helper to call COLMAP CLI (assumes COLMAP installed)
- `utils.py` - image handling, spherical projection helpers
- `notebooks/analysis.py` - scripted notebook for reprojection/error analysis
- `requirements.txt` - python dependencies
- `examples/` - instructions and placeholders for dataset
- `EXPERIMENTS.md` - how to run reproducible experiments and metrics to collect (reprojection error, completeness)

## Quick start
1. Install COLMAP (https://colmap.github.io/).
2. Create a working folder `data/` and add your spherical images (do NOT upload datasets to GitHub).
3. `pip install -r requirements.txt`
4. Run `python pipeline.py --data_dir data/ --output out/ --run_colmap True`

## Notes for reproducibility
- Do not commit image datasets; include a `data/README.md` describing how to obtain/prepare imagery.
- `EXPERIMENTS.md` contains reproducible config parameters and evaluation scripts.