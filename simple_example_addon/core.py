"""
A deliberately tiny example: one operator that adds a cube with a custom
name prefix, and one panel to trigger it. Replace this file's contents
with your real addon logic later — everything else in this template
stays the same regardless of what your addon actually does.
"""

import bpy


class SIMPLE_OT_add_named_cube(bpy.types.Operator):
    bl_idname = "simple_example.add_named_cube"
    bl_label = "Add Named Cube"
    bl_description = "Adds a cube and renames it using the prefix below"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        prefix = context.scene.simple_example_prefix
        bpy.ops.mesh.primitive_cube_add()
        obj = context.active_object
        obj.name = f"{prefix}_Cube"
        self.report({'INFO'}, f"Added {obj.name}")
        return {'FINISHED'}


class SIMPLE_PT_panel(bpy.types.Panel):
    bl_label = "Simple Example"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Simple Example"

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "simple_example_prefix")
        layout.operator(SIMPLE_OT_add_named_cube.bl_idname, icon='CUBE')


classes = (
    SIMPLE_OT_add_named_cube,
    SIMPLE_PT_panel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.simple_example_prefix = bpy.props.StringProperty(
        name="Prefix",
        default="MyPlugin",
    )


def unregister():
    del bpy.types.Scene.simple_example_prefix

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)