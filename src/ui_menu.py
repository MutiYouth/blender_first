#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# 
# 在blender的info窗口中，添加一个menu
# 
# author Cheetah
# version: v 0.1.0
# date 2023-01-28 21:39
#
import bpy

"""


REF
参考了 Shift + F11下的 Templates中的DEMO。
"""


# noinspection PyUnusedName
class CustomMenu(bpy.types.Menu):
    bl_label = "WENG’S TOOLS"  # Menu, 以bl_开头的，都是系统的属性
    bl_idname = "WENG_OBJECT_MT_custom_menu"

    def draw(self, context):
        layout = self.layout

        layout.operator("wm.open_mainfile")
        layout.operator("wm.save_as_mainfile").copy = True

        layout.operator("object.shade_smooth")

        layout.label(text="Hello WENG, Dear!", icon='WORLD_DATA')

        # use an operator enum property to populate a sub-menu
        layout.operator_menu_enum("object.select_by_type",
                                  property="type",
                                  text="Select All by Type",
                                  )

        # call another menu
        layout.operator("wm.call_menu", text="Unwrap").name = "VIEW3D_MT_uv_map"


def draw_item(self, context):
    layout = self.layout
    layout.menu(CustomMenu.bl_idname)


def register():
    bpy.utils.register_class(CustomMenu)

    # lets add ourselves to the main header
    bpy.types.INFO_HT_header.append(draw_item)  # INFO_HT_header, Info窗口; VIEW3D_HT_header


def unregister():
    bpy.utils.unregister_class(CustomMenu)

    bpy.types.INFO_HT_header.remove(draw_item)


if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=CustomMenu.bl_idname)
