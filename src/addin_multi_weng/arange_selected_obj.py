import bpy



# REF


sel = bpy.context.selected_objects

loc_x = loc_y = loc_z = 0

for obj in sel: 
    
    # obj.location = （loc_x,loc_y,loc_z）
    
    # loc_x+=5
    print(obj.location)