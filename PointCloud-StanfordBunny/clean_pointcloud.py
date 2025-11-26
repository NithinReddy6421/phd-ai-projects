import argparse
import open3d as o3d
import numpy as np
def clean_pointcloud(path_in, out_path):
    pcd = o3d.io.read_point_cloud(path_in)
    print('Original points:', len(pcd.points))
    pcd, ind = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
    pcd = pcd.voxel_down_sample(voxel_size=0.002)
    o3d.io.write_point_cloud(out_path, pcd)
    print('Saved cleaned point cloud to', out_path)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True)
    p.add_argument('--output', required=True)
    args = p.parse_args()
    clean_pointcloud(args.input, args.output)