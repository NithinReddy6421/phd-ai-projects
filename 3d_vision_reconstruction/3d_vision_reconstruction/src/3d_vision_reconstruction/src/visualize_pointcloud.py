try:
    import open3d as o3d
except:
    o3d = None

def visualize(points):
    if o3d is None:
        print("Open3D not installed.")
        return
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    o3d.visualization.draw_geometries([pcd])
