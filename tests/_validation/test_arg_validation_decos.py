from random import randint
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from retrying import retry

import apysc as ap
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


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_not_empty_string() -> None:

    @arg_validation_decos.not_empty_string(arg_position_index=0)
    def _test_func(a: str) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a='',
        match='An argument\'s string value must not be empty.')
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a=10)

    _test_func('Hello')
    _test_func(a='Hello')

    test_instance: _TestClass1 = _TestClass1()
    assert_raises(
        expected_error_class=ValueError,
        callable_=test_instance._test_method_1,
        match='An argument\'s string value must not be empty.',
        a='')
    assert_raises(
        expected_error_class=ValueError,
        callable_=test_instance._test_method_2,
        match='An argument\'s string value must not be empty.',
        a='')

    test_instance._test_method_1(a='Hello')
    test_instance._test_method_2(a='Hello')
    test_instance._test_method_2('Hello')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__extract_arg_value() -> None:

    def _test_func_1(*, a: int) -> None:
        ...

    value: Any = arg_validation_decos._extract_arg_value(
        args=[],
        kwargs={'a': 'Test message 1'},
        arg_position_index=0,
        callable_=_test_func_1)
    assert value == 'Test message 1'

    value = arg_validation_decos._extract_arg_value(
        args=['Test message 2'],
        kwargs={},
        arg_position_index=0,
        callable_=_test_func_1)
    assert value == 'Test message 2'

    value = arg_validation_decos._extract_arg_value(
        args=[],
        kwargs={},
        arg_position_index=0,
        callable_=_test_func_1)
    assert value is None

    def _test_func_2(*, a: str = 'Hello!') -> None:
        ...

    value = arg_validation_decos._extract_arg_value(
        args=[],
        kwargs={},
        arg_position_index=0,
        callable_=_test_func_2)
    assert value == 'Hello!'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_handler_args_num() -> None:

    def _test_handler_1(e: ap.Event) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func_2,
        match='Target callable name: _test_func_2',
        handler=_test_handler_1,
    )

    def _test_handler_2(e: ap.Event, options: dict) -> None:
        ...

    _test_func_2(handler=_test_handler_2)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_handler_options_type() -> None:

    @arg_validation_decos.handler_options_type(arg_position_index=0)
    def _test_func(*, options: dict) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        options=10)

    _test_func(options={'msg': 'Hello!'})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_arg_name_by_index() -> None:

    def _test_func(*, a: int, b: str) -> None:
        ...

    arg_name: str = arg_validation_decos._get_arg_name_by_index(
        callable_=_test_func, arg_position_index=0)
    assert arg_name == 'a'
    arg_name = arg_validation_decos._get_arg_name_by_index(
        callable_=_test_func, arg_position_index=1)
    assert arg_name == 'b'

    def _test_func_2(a: int, b: str) -> None:
        ...

    arg_name = arg_validation_decos._get_arg_name_by_index(
        callable_=_test_func_2, arg_position_index=0)
    assert arg_name == 'a'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_callable_and_arg_names_msg() -> None:

    def _test_func(a: int) -> None:
        ...

    callable_and_arg_names_msg: str = arg_validation_decos.\
        _get_callable_and_arg_names_msg(
            callable_=_test_func, arg_position_index=0)
    assert callable_and_arg_names_msg == (
        'Target callable name: _test_func'
        '\nTarget argument name: a'
    )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_integer() -> None:

    @arg_validation_decos.is_integer(arg_position_index=1)
    def _test_func(*, a: str, b: Union[int, ap.Int]) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a='Hello!',
        b='World!')

    _test_func(a='Hello!', b=10)
    _test_func(a='Hello!', b=ap.Int(10))


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_num_is_gt_zero() -> None:

    @arg_validation_decos.num_is_gt_zero(arg_position_index=0)
    def _test_func(*, a: Union[int, ap.Int]) -> None:
        ...

    _test_func(a=1)
    _test_func(a=ap.Int(1))
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a=0)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
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
        easing=10)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_default_val_by_arg_name() -> None:

    def _test_func(*, a: int, b: str = 'Hello!') -> None:
        ...

    default_val: Any = arg_validation_decos._get_default_val_by_arg_name(
        callable_=_test_func, arg_name='a')
    assert default_val is None

    default_val = arg_validation_decos._get_default_val_by_arg_name(
        callable_=_test_func, arg_name='b')
    assert default_val == 'Hello!'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_num() -> None:

    @arg_validation_decos.is_num(arg_position_index=0)
    def _test_func_1(
            *, a: Union[int, float, ap.Int, ap.Number]) -> None:
        ...

    _test_func_1(a=1.5)
    _test_func_1(a=1)
    _test_func_1(a=ap.Int(1))
    _test_func_1(a=ap.Number(1.5))

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func_1,
        a='Hello!')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_hex_color_code_format() -> None:

    @arg_validation_decos.is_hex_color_code_format(arg_position_index=0)
    def _test_func(*, a: str) -> None:
        ...

    _test_func(a='#a')
    _test_func(a='0af')
    _test_func(a='#0af')
    _test_func(a='#00aaff')

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a='Hello!')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_num_is_gte_zero() -> None:

    @arg_validation_decos.num_is_gte_zero(arg_position_index=0)
    def _test_func(*, a: int) -> None:
        ...

    _test_func(a=0)
    _test_func(a=1)
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a=-1)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_num_is_0_to_1_range() -> None:

    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=0)
    def _test_func(*, a: float) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a=-0.1)
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a=1.1)

    _test_func(a=0.0)
    _test_func(a=1.0)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_animations() -> None:

    @arg_validation_decos.is_animations(arg_position_index=0)
    def _test_func(*, a: List[ap.AnimationBase]) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        match='A specified animations list must be a list:',
        a=10)
    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        match='A specified animations\' list cannot contain '
        'non-animation instance:',
        a=[10, 20])

    ap.Stage()
    sprite: ap.Sprite = ap.Sprite()
    _test_func(
        a=[
            sprite.animation_x(x=10),
        ])


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_apysc_boolean() -> None:

    @arg_validation_decos.is_apysc_boolean(arg_position_index=0)
    def _test_func(*, a: ap.Boolean) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        match='A specified argument value is not a `Boolean` type: ',
        a=True)

    _test_func(a=ap.Boolean(True))


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_vars_dict() -> None:

    @arg_validation_decos.is_vars_dict(arg_position_index=0)
    def _test_func_1(*, a: Optional[Dict[str, Any]]) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError, callable_=_test_func_1,
        match='A specified variables argument value is not a '
        'dictionary or None',
        a=10)
    assert_raises(
        expected_error_class=ValueError, callable_=_test_func_1,
        match='A specified variables argument dictionary\'s '
        'key cannot contain a non-str value:',
        a={10: 20})
    _test_func_1(a=None)
    _test_func_1(a={'b': 10})

    @arg_validation_decos.is_vars_dict(arg_position_index=0, optional=False)
    def _test_func_2(*, a: Dict[str, Any]) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError, callable_=_test_func_2,
        match='A specified variables argument value is not '
        'a dictionary:',
        a=None)
    assert_raises(
        expected_error_class=TypeError, callable_=_test_func_2,
        match='A specified variables argument value is not '
        'a dictionary:',
        a=10)
    _test_func_2(a={'b': 10})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_display_object() -> None:

    @arg_validation_decos.is_display_object(arg_position_index=0)
    def _test_func(*, a: ap.DisplayObject) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a=100)

    ap.Stage()
    sprite: ap.Sprite = ap.Sprite()
    _test_func(a=sprite)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_display_object_container() -> None:

    @arg_validation_decos.is_display_object_container(arg_position_index=0)
    def _test_func(*, a: Union[ap.Sprite, ap.Stage]) -> None:
        ...

    stage: ap.Stage = ap.Stage()
    _test_func(a=stage)
    sprite: ap.Sprite = ap.Sprite()
    _test_func(a=sprite)

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a=100)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_string() -> None:

    @arg_validation_decos.is_string(arg_position_index=0)
    def _test_func(*, a: Union[str, ap.String]) -> None:
        ...

    _test_func(a='Hello!')
    _test_func(a=ap.String('Hello!'))

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a=100,
    )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
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


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_points() -> None:

    @arg_validation_decos.is_points(arg_position_index=0)
    def _test_func(
            *, a: Union[List[ap.Point2D], ap.Array[ap.Point2D]]) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        a=100,
    )
    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        a=[100, ap.Point2D(x=10, y=20)],
    )
    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        a=ap.Array([100, ap.Point2D(x=10, y=20)]),
    )

    _test_func(a=[ap.Point2D(x=10, y=20), ap.Point2D(x=30, y=40)])
    _test_func(
        a=ap.Array([ap.Point2D(x=10, y=20), ap.Point2D(x=30, y=40)]))


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_path_data_list() -> None:

    @arg_validation_decos.is_path_data_list(arg_position_index=0)
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

    _test_func(
        a=[ap.PathMoveTo(x=50, y=50), ap.PathLineTo(x=100, y=100)])


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_line_cap() -> None:

    @arg_validation_decos.is_line_cap(arg_position_index=0)
    def _test_func(*, a: Union[ap.String, ap.LineCaps]) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a=100)
    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func,
        a=ap.String('Hello'))

    _test_func(a=ap.LineCaps.ROUND)
    _test_func(a=ap.String(ap.LineCaps.BUTT.value))


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_multiple_line_settings_are_not_set() -> None:

    @arg_validation_decos.multiple_line_settings_are_not_set(
        arg_position_index=0)
    def _test_func_1(*, rectangle: ap.Rectangle) -> None:
        rectangle.line_dot_setting = ap.LineDotSetting(dot_size=10)

    @arg_validation_decos.multiple_line_settings_are_not_set(
        arg_position_index=0)
    def _test_func_2(*, rectangle: ap.Rectangle) -> None:
        rectangle.line_dot_setting = ap.LineDotSetting(dot_size=10)
        rectangle.line_dash_setting = ap.LineDashSetting(
            dash_size=10, space_size=5)

    ap.Stage()
    sprite: ap.Sprite = ap.Sprite()
    rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    _test_func_1(rectangle=rectangle)

    assert_raises(
        expected_error_class=ValueError,
        callable_=_test_func_2,
        rectangle=rectangle,
    )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_line_dash_dot_setting() -> None:

    @arg_validation_decos.is_line_dash_dot_setting(
        arg_position_index=0, optional=True)
    def _test_func_1(*, a: Optional[ap.LineDashDotSetting]) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func_1,
        a=100)
    _test_func_1(a=None)
    _test_func_1(
        a=ap.LineDashDotSetting(dot_size=5, dash_size=10, space_size=5))

    @arg_validation_decos.is_line_dash_dot_setting(
        arg_position_index=0, optional=False)
    def _test_func_2(*, a: ap.LineDashDotSetting) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func_2,
        a=None)
    _test_func_2(
        a=ap.LineDashDotSetting(dot_size=5, dash_size=10, space_size=5))


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_line_dash_setting() -> None:

    @arg_validation_decos.is_line_dash_setting(
        arg_position_index=0, optional=True)
    def _test_func_1(*, a: Optional[ap.LineDashSetting]) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func_1,
        a=100)
    _test_func_1(a=None)
    _test_func_1(a=ap.LineDashSetting(dash_size=10, space_size=5))

    @arg_validation_decos.is_line_dash_setting(
        arg_position_index=0, optional=False)
    def _test_func_2(*, a: Optional[ap.LineDashSetting]) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func_2,
        a=None)
    _test_func_2(a=ap.LineDashSetting(dash_size=10, space_size=5))


# @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_line_dot_setting() -> None:

    @arg_validation_decos.is_line_dot_setting(arg_position_index=0)
    def _test_func(*, a: Optional[ap.LineDotSetting]) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError,
        callable_=_test_func,
        a=100)
    _test_func(a=None)
    _test_func(a=ap.LineDotSetting(dot_size=5))
