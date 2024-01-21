import random

from bk7084.math import *
from components import *


"""
This file contains the Skyscraper, Highrise, and Office classes.
These classes are used to generate buildings with different shapes and sizes.
The Skyscraper class is already implemented for you as an example.
You will need to implement the Highrise and Office classes yourself.

A building is made up of multiple components. Each component is a mesh. For
example, a skyscraper is made up of multiple floors, walls, and windows. Each
floor, wall, and window is a component. To generate a building, we need to
generate each component and place them in the correct position. 
 
But how do we place each component in the correct position? Of course, we can
place each component manually. But what if we want to translate the whole
building? We will need to translate each component individually. This is
tedious and error-prone.

Recall what we have learned in the hierarchy lecture, how do we construct the 
solar system? We parent each planet to the sun, and moon to each planet by 
multiplying the transformation of the parent right before the transformation
of the child. This way, all the children will be transformed correctly when
the parent is transformed.
 
We can do the same thing here. We can parent each component to a base 
component and only transform the base component. This way, all the children 
will be transformed correctly when the base component is transformed. This
time, we will use the app.spawn_building() function to spawn a base component
for us. The app.spawn_building() function will spawn a base component with
nothing in it. You can then parent other components to this base component.

Check out the `self.building` variable in the Skyscraper class. It is the base
component that we will use to parent other components. Go back to the main.py
file and you will see that we apply a transformation to the self.building
component. This transformation will be applied to all the children of the
self.building component. This is how we can translate the whole building.
"""


class Skyscraper:
    def __init__(self, app, num_floors, max_width):
        self.num_floors = num_floors
        self.building = app.spawn_building()
        self.building.set_visible(True)
        for i in range(self.num_floors):
            floor1 = app.add_mesh(SkyscraperFloor(max_width, max_width, material_basic_floor), parent=self.building)
            floor1.set_transform(Mat4.from_translation(Vec3(0, max_width * i, 0)))
            floor1.set_visible(True)
            floor2 = app.add_mesh(SkyscraperFloor(max_width, max_width, material_basic_ground), parent=floor1)
            floor2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
            floor2.set_visible(True)

            wall1 = app.add_mesh(OfficeWall2(max_width, max_width, lego), parent=floor1)
            wall1.set_transform(Mat4.from_rotation_y(60, True) * Mat4.from_translation(Vec3(0, max_width/2, 0.5*max_width*np.tan(np.pi/6))))
            wall1.set_visible(True)
            wall2 = app.add_mesh(BasicWindowWall(max_width, max_width), parent=floor1)
            wall2.set_transform(Mat4.from_rotation_y(180, True) * Mat4.from_translation(Vec3(0, max_width/2, 0.5*max_width*np.tan(np.pi/6))))
            wall2.set_visible(True)

            if i == 0:
                wall3 = app.add_mesh(DoorWall(max_width, max_width), parent=floor1)
            else:
                wall3 = app.add_mesh(OfficeWall1(3*max_width, 3*max_width), parent=floor1)
            wall3.set_transform(Mat4.from_rotation_y(-60, True) * Mat4.from_translation(Vec3(0, max_width/2, 0.5*max_width*np.tan(np.pi/6))))
            wall3.set_visible(True)


class Highrise:
    def __init__(self, app, num_floors, max_width):
        self.num_floors = num_floors
        # Spawn the building and save the reference to the building
        self.building = app.spawn_building()
        self.building.set_visible(True)
        max_width = max_width/2
        for i in range(self.num_floors):
            floor1 = app.add_mesh(HighriseFloor(max_width, max_width, material_basic_floor), parent=self.building)
            floor1.set_transform(Mat4.from_translation(Vec3(0, max_width*i, 0)) * Mat4.from_rotation_y(90 * i, True))
            floor1.set_visible(True)
            floor2 = app.add_mesh(HighriseFloor(max_width, max_width, Foto_dak), parent=floor1)
            floor2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
            floor2.set_visible(True)

            side = 2 * np.sin(np.pi / 12) * max_width
            angle = []
            wall_angle = []
            x_position = []
            z_position = []
            for n in range(12):
                phi = np.pi / 12 + n * np.pi / 6
                while -np.pi < phi < np.pi:
                    if phi < -np.pi:
                        phi = phi + 2 * np.pi
                    else:
                        phi = phi - 2 * np.pi
                
                angle.append(phi)
                wall_angle.append(np.degrees(phi))
                wall_distance = np.sqrt(max_width**2 - (side/2)**2)

                # Calculate the position of the wall
                x_position.append(np.sin(phi) * wall_distance)
                z_position.append(np.cos(phi) * wall_distance)
                y_position = max_width/2

            # Create and position the wall
            wall0 = app.add_mesh(OfficeWall2(side, max_width), parent=floor1)
            wall0.set_transform(Mat4.from_translation(Vec3(x_position[0], y_position, z_position[0])) * Mat4.from_rotation_y(wall_angle[0], True))
            wall0.set_visible(True)
            wall1 = app.add_mesh(OfficeWall2(side, max_width), parent=floor1)
            wall1.set_transform(Mat4.from_translation(Vec3(x_position[1], y_position, z_position[1])) * Mat4.from_rotation_y(wall_angle[1], True))
            wall1.set_visible(True)
            wall2 = app.add_mesh(OfficeWall2(side, max_width), parent=floor1)
            wall2.set_transform(Mat4.from_translation(Vec3(x_position[2], y_position, z_position[2])) * Mat4.from_rotation_y(wall_angle[2], True))
            wall2.set_visible(True)
            wall3 = app.add_mesh(OfficeWall2(side, max_width), parent=floor1)
            wall3.set_transform(Mat4.from_translation(Vec3(x_position[3], y_position, z_position[3])) * Mat4.from_rotation_y(wall_angle[3], True))
            wall3.set_visible(True)
            wall4 = app.add_mesh(OfficeWall2(side, max_width), parent=floor1)
            wall4.set_transform(Mat4.from_translation(Vec3(x_position[4], y_position, z_position[4])) * Mat4.from_rotation_y(wall_angle[4], True))
            wall4.set_visible(True)
            wall5 = app.add_mesh(OfficeWall2(side, max_width), parent=floor1)
            wall5.set_transform(Mat4.from_translation(Vec3(x_position[5], y_position, z_position[5])) * Mat4.from_rotation_y(wall_angle[5], True))
            wall5.set_visible(True)
            wall6 = app.add_mesh(OfficeWall2(side, max_width), parent=floor1)
            wall6.set_transform(Mat4.from_translation(Vec3(x_position[6], y_position, z_position[6])) * Mat4.from_rotation_y(wall_angle[6], True))
            wall6.set_visible(True)
            wall7 = app.add_mesh(OfficeWall2(side, max_width), parent=floor1)
            wall7.set_transform(Mat4.from_translation(Vec3(x_position[7], y_position, z_position[7])) * Mat4.from_rotation_y(wall_angle[7], True))
            wall7.set_visible(True)
            wall8 = app.add_mesh(OfficeWall2(side, max_width), parent=floor1)
            wall8.set_transform(Mat4.from_translation(Vec3(x_position[8], y_position, z_position[8])) * Mat4.from_rotation_y(wall_angle[8], True))
            wall8.set_visible(True)
            wall9 = app.add_mesh(OfficeWall2(side, max_width), parent=floor1)
            wall9.set_transform(Mat4.from_translation(Vec3(x_position[9], y_position, z_position[9])) * Mat4.from_rotation_y(wall_angle[9], True))
            wall9.set_visible(True)
            wall10 = app.add_mesh(OfficeWall2(side, max_width), parent=floor1)
            wall10.set_transform(Mat4.from_translation(Vec3(x_position[10], y_position, z_position[10])) * Mat4.from_rotation_y(wall_angle[10], True))
            wall10.set_visible(True)
            wall11 = app.add_mesh(OfficeWall2(side, max_width), parent=floor1)
            wall11.set_transform(Mat4.from_translation(Vec3(x_position[11], y_position, z_position[11])) * Mat4.from_rotation_y(wall_angle[11], True))
            wall11.set_visible(True)


class Office:

    def __init__(self, app, num_floors, max_width):
        self.num_floors = num_floors
        # Spawn the building and save the reference to the building
        self.building = app.spawn_building()
        self.building.set_visible(True)
        for i in range(self.num_floors):
            if i != 0:
                random = np.random.randint(0,4)
            else:
                random = 0
            floor1 = app.add_mesh(OfficeFloor(max_width, max_width, material_basic_floor), parent=self.building)
            floor1.set_transform(Mat4.from_translation(Vec3(0, max_width/3*i, 0)) * Mat4.from_rotation_y(90 * random, True))
            floor1.set_visible(True)
            floor2 = app.add_mesh(OfficeFloor(max_width, max_width, material_gold), parent=floor1)
            floor2.set_transform(Mat4.from_translation(Vec3(0, max_width/3, 0)))
            floor2.set_visible(True)
            if i != self.num_floors - 1:
                floor2 = app.add_mesh(OfficeFloor(max_width, max_width, material_gold), parent=floor1)
                floor2.set_transform(Mat4.from_translation(Vec3(0, max_width/3, 0)) * Mat4.from_rotation_x(180, True))
                floor2.set_visible(True)

            if i == 0:
                wall1 = app.add_mesh(DoorWall(max_width/3, max_width/3), parent=floor1)
            else:
                wall1 = app.add_mesh(OfficeWall1(max_width, max_width), parent=floor1)
            wall1.set_transform(Mat4.from_translation(Vec3(0, max_width / 6, -max_width / 6)))
            wall1.set_visible(True)
            wall2 = app.add_mesh(OfficeWall1(max_width, max_width), parent=floor1)
            wall2.set_transform(Mat4.from_translation(Vec3(max_width/3, max_width / 6, max_width / 2)))
            wall2.set_visible(True)
            wall3 = app.add_mesh(OfficeWall1(max_width, max_width), parent=floor1)
            wall3.set_transform(Mat4.from_translation(Vec3(-max_width/3, max_width / 6, max_width / 2)))
            wall3.set_visible(True)
            wall4 = app.add_mesh(OfficeWall1(max_width, max_width), parent=floor1)
            wall4.set_transform(Mat4.from_translation(Vec3(-max_width/6, max_width / 6, 0)) * Mat4.from_rotation_y(90, True))
            wall4.set_visible(True)
            wall5 = app.add_mesh(OfficeWall1(max_width, max_width), parent=floor1)
            wall5.set_transform(Mat4.from_translation(Vec3(max_width/6, max_width / 6, 0)) * Mat4.from_rotation_y(-90, True))
            wall5.set_visible(True)
            wall6 = app.add_mesh(OfficeWall1(max_width, max_width), parent=floor1)
            wall6.set_transform(Mat4.from_translation(Vec3(max_width/2, max_width / 6, 0)) * Mat4.from_rotation_y(90, True))
            wall6.set_visible(True)
            wall7 = app.add_mesh(OfficeWall1(max_width, max_width), parent=floor1)
            wall7.set_transform(Mat4.from_translation(Vec3(max_width/2, max_width / 6, max_width/3)) * Mat4.from_rotation_y(90, True))
            wall7.set_visible(True)
            wall8 = app.add_mesh(OfficeWall1(max_width, max_width), parent=floor1)
            wall8.set_transform(Mat4.from_translation(Vec3(max_width/2, max_width / 6, -max_width/3)) * Mat4.from_rotation_y(90, True))
            wall8.set_visible(True)

            wall9 = app.add_mesh(OfficeWall1(max_width, max_width), parent=floor1)
            wall9.set_transform(Mat4.from_translation(Vec3(max_width/3, max_width / 6, -max_width/2)) * Mat4.from_rotation_y(180, True))
            wall9.set_visible(True)
            wall10 = app.add_mesh(OfficeWall1(max_width, max_width), parent=floor1)
            wall10.set_transform(Mat4.from_translation(Vec3(0, max_width / 6, -max_width/2)) * Mat4.from_rotation_y(180, True))
            wall10.set_visible(True)
            wall11 = app.add_mesh(OfficeWall1(max_width, max_width), parent=floor1)
            wall11.set_transform(Mat4.from_translation(Vec3(-max_width/3, max_width / 6, -max_width/2)) * Mat4.from_rotation_y(180, True))
            wall11.set_visible(True)

            wall12 = app.add_mesh(OfficeWall1(max_width, max_width), parent=floor1)
            wall12.set_transform(Mat4.from_translation(Vec3(-max_width/2, max_width / 6, -max_width/3)) * Mat4.from_rotation_y(-90, True))
            wall12.set_visible(True)
            wall13 = app.add_mesh(OfficeWall1(max_width, max_width), parent=floor1)
            wall13.set_transform(Mat4.from_translation(Vec3(-max_width/2, max_width / 6, 0)) * Mat4.from_rotation_y(-90, True))
            wall13.set_visible(True)
            wall14 = app.add_mesh(OfficeWall1(max_width, max_width), parent=floor1)
            wall14.set_transform(Mat4.from_translation(Vec3(-max_width/2, max_width / 6, max_width/3)) * Mat4.from_rotation_y(-90, True))
            wall14.set_visible(True)

            wall15 = app.add_mesh(OfficeWall1(max_width, max_width), parent=floor1)
            wall15.set_transform(Mat4.from_translation(Vec3(max_width/6, max_width / 6, max_width/3)) * Mat4.from_rotation_y(-90, True))
            wall15.set_visible(True)
            wall16 = app.add_mesh(OfficeWall1(max_width, max_width), parent=floor1)
            wall16.set_transform(Mat4.from_translation(Vec3(-max_width/6, max_width / 6, max_width/3)) * Mat4.from_rotation_y(90, True))
            wall16.set_visible(True)



# pre-loaded park model
park_model = bk.Mesh.load_from(bk.res_path("./assets/park.obj"))


class Park:
    def __init__(self, app):
        self.building = app.add_mesh(park_model)
        self.building.set_visible(True)
        angle = random.randint(0, 3) * 90
        self.pre_transform = (
            Mat4.from_translation(Vec3(0, 1.4, 0))
            * Mat4.from_scale(Vec3(0.5))
            * Mat4.from_rotation_y(angle, True)
        )


# pre-loaded house model
house_model = bk.Mesh.load_from(bk.res_path("./assets/house.obj"))


class House:
    def __init__(self, app):
        self.building = app.add_mesh(house_model)
        self.building.set_visible(True)
        angle = random.randint(0, 3) * 90
        self.pre_transform = (
            Mat4.from_scale(Vec3(0.5))
            * Mat4.from_translation(Vec3(0, 6.8, 0))
            * Mat4.from_rotation_y(angle, True)
        )
