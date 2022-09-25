"""The module to define keyword link mappings.
"""

from typing import Dict

_Keyword = str
_DocFileName = str

MAPPINGS: Dict[_Keyword, _DocFileName] = {
    "Stage": "stage",
    "Sprite": "sprite",
    "save_overall_html": "save_overall_html",
    "add_child": "add_child_and_remove_child",
    "remove_child": "add_child_and_remove_child",
    "display_on_jupyter": "display_on_jupyter",
    "display_on_colaboratory": "display_on_colaboratory",
    "append_js_expression": "append_js_expression",
    "remove_children": "remove_children",
    "contains": "contains",
    "num_children": "num_children",
    "get_child_at": "get_child_at",
    "Int": "int_and_number",
    "Number": "int_and_number",
    "Float": "int_and_number",
    "String": "string",
    "Boolean": "boolean",
    "Bool": "boolean",
    "Array": "array",
    "Dictionary": "dictionary",
    "DisplayObject": "display_object",
    "get_css": "display_object_get_and_set_css",
    "set_css": "display_object_get_and_set_css",
    "fill_color": "graphics_base_fill_color",
    "fill_alpha": "graphics_base_fill_alpha",
    "line_color": "graphics_base_line_color",
    "line_alpha": "graphics_base_line_alpha",
    "line_thickness": "graphics_base_line_thickness",
    "line_dot_setting": "graphics_base_line_dot_setting",
    "line_dash_setting": "graphics_base_line_dash_setting",
    "line_round_dot_setting": "graphics_base_line_round_dot_setting",
    "line_dash_dot_setting": "graphics_base_line_dash_dot_setting",
    "rotation_around_center": "graphics_base_rotation_around_center",
    "get_rotation_around_point": "graphics_base_rotation_around_point",
    "set_rotation_around_point": "graphics_base_rotation_around_point",
    "scale_x_from_center": "graphics_base_scale_from_center",
    "scale_y_from_center": "graphics_base_scale_from_center",
    "get_scale_x_from_point": "graphics_base_scale_from_point",
    "get_scale_y_from_point": "graphics_base_scale_from_point",
    "set_scale_x_from_point": "graphics_base_scale_from_point",
    "set_scale_y_from_point": "graphics_base_scale_from_point",
    "flip_x": "graphics_base_flip_interfaces",
    "flip_y": "graphics_base_flip_interfaces",
    "skew_x": "graphics_base_skew",
    "skew_y": "graphics_base_skew",
    "Rectangle": "rectangle",
    "Circle": "circle",
    "Ellipse": "ellipse",
    "Line": "line",
    "Polyline": "polyline",
    "Polygon": "polygon",
    "Path": "path",
    "Graphics": "graphics",
    "begin_fill": "graphics_begin_fill",
    "line_style": "graphics_line_style",
    "draw_rect": "graphics_draw_rect",
    "draw_round_rect": "graphics_draw_round_rect",
    "draw_circle": "graphics_draw_circle",
    "draw_ellipse": "graphics_draw_ellipse",
    "draw_line": "graphics_draw_line",
    "draw_dotted_line": "graphics_draw_dotted_line",
    "draw_dashed_line": "graphics_draw_dashed_line",
    "draw_round_dotted_line": "graphics_draw_round_dotted_line",
    "draw_dash_dotted_line": "graphics_draw_dash_dotted_line",
    "draw_polygon": "graphics_draw_polygon",
    "draw_path": "graphics_draw_path",
    "Point2D": "point2d",
    "PathMoveTo": "path_move_to",
    "PathLineTo": "path_line_to",
    "PathHorizontal": "path_horizontal",
    "PathVertical": "path_vertical",
    "PathClose": "path_close",
    "PathBezier2D": "path_bezier_2d",
    "PathBezier2DContinual": "path_bezier_2d_continual",
    "PathBezier3D": "path_bezier_3d",
    "PathBezier3DContinual": "path_bezier_3d_continual",
    "prevent_default": "event_prevent_default_and_stop_propagation",
    "stop_propagation": "event_prevent_default_and_stop_propagation",
    "bind_custom_event": "bind_and_trigger_custom_event",
    "trigger_custom_event": "bind_and_trigger_custom_event",
    "MouseEvent": "mouse_event_abstract",
    "click": "click",
    "unbind_click": "click",
    "unbind_click_all": "click",
    "dblclick": "dblclick",
    "unbind_dblclick": "dblclick",
    "unbind_dblclick_all": "dblclick",
    "mousedown": "mousedown_and_mouseup",
    "mouseup": "mousedown_and_mouseup",
    "unbind_mousedown": "mousedown_and_mouseup",
    "unbind_mousedown_all": "mousedown_and_mouseup",
    "unbind_mouseup": "mousedown_and_mouseup",
    "unbind_mouseup_all": "mousedown_and_mouseup",
    "mouseover": "mouseover_and_mouseout",
    "mouseout": "mouseover_and_mouseout",
    "unbind_mouseover": "mouseover_and_mouseout",
    "unbind_mouseover_all": "mouseover_and_mouseout",
    "unbind_mouseout": "mouseover_and_mouseout",
    "unbind_mouseout_all": "mouseover_and_mouseout",
    "mousemove": "mousemove",
    "unbind_mousemove": "mousemove",
    "unbind_mousemove_all": "mousemove",
    "If": "if",
    "Elif": "elif",
    "Else": "else",
    "Return": "return",
    "For": "for",
    "Continue": "continue",
    "Timer": "timer",
    "TimerEvent": "timer_event",
    "FPS": "fps",
    "timer_complete": "timer_complete",
    "AnimationEvent": "animation_event",
    "animation_complete": "animation_complete",
    "animation_pause": "animation_pause_and_play",
    "animation_play": "animation_pause_and_play",
    "animation_reset": "animation_reset",
    "animation_finish": "animation_finish",
    "animation_reverse": "animation_reverse",
    "animation_time": "animation_time",
    "Easing": "easing_enum",
    "animation_parallel": "animation_parallel",
    "animation_move": "animation_move",
    "animation_x": "animation_x",
    "animation_y": "animation_y",
    "animation_width": "animation_width_and_height",
    "animation_height": "animation_width_and_height",
    "animation_fill_color": "animation_fill_color",
    "animation_fill_alpha": "animation_fill_alpha",
    "animation_line_color": "animation_line_color",
    "animation_line_alpha": "animation_line_alpha",
    "animation_line_thickness": "animation_line_thickness",
    "animation_radius": "animation_radius",
    "animation_rotation_around_center": "animation_rotation_around_center",
    "animation_rotation_around_point": "animation_rotation_around_point",
    "animation_scale_x_from_center": "animation_scale_x_and_y_from_center",
    "animation_scale_y_from_center": "animation_scale_x_and_y_from_center",
    "animation_scale_x_from_point": "animation_scale_x_and_y_from_point",
    "animation_scale_y_from_point": "animation_scale_x_and_y_from_point",
    "delete": "delete",
    "trace": "trace",
    "set_debug_mode": "set_debug_mode",
    "unset_debug_mode": "unset_debug_mode",
    "add_debug_info_setting": "add_debug_info_setting",
    "variable_name_suffix": "variable_name_suffix",
    "assert_equal": "assert_equal_and_not_equal",
    "assert_not_equal": "assert_equal_and_not_equal",
    "assert_true": "assert_true_and_false",
    "assert_false": "assert_true_and_false",
    "assert_arrays_equal": "assert_arrays_equal_and_arrays_not_equal",
    "assert_arrays_not_equal": "assert_arrays_equal_and_arrays_not_equal",
    "assert_dicts_equal": "assert_dicts_equal_and_dicts_not_equal",
    "assert_dicts_not_equal": "assert_dicts_equal_and_dicts_not_equal",
    "assert_defined": "assert_defined_and_undefined",
    "assert_undefined": "assert_defined_and_undefined",
    "assert_dicts_equal": "assert_dicts_equal_and_dicts_not_equal",
    "assert_dicts_not_equal": "assert_dicts_equal_and_dicts_not_equal",
    "assert_defined": "assert_defined_and_undefined",
    "assert_undefined": "assert_defined_and_undefined",
}
