#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# 
# blender scripts first.
# 
# author Cheetah
# version: v 0.1.0
# date 2023-01-27 23:08
#

import bpy
from random import randint
import numpy as np

"""

REF
https://docs.blender.org/manual/zh-hans/dev/editors/python_console.html
blender python中安装库，https://blog.csdn.net/weixin_42417376/article/details/124674837
blender api: https://docs.blender.org/api/current/info_quickstart.html

F:\DS\_ws\blender\3.4\python\bin
bpy的安装：F:\DS\_ws\blender\3.4\python\bin>.\python.exe -m pip install fake-bpy-module-3.4

调试：https://blog.csdn.net/sam_shan/article/details/120995582

Examples
https://blog.csdn.net/qq_43331089/article/details/123397323
"""


# 随机创建100个cube，x/y/z范围限制（-30，30）
number = 100
for i in range(0, number):
    x = randint(-30, 30)
    y = randint(-30, 30)
    z = randint(-30, 30)
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
