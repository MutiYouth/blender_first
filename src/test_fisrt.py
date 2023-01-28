#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# 
# blender scripts first.
# 
# author Cheetah
# version: v 0.1.0
# date 2023-01-27 23:08
#

from random import randint

import bpy
import pydevd_pycharm

"""

REF
https://docs.blender.org/manual/zh-hans/dev/editors/python_console.html
blender python中安装库，https://blog.csdn.net/weixin_42417376/article/details/124674837
blender api: https://docs.blender.org/api/current/info_quickstart.html

F:\DS\_ws\blender\3.4\python\bin
bpy的安装：F:\DS\_ws\blender\3.4\python\bin>.\python.exe -m pip install fake-bpy-module-3.4

调试
https://blog.csdn.net/weixin_43775400/article/details/124777871
https://zhuanlan.zhihu.com/p/595184674
F:\DS\_ws\blender\3.4\python\bin>.\python.exe -m pip install pydevd-pycharm~=223.7571.182
在 D:\Pros\IDE\Cache\.IntelliJIdea2019.2\config\plugins\python\debugger-eggs-output 中找到 pydevd-pycharm.egg



Examples
https://blog.csdn.net/qq_43331089/article/details/123397323
"""

pydevd_pycharm.settrace('localhost', port=1090, stdoutToServer=True, stderrToServer=True)

# 随机创建100个cube，x/y/z范围限制（-30，30）
number = 100
for i in range(0, number):
    x = randint(-30, 30)
    y = randint(-30, 30)
    z = randint(-30, 30)
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
