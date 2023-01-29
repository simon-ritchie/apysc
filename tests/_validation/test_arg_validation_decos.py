from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from apysc._validation import arg_validation_decos


class _TestClass1:
    @arg_validation_decos.not_empty_string(arg_position_index=1)
    def _test_method_1(self, *, a: str) -> None:
        ...

    @arg_validation_decos.not_empty_string(arg_position_index=1)
    def _test_method_2(self, a: str) -> None:
        ...


@arg_validation_decos.handler_args_num(arg_position_index=0)
def _test_func_2(*, handler: Callable) -> None:
    ...


@apply_test_settings()
def test_not_empty_string() -> None:
    @arg_validation_decos.not_empty_string(arg_position_index=0)
    def _test_func(a: str) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a="",
        match="An argument's string value must not be empty.",
    )
    assert_raises(expected_error_class=ValueError, callable_=_test_func, a=10)

    _test_func("Hello")
    _test_func(a="Hello")

    test_instance: _TestClass1 = _TestClass1()
    assert_raises(
        expected_error_class=ValueError,
        callable_=test_instance._test_method_1,
        match="An argument's string value must not be empty.",
        a="",
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=test_instance._test_method_2,
        match="An argument's string value must not be empty.",
        a="",
    )

    test_instance._test_method_1(a="Hello")
    test_instance._test_method_2(a="Hello")
    test_instance._test_method_2("Hello")


@apply_test_settings()
def test__extract_arg_value() -> None:
    def _test_func_1(*, a: int) -> None:
        ...

    value: Any = arg_validation_decos._extract_arg_value(
        args=[],
        kwargs={"a": "Test message 1"},
        arg_position_index=0,
        callable_=_test_func_1,
    )
    assert value == "Test message 1"

    value = arg_validation_decos._extract_arg_value(
        args=["Test message 2"], kwargs={}, arg_position_index=0, callable_=_test_func_1
    )
    assert value == "Test message 2"

    value = arg_validation_decos._extract_arg_value(
        args=[], kwargs={}, arg_position_index=0, callable_=_test_func_1
    )
    assert value is None

    def _test_func_2(*, a: str = "Hello!") -> None:
        ...

    value = arg_validation_decos._extract_arg_value(
        args=[], kwargs={}, arg_position_index=0, callable_=_test_func_2
    )
    assert value == "Hello!"


@apply_test_settings()
def test_handler_args_num() -> None:
    def _test_handler_1(e: ap.Event) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func_2,
        match="Target callable name: _test_func_2",
        handler=_test_handler_1,
    )

    def _test_handler_2(e: ap.Event, options: dict) -> None:
        ...

    _test_func_2(handler=_test_handler_2)


@apply_test_settings()
def test_handler_options_type() -> None:
    @arg_validation_decos.handler_options_type(arg_position_index=0)
    def _test_func(*, options: dict) -> None:
        ...

    assert_raises(expected_error_class=TypeError, callable_=_test_func, options=10)

    _test_func(options={"msg": "Hello!"})


@apply_test_settings()
def test__get_arg_name_by_index() -> None:
    def _test_func(*, a: int, b: str) -> None:
        ...

    arg_name: str = arg_validation_decos._get_arg_name_by_index(
        callable_=_test_func, arg_position_index=0
    )
    assert arg_name == "a"
    arg_name = arg_validation_decos._get_arg_name_by_index(
        callable_=_test_func, arg_position_index=1
    )
    assert arg_name == "b"

    def _test_func_2(a: int, b: str) -> None:
        ...

    arg_name = arg_validation_decos._get_arg_name_by_index(
        callable_=_test_func_2, arg_position_index=0
    )
    assert arg_name == "a"


@apply_test_settings()
def test__get_callable_and_arg_names_msg() -> None:
    def _test_func(a: int) -> None:
        ...

    callable_and_arg_names_msg: str = (
        arg_validation_decos._get_callable_and_arg_names_msg(
            callable_=_test_func, arg_position_index=0
        )
    )
    assert callable_and_arg_names_msg == (
        "Target callable name: _test_func" "\nTarget argument name: a"
    )


@apply_test_settings()
def test_is_integer() -> None:
    @arg_validation_decos.is_integer(arg_position_index=1)
    def _test_func(*, a: str, b: Union[int, ap.Int]) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError, callable_=_test_func, a="Hello!", b="World!"
    )

    _test_func(a="Hello!", b=10)
    _test_func(a="Hello!", b=ap.Int(10))


@apply_test_settings()
def test_num_is_gt_zero() -> None:
    @arg_validation_decos.num_is_gt_zero(arg_position_index=0)
    def _test_func(*, a: Union[int, ap.Int]) -> None:
        ...

    _test_func(a=1)
    _test_func(a=ap.Int(1))
    assert_raises(expected_error_class=ValueError, callable_=_test_func, a=0)


@apply_test_settings()
def test_is_easing() -> None:
    @arg_validation_decos.is_easing(arg_position_index=0)
    def _test_func(*, easing: ap.Easing) -> None:
        ...

    _test_func(easing=ap.Easing.EASE_IN_SINE)
    _test_func(easing=ap.Easing.EASE_OUT_QUAD)
    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        match=r"A specified easing argument\'s type is not the ap\.Easing\: ",
        easing=10,
    )


@apply_test_settings()
def test__get_default_val_by_arg_name() -> None:
    def _test_func(*, a: int, b: str = "Hello!") -> None:
        ...

    default_val: Any = arg_validation_decos._get_default_val_by_arg_name(
        callable_=_test_func, arg_name="a"
    )
    assert default_val is None

    default_val = arg_validation_decos._get_default_val_by_arg_name(
        callable_=_test_func, arg_name="b"
    )
    assert default_val == "Hello!"


@apply_test_settings()
def test_is_num() -> None:
    @arg_validation_decos.is_num(arg_position_index=0)
    def _test_func_1(*, a: Union[int, float, ap.Int, ap.Number]) -> None:
        ...

    _test_func_1(a=1.5)
    _test_func_1(a=1)
    _test_func_1(a=ap.Int(1))
    _test_func_1(a=ap.Number(1.5))

    assert_raises(expected_error_class=ValueError, callable_=_test_func_1, a="Hello!")


@apply_test_settings()
def test_is_hex_color_code_format() -> None:
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=0)
    def _test_func(*, a: str) -> None:
        ...

    _test_func(a="#a")
    _test_func(a="0af")
    _test_func(a="#0af")
    _test_func(a="#00aaff")

    assert_raises(expected_error_class=ValueError, callable_=_test_func, a="Hello!")


@apply_test_settings()
def test_num_is_gte_zero() -> None:
    @arg_validation_decos.num_is_gte_zero(arg_position_index=0)
    def _test_func(*, a: int) -> None:
        ...

    _test_func(a=0)
    _test_func(a=1)
    assert_raises(expected_error_class=ValueError, callable_=_test_func, a=-1)


@apply_test_settings()
def test_num_is_0_to_1_range() -> None:
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=0)
    def _test_func(*, a: float) -> None:
        ...

    assert_raises(expected_error_class=ValueError, callable_=_test_func, a=-0.1)
    assert_raises(expected_error_class=ValueError, callable_=_test_func, a=1.1)

    _test_func(a=0.0)
    _test_func(a=1.0)


@apply_test_settings()
def test_is_animations() -> None:
    @arg_validation_decos.is_animations(arg_position_index=0)
    def _test_func(*, a: List[ap.AnimationBase]) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        match="A specified animations list must be a list:",
        a=10,
    )
    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        match="A specified animations' list cannot contain " "non-animation instance:",
        a=[10, 20],
    )

    ap.Stage()
    sprite: ap.Sprite = ap.Sprite()
    _test_func(
        a=[
            sprite.animation_x(x=10),
        ]
    )


@apply_test_settings()
def test_is_apysc_boolean() -> None:
    @arg_validation_decos.is_apysc_boolean(arg_position_index=0)
    def _test_func(*, a: ap.Boolean) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        match="A specified argument value is not a `Boolean` type: ",
        a=True,
    )

    _test_func(a=ap.Boolean(True))


@apply_test_settings()
def test_is_vars_dict() -> None:
    @arg_validation_decos.is_vars_dict(arg_position_index=0)
    def _test_func_1(*, a: Optional[Dict[str, Any]]) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func_1,
        match="A specified variables argument value is not a " "dictionary or None",
        a=10,
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func_1,
        match="A specified variables argument dictionary's "
        "key cannot contain a non-str value:",
        a={10: 20},
    )
    _test_func_1(a=None)
    _test_func_1(a={"b": 10})

    @arg_validation_decos.is_vars_dict(arg_position_index=0, optional=False)
    def _test_func_2(*, a: Dict[str, Any]) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func_2,
        match="A specified variables argument value is not " "a dictionary:",
        a=None,
    )
    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func_2,
        match="A specified variables argument value is not " "a dictionary:",
        a=10,
    )
    _test_func_2(a={"b": 10})


@apply_test_settings()
def test_is_display_object() -> None:
    @arg_validation_decos.is_display_object(arg_position_index=0)
    def _test_func(*, a: ap.DisplayObject) -> None:
        ...

    assert_raises(expected_error_class=ValueError, callable_=_test_func, a=100)

    ap.Stage()
    sprite: ap.Sprite = ap.Sprite()
    _test_func(a=sprite)


@apply_test_settings()
def test_is_display_object_container() -> None:
    @arg_validation_decos.is_display_object_container(
        arg_position_index=0, optional=False
    )
    def _test_func_1(*, a: Union[ap.Sprite, ap.Stage]) -> None:
        ...

    stage: ap.Stage = ap.Stage()
    _test_func_1(a=stage)
    sprite: ap.Sprite = ap.Sprite()
    _test_func_1(a=sprite)
    assert_raises(expected_error_class=ValueError, callable_=_test_func_1, a=100)
    assert_raises(expected_error_class=ValueError, callable_=_test_func_1, a=None)

    @arg_validation_decos.is_display_object_container(
        arg_position_index=0, optional=True
    )
    def _test_func_2(*, a: Optional[ap.Sprite]) -> None:
        ...

    assert_raises(expected_error_class=ValueError, callable_=_test_func_2, a=100)
    _test_func_2(a=sprite)
    _test_func_2(a=None)


@apply_test_settings()
def test_is_string() -> None:
    @arg_validation_decos.is_string(arg_position_index=0)
    def _test_func(*, a: Union[str, ap.String]) -> None:
        ...

    _test_func(a="Hello!")
    _test_func(a=ap.String("Hello!"))

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a=100,
    )


@apply_test_settings()
def test_is_apysc_num() -> None:
    @arg_validation_decos.is_apysc_num(arg_position_index=0)
    def _test_func(*, a: Union[ap.Int, ap.Number]) -> None:
        ...

    _test_func(a=ap.Int(10))
    _test_func(a=ap.Number(10))

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        a=10,
    )


@apply_test_settings()
def test_is_point_2ds() -> None:
    @arg_validation_decos.is_point_2ds(arg_position_index=0)
    def _test_func(*, a: Union[List[ap.Point2D], ap.Array[ap.Point2D]]) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        a=100,
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a=[100, ap.Point2D(x=10, y=20)],
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a=ap.Array([100, ap.Point2D(x=10, y=20)]),
    )

    _test_func(a=[ap.Point2D(x=10, y=20), ap.Point2D(x=30, y=40)])
    _test_func(a=ap.Array([ap.Point2D(x=10, y=20), ap.Point2D(x=30, y=40)]))


@apply_test_settings()
def test_is_valid_path_data_list() -> None:
    @arg_validation_decos.is_valid_path_data_list(arg_position_index=0)
    def _test_func(*, a: List[ap.PathDataBase]) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        a=100,
    )
    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        a=[100],
    )

    _test_func(a=[ap.PathMoveTo(x=50, y=50), ap.PathLineTo(x=100, y=100)])


@apply_test_settings()
def test_is_line_cap() -> None:
    @arg_validation_decos.is_line_cap(arg_position_index=0, optional=True)
    def _test_func_1(*, a: Optional[Union[ap.String, ap.LineCaps]]) -> None:
        ...

    assert_raises(expected_error_class=ValueError, callable_=_test_func_1, a=100)
    assert_raises(
        expected_error_class=ValueError, callable_=_test_func_1, a=ap.String("Hello")
    )
    _test_func_1(a=ap.LineCaps.ROUND)
    _test_func_1(a=None)
    _test_func_1(a=ap.String(ap.LineCaps.BUTT.value))

    @arg_validation_decos.is_line_cap(arg_position_index=0, optional=False)
    def _test_func_2(*, a: Optional[Union[ap.String, ap.LineCaps]]) -> None:
        ...

    assert_raises(expected_error_class=ValueError, callable_=_test_func_2, a=None)
    _test_func_2(a=ap.LineCaps.ROUND)


@apply_test_settings()
def test_multiple_line_settings_are_not_set() -> None:
    @arg_validation_decos.multiple_line_settings_are_not_set(arg_position_index=0)
    def _test_func_1(*, rectangle: ap.Rectangle) -> None:
        rectangle.line_dot_setting = ap.LineDotSetting(dot_size=10)

    @arg_validation_decos.multiple_line_settings_are_not_set(arg_position_index=0)
    def _test_func_2(*, rectangle: ap.Rectangle) -> None:
        rectangle.line_dot_setting = ap.LineDotSetting(dot_size=10)
        rectangle.line_dash_setting = ap.LineDashSetting(dash_size=10, space_size=5)

    ap.Stage()
    sprite: ap.Sprite = ap.Sprite()
    rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
    _test_func_1(rectangle=rectangle)

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func_2,
        rectangle=rectangle,
    )


@apply_test_settings()
def test_is_line_dash_dot_setting() -> None:
    @arg_validation_decos.is_line_dash_dot_setting(arg_position_index=0)
    def _test_func(*, a: Optional[ap.LineDashDotSetting]) -> None:
        ...

    assert_raises(expected_error_class=TypeError, callable_=_test_func, a=100)
    _test_func(a=None)
    _test_func(a=ap.LineDashDotSetting(dot_size=5, dash_size=10, space_size=5))


@apply_test_settings()
def test_is_line_dash_setting() -> None:
    @arg_validation_decos.is_line_dash_setting(arg_position_index=0)
    def _test_func(*, a: Optional[ap.LineDashSetting]) -> None:
        ...

    assert_raises(expected_error_class=TypeError, callable_=_test_func, a=100)
    _test_func(a=None)
    _test_func(a=ap.LineDashSetting(dash_size=10, space_size=5))


@apply_test_settings()
def test_is_line_dot_setting() -> None:
    @arg_validation_decos.is_line_dot_setting(arg_position_index=0)
    def _test_func(*, a: Optional[ap.LineDotSetting]) -> None:
        ...

    assert_raises(expected_error_class=TypeError, callable_=_test_func, a=100)
    _test_func(a=None)
    _test_func(a=ap.LineDotSetting(dot_size=5))


@apply_test_settings()
def test_is_line_joints() -> None:
    @arg_validation_decos.is_line_joints(arg_position_index=0, optional=True)
    def _test_func_1(*, a: Optional[Union[ap.LineJoints, ap.String]]) -> None:
        ...

    assert_raises(expected_error_class=ValueError, callable_=_test_func_1, a=100)
    _test_func_1(a=ap.LineJoints.BEVEL)
    _test_func_1(a=None)
    _test_func_1(a=ap.String(ap.LineJoints.BEVEL.value))

    @arg_validation_decos.is_line_joints(arg_position_index=0, optional=False)
    def _test_func_2(*, a: Optional[Union[ap.LineJoints, ap.String]]) -> None:
        ...

    assert_raises(expected_error_class=ValueError, callable_=_test_func_2, a=None)
    _test_func_2(a=ap.LineJoints.BEVEL)


@apply_test_settings()
def test_is_line_round_dot_setting() -> None:
    @arg_validation_decos.is_line_round_dot_setting(arg_position_index=0)
    def _test_func(*, a: Optional[ap.LineRoundDotSetting]) -> None:
        ...

    assert_raises(expected_error_class=TypeError, callable_=_test_func, a=100)
    _test_func(a=None)
    _test_func(a=ap.LineRoundDotSetting(round_size=10, space_size=5))


@apply_test_settings()
def test_is_apysc_integer() -> None:
    @arg_validation_decos.is_apysc_integer(arg_position_index=0)
    def _test_func(*, a: ap.Int) -> None:
        ...

    assert_raises(expected_error_class=TypeError, callable_=_test_func, a=100)
    _test_func(a=ap.Int(100))


@apply_test_settings()
def test_is_point_2d() -> None:
    @arg_validation_decos.is_point_2d(arg_position_index=0)
    def _test_func(*, a: ap.Point2D) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a=100,
    )
    _test_func(a=ap.Point2D(x=50, y=100))


@apply_test_settings()
def test_is_builtin_string() -> None:
    @arg_validation_decos.is_builtin_string(arg_position_index=0, optional=False)
    def _test_func_1(*, a: str) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func_1,
        a=None,
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func_1,
        a=ap.String("Hello!"),
    )
    _test_func_1(a="Hello!")

    @arg_validation_decos.is_builtin_string(arg_position_index=0, optional=True)
    def _test_func_2(*, a: Optional[str]) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func_2,
        a=ap.String("Hello!"),
    )
    _test_func_2(a=None)
    _test_func_2(a="Hello!")


@apply_test_settings()
def test_is_builtin_integer() -> None:
    @arg_validation_decos.is_builtin_integer(arg_position_index=0)
    def _test_func(*, a: int) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a=ap.Int(100),
    )
    _test_func(a=100)


@apply_test_settings()
def test_is_variable_name_interface_type() -> None:
    @arg_validation_decos.is_variable_name_interface_type(arg_position_index=0)
    def _test_func(*, a: ap.Int) -> None:
        ...

    assert_raises(expected_error_class=TypeError, callable_=_test_func, a=100)
    _test_func(a=ap.Int(100))


@apply_test_settings()
def test_is_event() -> None:
    @arg_validation_decos.is_event(arg_position_index=0)
    def _test_func(*, a: ap.Event) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a=100,
    )
    stage: ap.Stage = ap.Stage()
    e: ap.Event = ap.Event(this=stage)
    _test_func(a=e)


@apply_test_settings()
def test_is_boolean() -> None:
    @arg_validation_decos.is_boolean(arg_position_index=0)
    def _test_func(*, a: Union[bool, ap.Boolean]) -> None:
        ...

    assert_raises(expected_error_class=ValueError, callable_=_test_func, a=100)
    _test_func(a=True)
    _test_func(a=ap.Boolean(True))


@apply_test_settings()
def test_is_builtin_boolean() -> None:
    @arg_validation_decos.is_builtin_boolean(arg_position_index=0)
    def _test_func(*, a: bool) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a=ap.Boolean(True),
    )
    _test_func(a=True)


@apply_test_settings()
def test_is_acceptable_array_value() -> None:
    @arg_validation_decos.is_acceptable_array_value(arg_position_index=0)
    def _test_func(*, a: Union[list, tuple, range, ap.Array]) -> None:
        ...

    assert_raises(expected_error_class=TypeError, callable_=_test_func, a="Hello")
    _test_func(a=[10, 20])
    _test_func(a=(10, 20))
    _test_func(a=range(10))
    _test_func(a=ap.Array([10, 20]))


@apply_test_settings()
def test_is_acceptable_dictionary_value() -> None:
    @arg_validation_decos.is_acceptable_dictionary_value(arg_position_index=0)
    def _test_func(*, a: Union[dict, ap.Dictionary]) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        a="Hello",
    )
    _test_func(a={"b": 20})
    _test_func(a=ap.Dictionary({"b": 20}))


@apply_test_settings()
def test_is_acceptable_boolean_value() -> None:
    @arg_validation_decos.is_acceptable_boolean_value(arg_position_index=0)
    def _test_func(*, a: Union[bool, int, ap.Int, ap.Boolean]) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a=2,
    )
    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        a="Hello",
    )
    _test_func(a=0)
    _test_func(a=1)
    _test_func(a=ap.Int(0))
    _test_func(a=ap.Int(1))
    _test_func(a=True)
    _test_func(a=False)
    _test_func(a=ap.Boolean(True))
    _test_func(a=ap.Boolean(False))


@apply_test_settings()
def test_is_fps() -> None:
    @arg_validation_decos.is_fps(arg_position_index=0)
    def _test_func(*, fps: ap.FPS) -> int:
        return 10

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        fps=10,
    )

    result: int = _test_func(fps=ap.FPS.FPS_60)
    assert result == 10


@apply_test_settings()
def test_is_builtin_dict() -> None:
    @arg_validation_decos.is_builtin_dict(arg_position_index=0)
    def _test_func(*, dict_val: Dict[Any, Any]) -> int:
        return 20

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        dict_val=10,
    )

    result: int = _test_func(dict_val={"value": 30})
    assert result == 20


@apply_test_settings()
def test_is_four_digit_year() -> None:
    @arg_validation_decos.is_four_digit_year(arg_position_index=0)
    def _test_func(*, year: Union[int, ap.Int]) -> int:
        return 30

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        year=22,
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        year=ap.Int(22),
    )

    result: int = _test_func(year=2022)
    assert result == 30
    result = _test_func(year=ap.Int(2022))
    assert result == 30
    result = _test_func(year=ap.Int(0))
    assert result == 30


@apply_test_settings()
def test_is_month_int() -> None:
    @arg_validation_decos.is_month_int(arg_position_index=0)
    def _test_func(*, month: Union[int, ap.Int]) -> int:
        return 40

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        month=0,
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        month=13,
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        month=ap.Int(-1),
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        month=ap.Int(13),
    )

    result: int = _test_func(month=1)
    assert result == 40
    result = _test_func(month=12)
    assert result == 40
    result = _test_func(month=ap.Int(0))
    assert result == 40
    result = _test_func(month=ap.Int(1))
    assert result == 40
    result = _test_func(month=ap.Int(12))
    assert result == 40


@apply_test_settings()
def test_is_day_int() -> None:
    @arg_validation_decos.is_day_int(arg_position_index=0)
    def _test_func(*, day: Union[int, ap.Int]) -> int:
        return 50

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        day=0,
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        day=32,
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        day=ap.Int(-1),
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        day=ap.Int(32),
    )

    result: int = _test_func(day=1)
    assert result == 50
    result = _test_func(day=31)
    assert result == 50
    result = _test_func(day=31)
    assert result == 50
    result = _test_func(day=ap.Int(0))
    assert result == 50
    result = _test_func(day=ap.Int(1))
    assert result == 50
    result = _test_func(day=ap.Int(31))
    assert result == 50


@apply_test_settings()
def test_is_hour_int() -> None:
    @arg_validation_decos.is_hour_int(arg_position_index=0)
    def _test_func(*, hour: Union[int, ap.Int]) -> int:
        return 60

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        hour=-1,
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        hour=24,
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        hour=ap.Int(-1),
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        hour=ap.Int(24),
    )

    result: int = _test_func(hour=0)
    assert result == 60
    result = _test_func(hour=23)
    assert result == 60


@apply_test_settings()
def test_is_minute_int() -> None:
    @arg_validation_decos.is_minute_int(arg_position_index=0)
    def _test_func(*, minute: Union[int, ap.Int]) -> int:
        return 80

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        minute=-1,
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        minute=60,
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        minute=ap.Int(-1),
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        minute=ap.Int(60),
    )

    result: int = _test_func(minute=0)
    assert result == 80
    result = _test_func(minute=59)
    assert result == 80
    result = _test_func(minute=ap.Int(0))
    assert result == 80
    result = _test_func(minute=ap.Int(59))
    assert result == 80


@apply_test_settings()
def test_is_second_int() -> None:
    @arg_validation_decos.is_second_int(arg_position_index=0)
    def _test_func(*, second: Union[int, ap.Int]) -> int:
        return 100

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        second=-1,
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        second=60,
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        second=ap.Int(-1),
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        second=ap.Int(60),
    )

    result: int = _test_func(second=0)
    assert result == 100
    result = _test_func(second=59)
    assert result == 100
    result = _test_func(second=ap.Int(0))
    assert result == 100
    result = _test_func(second=ap.Int(59))
    assert result == 100


@apply_test_settings()
def test_is_millisecond_int() -> None:
    @arg_validation_decos.is_millisecond_int(arg_position_index=0)
    def _test_func(*, millisecond: Union[int, ap.Int]) -> int:
        return 120

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        millisecond=-1,
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        millisecond=1000,
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        millisecond=ap.Int(-1),
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        millisecond=ap.Int(1000),
    )

    result: int = _test_func(millisecond=0)
    assert result == 120
    result = _test_func(millisecond=999)
    assert result == 120
    result = _test_func(millisecond=ap.Int(0))
    assert result == 120
    result = _test_func(millisecond=ap.Int(999))
    assert result == 120


@apply_test_settings()
def test_is_apysc_datetime() -> None:
    @arg_validation_decos.is_apysc_datetime(arg_position_index=0)
    def _test_func(*, datetime_: ap.DateTime) -> int:
        return 130

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        datetime_=200,
    )

    result: int = _test_func(datetime_=ap.DateTime(year=2022, month=12, day=1))
    assert result == 130


@apply_test_settings()
def test_is_nums_array() -> None:
    @arg_validation_decos.is_nums_array(arg_position_index=0)
    def _test_func(*, arr: ap.Array) -> int:
        return 140

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        match="A specified argument is not an `Array` instance: ",
        arr=100,
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        match="A specified array contains a non-number value: ",
        arr=ap.Array([10, "test", 20.5, ap.Int(25)]),
    )

    result: int = _test_func(
        arr=ap.Array([10, 20.5, ap.Int(25), ap.Number(10.5)]),
    )
    assert result == 140
