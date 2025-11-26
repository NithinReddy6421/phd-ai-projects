import os, glob, shutil
from PIL import Image
def prepare_images(data_dir, output_dir):
    images_out = os.path.join(output_dir, 'images')
    os.makedirs(images_out, exist_ok=True)
    for img_path in glob.glob(os.path.join(data_dir, '*')):
        # simple copy; users may implement spherical pre-processing here
        shutil.copy(img_path, images_out)
    print('Images prepared in', images_out)

def compute_reprojection_errors(sparse_dir):
    # placeholder: parse COLMAP sparse outputs to compute reprojection errors
    return [0.5, 0.6, 0.4]