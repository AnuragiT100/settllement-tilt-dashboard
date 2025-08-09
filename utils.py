<<<<<<< HEAD
# src/utils.py
import numpy as np
import plotly.graph_objects as go

def box_vertices(width=10, depth=10, height=30):
    w, d, h = width / 2, depth / 2, height
    verts = np.array([
        [-w, -d, 0],
        [ w, -d, 0],
        [ w,  d, 0],
        [-w,  d, 0],
        [-w, -d, h],
        [ w, -d, h],
        [ w,  d, h],
        [-w,  d, h],
    ])
    return verts

def rotate_vertices(verts, tilt_x_deg=0.0, tilt_y_deg=0.0):
    rx = np.deg2rad(tilt_x_deg)
    ry = np.deg2rad(tilt_y_deg)
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(rx), -np.sin(rx)],
                   [0, np.sin(rx), np.cos(rx)]])
    Ry = np.array([[np.cos(ry), 0, np.sin(ry)],
                   [0, 1, 0],
                   [-np.sin(ry), 0, np.cos(ry)]])
    R = Ry @ Rx
    return verts.dot(R.T)

def plot_box(verts):
    x, y, z = verts.T
    i = [0, 0, 0, 1, 1, 2, 4, 5, 6, 4, 7, 3]
    j = [1, 2, 4, 2, 5, 3, 5, 6, 7, 7, 4, 0]
    k = [2, 4, 1, 5, 3, 0, 6, 7, 4, 0, 5, 7]
    mesh = go.Mesh3d(x=x, y=y, z=z, i=i, j=j, k=k, opacity=0.5)
    layout = go.Layout(scene=dict(aspectmode='auto'))
    fig = go.Figure(data=[mesh], layout=layout)
    return fig
=======
# src/utils.py
import numpy as np
import plotly.graph_objects as go

def box_vertices(width=10, depth=10, height=30):
    w, d, h = width / 2, depth / 2, height
    verts = np.array([
        [-w, -d, 0],
        [ w, -d, 0],
        [ w,  d, 0],
        [-w,  d, 0],
        [-w, -d, h],
        [ w, -d, h],
        [ w,  d, h],
        [-w,  d, h],
    ])
    return verts

def rotate_vertices(verts, tilt_x_deg=0.0, tilt_y_deg=0.0):
    rx = np.deg2rad(tilt_x_deg)
    ry = np.deg2rad(tilt_y_deg)
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(rx), -np.sin(rx)],
                   [0, np.sin(rx), np.cos(rx)]])
    Ry = np.array([[np.cos(ry), 0, np.sin(ry)],
                   [0, 1, 0],
                   [-np.sin(ry), 0, np.cos(ry)]])
    R = Ry @ Rx
    return verts.dot(R.T)

def plot_box(verts):
    x, y, z = verts.T
    i = [0, 0, 0, 1, 1, 2, 4, 5, 6, 4, 7, 3]
    j = [1, 2, 4, 2, 5, 3, 5, 6, 7, 7, 4, 0]
    k = [2, 4, 1, 5, 3, 0, 6, 7, 4, 0, 5, 7]
    mesh = go.Mesh3d(x=x, y=y, z=z, i=i, j=j, k=k, opacity=0.5)
    layout = go.Layout(scene=dict(aspectmode='auto'))
    fig = go.Figure(data=[mesh], layout=layout)
    return fig
>>>>>>> ff6ed34b7f408d0d84bd0ff98a752dc382751fb8
