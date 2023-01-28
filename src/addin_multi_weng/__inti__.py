bl_info = {
    "name": "WENG2 ADD Object",
    "author": "WENG U",
    "version": (0, 1, 0),
    "blender": (3, 4, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "{BLENDER_MANUAL_URL}/addons/camera/xxx.html",
    "category": "Add Mesh",
}

import bpy
import os

if "bpy" in locals():
    print("reloading .py files")
    import importlib

    from . import add_plane
    importlib.reload(add_plane)
# first time loading add-on
else:
    print("importing .py files")
    import bpy
    from . import add_plane


# =========================================================================
# Registration:
# =========================================================================


def register():
    add_plane.register()


def unregister():
    add_plane.unregister()


if __name__ == "__main__":
    register()
