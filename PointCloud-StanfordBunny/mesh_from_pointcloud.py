import open3d as o3d, argparse
def make_mesh(ply_in, mesh_out):
    pcd = o3d.io.read_point_cloud(ply_in)
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.01, max_nn=30))
    mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=9)
    o3d.io.write_triangle_mesh(mesh_out, mesh)
    print('Saved mesh to', mesh_out)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True)
    p.add_argument('--output', required=True)
    args = p.parse_args()
    make_mesh(args.input, args.output)