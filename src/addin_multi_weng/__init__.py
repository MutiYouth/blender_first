bl_info = {
    "name": "WENG ADD Object",
    "author": "WENG L",
    "version": (0, 2, 0),
    "blender": (3, 4, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "{BLENDER_MANUAL_URL}/addons/camera/xxx.html",
    "category": "Add Mesh",
}

import bpy
import os

from . import add_plane
from . import add_cube


# =========================================================================
# Registration:
# =========================================================================


def register():
    add_plane.register()
    add_cube.register()


def unregister():
    add_plane.unregister()
    add_cube.unregister()


if __name__ == "__main__":
    register()
