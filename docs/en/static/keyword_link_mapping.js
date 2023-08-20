
$(document).ready(function() {
    const KEYWORD_LINK_MAPPINGS = {"Stage": "https://simon-ritchie.github.io/apysc/en/stage.html", "Sprite": "https://simon-ritchie.github.io/apysc/en/sprite.html", "save_overall_html": "https://simon-ritchie.github.io/apysc/en/save_overall_html.html", "add_child": "https://simon-ritchie.github.io/apysc/en/add_child_and_remove_child.html", "remove_child": "https://simon-ritchie.github.io/apysc/en/add_child_and_remove_child.html", "display_on_jupyter": "https://simon-ritchie.github.io/apysc/en/display_on_jupyter.html", "display_on_colaboratory": "https://simon-ritchie.github.io/apysc/en/display_on_colaboratory.html", "append_js_expression": "https://simon-ritchie.github.io/apysc/en/append_js_expression.html", "remove_children": "https://simon-ritchie.github.io/apysc/en/remove_children.html", "contains": "https://simon-ritchie.github.io/apysc/en/contains.html", "num_children": "https://simon-ritchie.github.io/apysc/en/num_children.html", "get_child_at": "https://simon-ritchie.github.io/apysc/en/get_child_at.html", "Int": "https://simon-ritchie.github.io/apysc/en/int_and_number.html", "Number": "https://simon-ritchie.github.io/apysc/en/int_and_number.html", "Float": "https://simon-ritchie.github.io/apysc/en/int_and_number.html", "String": "https://simon-ritchie.github.io/apysc/en/string.html", "Str": "https://simon-ritchie.github.io/apysc/en/string.html", "Boolean": "https://simon-ritchie.github.io/apysc/en/boolean.html", "Bool": "https://simon-ritchie.github.io/apysc/en/boolean.html", "Array": "https://simon-ritchie.github.io/apysc/en/array.html", "Dictionary": "https://simon-ritchie.github.io/apysc/en/dictionary.html", "DisplayObject": "https://simon-ritchie.github.io/apysc/en/display_object.html", "get_css": "https://simon-ritchie.github.io/apysc/en/display_object_get_and_set_css.html", "set_css": "https://simon-ritchie.github.io/apysc/en/display_object_get_and_set_css.html", "fill_color": "https://simon-ritchie.github.io/apysc/en/graphics_base_fill_color.html", "fill_alpha": "https://simon-ritchie.github.io/apysc/en/graphics_base_fill_alpha.html", "line_color": "https://simon-ritchie.github.io/apysc/en/graphics_base_line_color.html", "line_alpha": "https://simon-ritchie.github.io/apysc/en/graphics_base_line_alpha.html", "line_thickness": "https://simon-ritchie.github.io/apysc/en/graphics_base_line_thickness.html", "line_dot_setting": "https://simon-ritchie.github.io/apysc/en/graphics_base_line_dot_setting.html", "line_dash_setting": "https://simon-ritchie.github.io/apysc/en/graphics_base_line_dash_setting.html", "line_round_dot_setting": "https://simon-ritchie.github.io/apysc/en/graphics_base_line_round_dot_setting.html", "line_dash_dot_setting": "https://simon-ritchie.github.io/apysc/en/graphics_base_line_dash_dot_setting.html", "rotation_around_center": "https://simon-ritchie.github.io/apysc/en/graphics_base_rotation_around_center.html", "get_rotation_around_point": "https://simon-ritchie.github.io/apysc/en/graphics_base_rotation_around_point.html", "set_rotation_around_point": "https://simon-ritchie.github.io/apysc/en/graphics_base_rotation_around_point.html", "scale_x_from_center": "https://simon-ritchie.github.io/apysc/en/graphics_base_scale_from_center.html", "scale_y_from_center": "https://simon-ritchie.github.io/apysc/en/graphics_base_scale_from_center.html", "get_scale_x_from_point": "https://simon-ritchie.github.io/apysc/en/graphics_base_scale_from_point.html", "get_scale_y_from_point": "https://simon-ritchie.github.io/apysc/en/graphics_base_scale_from_point.html", "set_scale_x_from_point": "https://simon-ritchie.github.io/apysc/en/graphics_base_scale_from_point.html", "set_scale_y_from_point": "https://simon-ritchie.github.io/apysc/en/graphics_base_scale_from_point.html", "flip_x": "https://simon-ritchie.github.io/apysc/en/graphics_base_flip_interfaces.html", "flip_y": "https://simon-ritchie.github.io/apysc/en/graphics_base_flip_interfaces.html", "skew_x": "https://simon-ritchie.github.io/apysc/en/graphics_base_skew.html", "skew_y": "https://simon-ritchie.github.io/apysc/en/graphics_base_skew.html", "Rectangle": "https://simon-ritchie.github.io/apysc/en/rectangle.html", "Circle": "https://simon-ritchie.github.io/apysc/en/circle.html", "Ellipse": "https://simon-ritchie.github.io/apysc/en/ellipse.html", "Line": "https://simon-ritchie.github.io/apysc/en/line.html", "Polyline": "https://simon-ritchie.github.io/apysc/en/polyline.html", "Polygon": "https://simon-ritchie.github.io/apysc/en/polygon.html", "Path": "https://simon-ritchie.github.io/apysc/en/path.html", "Graphics": "https://simon-ritchie.github.io/apysc/en/graphics.html", "begin_fill": "https://simon-ritchie.github.io/apysc/en/graphics_begin_fill.html", "line_style": "https://simon-ritchie.github.io/apysc/en/graphics_line_style.html", "line_cap": "https://simon-ritchie.github.io/apysc/en/graphics_line_style.html", "line_joints": "https://simon-ritchie.github.io/apysc/en/graphics_line_style.html", "draw_rect": "https://simon-ritchie.github.io/apysc/en/graphics_draw_rect.html", "draw_round_rect": "https://simon-ritchie.github.io/apysc/en/graphics_draw_round_rect.html", "draw_circle": "https://simon-ritchie.github.io/apysc/en/graphics_draw_circle.html", "draw_ellipse": "https://simon-ritchie.github.io/apysc/en/graphics_draw_ellipse.html", "draw_line": "https://simon-ritchie.github.io/apysc/en/graphics_draw_line.html", "draw_dotted_line": "https://simon-ritchie.github.io/apysc/en/graphics_draw_dotted_line.html", "draw_dashed_line": "https://simon-ritchie.github.io/apysc/en/graphics_draw_dashed_line.html", "draw_round_dotted_line": "https://simon-ritchie.github.io/apysc/en/graphics_draw_round_dotted_line.html", "draw_dash_dotted_line": "https://simon-ritchie.github.io/apysc/en/graphics_draw_dash_dotted_line.html", "draw_polygon": "https://simon-ritchie.github.io/apysc/en/graphics_draw_polygon.html", "draw_path": "https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html", "Point2D": "https://simon-ritchie.github.io/apysc/en/point2d.html", "PathMoveTo": "https://simon-ritchie.github.io/apysc/en/path_move_to.html", "PathLineTo": "https://simon-ritchie.github.io/apysc/en/path_line_to.html", "PathHorizontal": "https://simon-ritchie.github.io/apysc/en/path_horizontal.html", "PathVertical": "https://simon-ritchie.github.io/apysc/en/path_vertical.html", "PathClose": "https://simon-ritchie.github.io/apysc/en/path_close.html", "PathBezier2D": "https://simon-ritchie.github.io/apysc/en/path_bezier_2d.html", "PathBezier2DContinual": "https://simon-ritchie.github.io/apysc/en/path_bezier_2d_continual.html", "PathBezier3D": "https://simon-ritchie.github.io/apysc/en/path_bezier_3d.html", "PathBezier3DContinual": "https://simon-ritchie.github.io/apysc/en/path_bezier_3d_continual.html", "prevent_default": "https://simon-ritchie.github.io/apysc/en/event_prevent_default_and_stop_propagation.html", "stop_propagation": "https://simon-ritchie.github.io/apysc/en/event_prevent_default_and_stop_propagation.html", "bind_custom_event": "https://simon-ritchie.github.io/apysc/en/bind_and_trigger_custom_event.html", "trigger_custom_event": "https://simon-ritchie.github.io/apysc/en/bind_and_trigger_custom_event.html", "MouseEvent": "https://simon-ritchie.github.io/apysc/en/mouse_event_abstract.html", "click": "https://simon-ritchie.github.io/apysc/en/click.html", "unbind_click": "https://simon-ritchie.github.io/apysc/en/click.html", "unbind_click_all": "https://simon-ritchie.github.io/apysc/en/click.html", "dblclick": "https://simon-ritchie.github.io/apysc/en/dblclick.html", "unbind_dblclick": "https://simon-ritchie.github.io/apysc/en/dblclick.html", "unbind_dblclick_all": "https://simon-ritchie.github.io/apysc/en/dblclick.html", "mousedown": "https://simon-ritchie.github.io/apysc/en/mousedown_and_mouseup.html", "mouseup": "https://simon-ritchie.github.io/apysc/en/mousedown_and_mouseup.html", "unbind_mousedown": "https://simon-ritchie.github.io/apysc/en/mousedown_and_mouseup.html", "unbind_mousedown_all": "https://simon-ritchie.github.io/apysc/en/mousedown_and_mouseup.html", "unbind_mouseup": "https://simon-ritchie.github.io/apysc/en/mousedown_and_mouseup.html", "unbind_mouseup_all": "https://simon-ritchie.github.io/apysc/en/mousedown_and_mouseup.html", "mouseover": "https://simon-ritchie.github.io/apysc/en/mouseover_and_mouseout.html", "mouseout": "https://simon-ritchie.github.io/apysc/en/mouseover_and_mouseout.html", "unbind_mouseover": "https://simon-ritchie.github.io/apysc/en/mouseover_and_mouseout.html", "unbind_mouseover_all": "https://simon-ritchie.github.io/apysc/en/mouseover_and_mouseout.html", "unbind_mouseout": "https://simon-ritchie.github.io/apysc/en/mouseover_and_mouseout.html", "unbind_mouseout_all": "https://simon-ritchie.github.io/apysc/en/mouseover_and_mouseout.html", "mousemove": "https://simon-ritchie.github.io/apysc/en/mousemove.html", "unbind_mousemove": "https://simon-ritchie.github.io/apysc/en/mousemove.html", "unbind_mousemove_all": "https://simon-ritchie.github.io/apysc/en/mousemove.html", "If": "https://simon-ritchie.github.io/apysc/en/if.html", "Elif": "https://simon-ritchie.github.io/apysc/en/elif.html", "Else": "https://simon-ritchie.github.io/apysc/en/else.html", "Return": "https://simon-ritchie.github.io/apysc/en/return.html", "Continue": "https://simon-ritchie.github.io/apysc/en/continue.html", "Timer": "https://simon-ritchie.github.io/apysc/en/timer.html", "TimerEvent": "https://simon-ritchie.github.io/apysc/en/timer_event.html", "FPS": "https://simon-ritchie.github.io/apysc/en/fps.html", "fps": "https://simon-ritchie.github.io/apysc/en/fps.html", "timer_complete": "https://simon-ritchie.github.io/apysc/en/timer_complete.html", "AnimationEvent": "https://simon-ritchie.github.io/apysc/en/animation_event.html", "animation_complete": "https://simon-ritchie.github.io/apysc/en/animation_complete.html", "animation_pause": "https://simon-ritchie.github.io/apysc/en/animation_pause_and_play.html", "animation_play": "https://simon-ritchie.github.io/apysc/en/animation_pause_and_play.html", "animation_reset": "https://simon-ritchie.github.io/apysc/en/animation_reset.html", "animation_finish": "https://simon-ritchie.github.io/apysc/en/animation_finish.html", "animation_reverse": "https://simon-ritchie.github.io/apysc/en/animation_reverse.html", "animation_time": "https://simon-ritchie.github.io/apysc/en/animation_time.html", "Easing": "https://simon-ritchie.github.io/apysc/en/easing_enum.html", "animation_parallel": "https://simon-ritchie.github.io/apysc/en/animation_parallel.html", "animation_move": "https://simon-ritchie.github.io/apysc/en/animation_move.html", "animation_x": "https://simon-ritchie.github.io/apysc/en/animation_x.html", "animation_y": "https://simon-ritchie.github.io/apysc/en/animation_y.html", "animation_width": "https://simon-ritchie.github.io/apysc/en/animation_width_and_height.html", "animation_height": "https://simon-ritchie.github.io/apysc/en/animation_width_and_height.html", "animation_fill_color": "https://simon-ritchie.github.io/apysc/en/animation_fill_color.html", "animation_fill_alpha": "https://simon-ritchie.github.io/apysc/en/animation_fill_alpha.html", "animation_line_color": "https://simon-ritchie.github.io/apysc/en/animation_line_color.html", "animation_line_alpha": "https://simon-ritchie.github.io/apysc/en/animation_line_alpha.html", "animation_line_thickness": "https://simon-ritchie.github.io/apysc/en/animation_line_thickness.html", "animation_radius": "https://simon-ritchie.github.io/apysc/en/animation_radius.html", "animation_rotation_around_center": "https://simon-ritchie.github.io/apysc/en/animation_rotation_around_center.html", "animation_rotation_around_point": "https://simon-ritchie.github.io/apysc/en/animation_rotation_around_point.html", "animation_scale_x_from_center": "https://simon-ritchie.github.io/apysc/en/animation_scale_x_and_y_from_center.html", "animation_scale_y_from_center": "https://simon-ritchie.github.io/apysc/en/animation_scale_x_and_y_from_center.html", "animation_scale_x_from_point": "https://simon-ritchie.github.io/apysc/en/animation_scale_x_and_y_from_point.html", "animation_scale_y_from_point": "https://simon-ritchie.github.io/apysc/en/animation_scale_x_and_y_from_point.html", "delete": "https://simon-ritchie.github.io/apysc/en/delete.html", "trace": "https://simon-ritchie.github.io/apysc/en/trace.html", "set_debug_mode": "https://simon-ritchie.github.io/apysc/en/set_debug_mode.html", "unset_debug_mode": "https://simon-ritchie.github.io/apysc/en/unset_debug_mode.html", "add_debug_info_setting": "https://simon-ritchie.github.io/apysc/en/add_debug_info_setting.html", "variable_name_suffix": "https://simon-ritchie.github.io/apysc/en/variable_name_suffix.html", "assert_equal": "https://simon-ritchie.github.io/apysc/en/assert_equal_and_not_equal.html", "assert_not_equal": "https://simon-ritchie.github.io/apysc/en/assert_equal_and_not_equal.html", "assert_true": "https://simon-ritchie.github.io/apysc/en/assert_true_and_false.html", "assert_false": "https://simon-ritchie.github.io/apysc/en/assert_true_and_false.html", "assert_arrays_equal": "https://simon-ritchie.github.io/apysc/en/assert_arrays_equal_and_arrays_not_equal.html", "assert_arrays_not_equal": "https://simon-ritchie.github.io/apysc/en/assert_arrays_equal_and_arrays_not_equal.html", "assert_dicts_equal": "https://simon-ritchie.github.io/apysc/en/assert_dicts_equal_and_dicts_not_equal.html", "assert_dicts_not_equal": "https://simon-ritchie.github.io/apysc/en/assert_dicts_equal_and_dicts_not_equal.html", "assert_defined": "https://simon-ritchie.github.io/apysc/en/assert_defined_and_undefined.html", "assert_undefined": "https://simon-ritchie.github.io/apysc/en/assert_defined_and_undefined.html", "print": "https://simon-ritchie.github.io/apysc/en/trace.html", "ap.trace": "https://simon-ritchie.github.io/apysc/en/trace.html", "DateTime": "https://simon-ritchie.github.io/apysc/en/datetime.html", "assert_greater": "https://simon-ritchie.github.io/apysc/en/assert_greater_and_greater_equal.html", "assert_greater_equal": "https://simon-ritchie.github.io/apysc/en/assert_greater_and_greater_equal.html", "assert_less": "https://simon-ritchie.github.io/apysc/en/assert_less_and_less_equal.html", "assert_less_equal": "https://simon-ritchie.github.io/apysc/en/assert_less_and_less_equal.html", "TimeDelta": "https://simon-ritchie.github.io/apysc/en/timedelta.html", "total_seconds": "https://simon-ritchie.github.io/apysc/en/timedelta_total_seconds.html", "enter_frame": "https://simon-ritchie.github.io/apysc/en/enter_frame.html", "EnterFrame": "https://simon-ritchie.github.io/apysc/en/enter_frame.html", "unbind_enter_frame": "https://simon-ritchie.github.io/apysc/en/unbind_enter_frame_and_unbind_enter_frame_all.html", "unbind_enter_frame_all": "https://simon-ritchie.github.io/apysc/en/unbind_enter_frame_and_unbind_enter_frame_all.html", "Triangle": "https://simon-ritchie.github.io/apysc/en/triangle.html", "Math.min": "https://simon-ritchie.github.io/apysc/en/math_min.html", "Math.max": "https://simon-ritchie.github.io/apysc/en/math_max.html", "Math.trunc": "https://simon-ritchie.github.io/apysc/en/math_trunc.html", "delete_line_dot_setting": "https://simon-ritchie.github.io/apysc/en/graphics_base_line_dot_setting.html", "delete_line_dash_setting": "https://simon-ritchie.github.io/apysc/en/graphics_base_line_dash_setting.html", "delete_line_round_dot_setting": "https://simon-ritchie.github.io/apysc/en/graphics_base_line_round_dot_setting.html", "delete_line_dash_dot_setting": "https://simon-ritchie.github.io/apysc/en/graphics_base_line_dash_dot_setting.html", "draw_triangle": "https://simon-ritchie.github.io/apysc/en/graphics_draw_triangle.html", "SVGText": "https://simon-ritchie.github.io/apysc/en/svg_text.html", "SVGTextSpan": "https://simon-ritchie.github.io/apysc/en/svg_text_span.html", "create_with_svg_text_spans": "https://simon-ritchie.github.io/apysc/en/svg_text_span.html", "get_bounds": "https://simon-ritchie.github.io/apysc/en/get_bounds.html", "RectangleGeom": "https://simon-ritchie.github.io/apysc/en/rectangle_geom.html", "to_string": "https://simon-ritchie.github.io/apysc/en/to_string.html", "range": "https://simon-ritchie.github.io/apysc/en/range.html", "lstrip": "https://simon-ritchie.github.io/apysc/en/string_lstrip.html", "strip": "https://simon-ritchie.github.io/apysc/en/string_strip.html", "rstrip": "https://simon-ritchie.github.io/apysc/en/string_rstrip.html", "ForArrayIndices": "https://simon-ritchie.github.io/apysc/en/for_array_indices.html", "ForArrayValues": "https://simon-ritchie.github.io/apysc/en/for_array_values.html", "ForArrayIndicesAndValues": "https://simon-ritchie.github.io/apysc/en/for_array_indices_and_values.html", "ForDictKeys": "https://simon-ritchie.github.io/apysc/en/for_dict_keys.html", "ForDictValues": "https://simon-ritchie.github.io/apysc/en/for_dict_values.html", "ForDictKeysAndValues": "https://simon-ritchie.github.io/apysc/en/for_dict_keys_and_values.html", "True_": "https://simon-ritchie.github.io/apysc/en/true_and_false.html", "False_": "https://simon-ritchie.github.io/apysc/en/true_and_false.html", "ap.True_": "https://simon-ritchie.github.io/apysc/en/true_and_false.html", "ap.False_": "https://simon-ritchie.github.io/apysc/en/true_and_false.html", "Color": "https://simon-ritchie.github.io/apysc/en/color.html", "ap.Color": "https://simon-ritchie.github.io/apysc/en/color.html", "COLORLESS": "https://simon-ritchie.github.io/apysc/en/colorless.html", "ap.COLORLESS": "https://simon-ritchie.github.io/apysc/en/colorless.html", "Colors": "https://simon-ritchie.github.io/apysc/en/colors.html", "ap.Colors": "https://simon-ritchie.github.io/apysc/en/colors.html"};
    const CURRENT_PAGE_FILE_NAME = location.pathname.substring(
        location.pathname.lastIndexOf("/") + 1
    );
    for (let keyword in KEYWORD_LINK_MAPPINGS) {
        let link = KEYWORD_LINK_MAPPINGS[keyword];
        let link_file_name = link.substring(link.lastIndexOf("/") + 1);
        if (link_file_name === CURRENT_PAGE_FILE_NAME) {
            continue;
        }
        $("span:contains(" + keyword + ")").each(function() {
            let elemText = $(this).text();
            elemText = sanitise(elemText);
            if (elemText !== keyword) {
                return;
            }
            let className = $(this).attr("class");
            className = sanitise(className);
            if (className !== "pre") {
                return;
            }
            $(this).html("<a href='" + link + "'>" + $(this).html() + "</a>");
        });
    }
});
