import bk7084 as bk
import numpy as np
from numpy.random import randint, rand

"""
Materials are used to define the appearance of a mesh.
"""
material_stone_bricks = bk.Material()
material_stone_bricks.textures = {
    "diffuse_texture": bk.res_path("../03_textures/assets/stone_bricks_col.jpg"),
    "normal_texture": bk.res_path("../03_textures/assets/stone_bricks_nrm.png"),
    "specular_texture": bk.res_path("../03_textures/assets/stone_bricks_refl.jpg"),
    "shininess_texture": bk.res_path("../03_textures/assets/stone_bricks_gloss.jpg"),
}

material_basic_bricks = bk.Material()
material_basic_bricks.specular = bk.Color(0.1, 0.1, 0.1)
material_basic_bricks.textures = {
    "diffuse_texture": bk.res_path("../assets/brick.jpg"),
}

material_basic_floor = bk.Material()
material_basic_floor.diffuse = bk.Color(0.8, 0.5, 0.5)

material_basic_window = bk.Material()
material_basic_window.textures = {
    "diffuse_texture": bk.res_path("../assets/window.jpg"),
}

material_basic_ground = bk.Material()
material_basic_ground.textures = {
    "diffuse_texture": bk.res_path("../assets/grass.jpg"),
}

material_mosaic_tiles = bk.Material()
material_mosaic_tiles.textures = {
    "diffuse_texture": bk.res_path("../03_textures/assets/mosaic_tiles_col.png"),
    "normal_texture": bk.res_path("../03_textures/assets/mosaic_tiles_nrm.png"),  
    "specular_texture": bk.res_path("../03_textures/assets/mosaic_tiles_refl.png"), 
    "shininess_texture": bk.res_path("../03_textures/assets/mosaic_tiles_gloss.png")
}

mat_office_delfts = bk.Material()
mat_office_delfts.textures = {
   "diffuse_texture": bk.res_path("C:/Users/rbjwe/BK7084-end-project/05_optimization/assets/Tiles101_2K-PNG/Tiles101_2K-PNG_Color.png"),
    #"normal_texture": bk.res_path("../05_optimization/assets\Tiles101_2K-PNG\Tiles101_2K-PNG_NormalGL.png"),  
    #"specular_texture": bk.res_path("../05_optimization/assets\Tiles101_2K-PNG\Tiles101_2K-PNG_Displacement.png"), 
    #"shininess_texture": bk.res_path("../05_optimization/assets\Tiles101_2K-PNG\Tiles101_2K-PNG_AmbientOcclusion.png")
}

class BasicWall(bk.Mesh):
    """
    Create a basic wall mesh with the given size and material.
    This class is a subclass of bk.Mesh, so it can be used as a mesh. For example,
    you can create a mesh instance by `mesh = BasicWallMesh(...)`, and then add it to
    a scene by `app.add_mesh(mesh)`. It's the same as using `mesh = create_basic_wall(...)`.
    """

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w, h, m=material_basic_bricks):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "BasicWallMesh"
        self.positions = [
            [-w / 2, -h / 2, 0],
            [w / 2, -h / 2, 0],
            [w / 2, h / 2, 0],
            [-w / 2, h / 2, 0],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.materials = [m]


class BasicFloor(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w, h, m=material_basic_floor):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "BasicFloorMesh"
        # self.materials = materials
        self.positions = [
            [-w / 2, 0, -h / 2],
            [w / 2, 0, -h / 2],
            [w / 2, 0, h / 2],
            [-w / 2, 0, h / 2],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 2, 1], [0, 3, 2]]
        self.materials = [m]

class OfficeFloor(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w, h, m=material_basic_floor):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "OfficeFloormesh"
        # self.materials = materials
        self.positions = [
            [-w/2, 0, h/2],
            [-w/2, 0, -h/6],
            [-w/6, 0, h/2],
            [-w/6, 0, -h/6],
            [-w/2, 0, -h/2],
            [w/2, 0, -h/2],
            [w/2, 0, -h/6],
            [w/6, 0, -h/6],
            [w/6, 0, h/2],
            [w/2, 0, h/2]
        ]
        self.texcoords = [
            [0, 1],
            [0, 1/3],
            [1/3, 1],
            [1/3, 1/3],
            [0, 0],
            [1, 0],
            [1, 1/3],
            [2/3, 1/3],
            [2/3, 1],
            [1, 1]
            ]
        self.triangles = [
            [1, 0, 2],
            [1, 2, 3],
            [4, 1, 6],
            [4, 6, 5],
            [7, 9, 6],
            [7, 8, 9]
            ]
        self.materials = [m]

class OfficeWall1(bk.Mesh):
    """
    Create a basic wall mesh with the given size and material.
    This class is a subclass of bk.Mesh, so it can be used as a mesh. For example,
    you can create a mesh instance by `mesh = BasicWallMesh(...)`, and then add it to
    a scene by `app.add_mesh(mesh)`. It's the same as using `mesh = create_basic_wall(...)`.
    """

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w, h, m=mat_office_delfts):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "BasicWallMesh"
        self.positions = [
            [-w / 3, -h / 6, 0],
            [w / 3, -h / 6, 0],
            [w / 3, h / 6, 0],
            [-w / 3, h / 6, 0],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1/2], [0, 1/2]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.materials = [m]

class BasicWindowWall(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w, h):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "BasicWindowWallMesh"
        # self.materials = materials
        self.positions = [
            [-w/2, -h/2, 0.0], [w/2, -h/2, 0.0], [w/2, h/2, 0.0], [-w/2, h/2, 0.0],
            [-w*0.2, -h*0.2, 0.0], [w*0.2, -h*0.2, 0.0], [w*0.2, h*0.2, 0.0], [-w*0.2, h*0.2, 0.0],
            [-w*0.2, -h*0.2, 0.0], [w*0.2, -h*0.2, 0.0], [w*0.2, h*0.2, 0.0], [-w*0.2, h*0.2, 0.0],
        ]
        self.texcoords = [
            [0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0, 1.0],
            [0.3, 0.3], [0.7, 0.3], [0.7, 0.7], [0.3, 0.7],
            [0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0, 1.0]
        ]
        self.triangles = [
            [0, 1, 5], [0, 5, 4], [1, 2, 6], [1, 6, 5], [2, 3, 7], [2, 7, 6], [3, 0, 4], [3, 4, 7],
            [8, 9, 10], [8, 10, 11],
        ]
        self.materials = [
            material_basic_bricks,
            material_basic_window,
        ]
        self.sub_meshes = [
            bk.SubMesh(0, 8, 0),
            bk.SubMesh(8, 10, 1),
        ]

class HighriseFloor(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w, h, m=material_basic_floor):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "HighriseFloormesh"
        # self.materials = materials
        self.materials = [m] 
        coords = []
        triangles = []
        pi_over_6 = np.pi / 6  # Using 12 sides for the dodecagon

        # Generate coordinates and triangles
        for i in range(12):
            coords.append([np.sin(i * pi_over_6), 0, np.cos(i * pi_over_6)])
            if i < 10:  # Adjusted to create triangles for a dodecagon
                triangles.append([0, i + 1, i + 2])

        # Transform the coordinates and create texture coordinates
        self.positions = np.array(coords) * w
        self.texcoords = np.array(coords)[:,:2]*0.5 + 0.5

        # Assign values to mesh properties
        self.triangles = triangles
        self.materials = [m]

class SkyscraperFloor(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w, h, m=material_basic_floor):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "OfficeFloormesh"
        # self.materials = materials
        self.positions = [[-0.5*w, 0, -0.25*np.sqrt(3)*w],
                          [0, 0, 0.25*np.sqrt(3)*w],
                          [0.5*w, 0, -0.25*np.sqrt(3)*w]
        ]
        self.texcoords = [[0,0],
                          [0.5,0.5*np.sqrt(3)],
                          [1,0]
            ]
        self.triangles = [[0,1,2]
            ]
        self.materials = [m]