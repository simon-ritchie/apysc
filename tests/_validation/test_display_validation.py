from random import randint

from retrying import retry

import apysc as ap
from apysc._display.display_object import DisplayObject
from apysc._testing import testing_helper
from apysc._testing.testing_helper import assert_raises
from apysc._validation import display_validation


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_stage() -> None:
    stage: ap.Stage = ap.Stage()
    display_validation.validate_stage(stage=stage)
    sprite: ap.Sprite = ap.Sprite()
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=display_validation.validate_stage,
        stage=sprite)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_display_object() -> None:
    stage: ap.Stage = ap.Stage()
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=display_validation.validate_display_object,
        match='\nTest error!',
        display_object=stage,
        additional_err_msg='Test error!')

    sprite: ap.Sprite = ap.Sprite()
    display_validation.validate_display_object(display_object=sprite)

    display_object: DisplayObject = DisplayObject(
        variable_name='test_display_object')
    display_validation.validate_display_object(display_object=display_object)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_graphics() -> None:
    ap.Stage()
    sprite: ap.Sprite = ap.Sprite()
    display_validation.validate_graphics(graphics=sprite.graphics)

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=display_validation.validate_graphics,
        graphics=sprite)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_sprite() -> None:
    stage: ap.Stage = ap.Stage()
    sprite: ap.Sprite = ap.Sprite()
    display_validation.validate_sprite(sprite=sprite)

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=display_validation.validate_sprite,
        sprite=stage)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_line_cap() -> None:
    display_validation.validate_line_cap(cap=ap.LineCaps.BUTT)
    display_validation.validate_line_cap(cap=ap.LineCaps.ROUND)
    display_validation.validate_line_cap(cap=ap.LineCaps.SQUARE)
    display_validation.validate_line_cap(
        cap=ap.String(ap.LineCaps.SQUARE.value))

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=display_validation.validate_line_cap,
        match='Not defined cap string is specified:',
        cap=ap.String('not_defined_cap'),)
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=display_validation.validate_line_cap,
        match='Specified cap style type is not LineCaps or String one: ',
        cap='square')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_line_joints() -> None:
    display_validation.validate_line_joints(joints=ap.LineJoints.MITER)
    display_validation.validate_line_joints(joints=ap.LineJoints.ROUND)
    display_validation.validate_line_joints(joints=ap.LineJoints.BEVEL)
    display_validation.validate_line_joints(
        joints=ap.String(ap.LineJoints.MITER.value))

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=display_validation.validate_line_joints,
        match=r'Not defined joints string is specified: ',
        joints=ap.String('not_defined_joints'))
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=display_validation.validate_line_joints,
        match=r'Specified joints type is not LineJoints or String one: ',
        joints='miter')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_multiple_line_settings_isnt_set() -> None:
    ap.Stage()
    sprite: ap.Sprite = ap.Sprite()
    display_validation.validate_multiple_line_settings_isnt_set(
        any_instance=sprite.graphics)

    sprite.graphics._line_dot_setting = ap.LineDotSetting(dot_size=5)
    display_validation.validate_multiple_line_settings_isnt_set(
        any_instance=sprite.graphics)

    sprite.graphics._line_dash_setting = ap.LineDashSetting(
        dash_size=10, space_size=5)
    assert_raises(
        expected_error_class=ValueError,
        callable_=display_validation.
        validate_multiple_line_settings_isnt_set,
        match=r"'LineDotSetting', 'LineDashSetting'",
        any_instance=sprite.graphics)
    delattr(sprite.graphics, '_line_dot_setting')

    sprite.graphics._line_round_dot_setting = ap.LineRoundDotSetting(
        round_size=5, space_size=5)
    assert_raises(
        expected_error_class=ValueError,
        callable_=display_validation.
        validate_multiple_line_settings_isnt_set,
        match=r"'LineDashSetting', 'LineRoundDotSetting'",
        any_instance=sprite.graphics)
    delattr(sprite.graphics, '_line_dash_setting')

    sprite.graphics._line_dash_dot_setting = ap.LineDashDotSetting(
        dot_size=5, dash_size=10, space_size=7)
    assert_raises(
        expected_error_class=ValueError,
        callable_=display_validation.
        validate_multiple_line_settings_isnt_set,
        match=r"'LineRoundDotSetting', 'LineDashDotSetting'",
        any_instance=sprite.graphics,)
    delattr(sprite.graphics, '_line_round_dot_setting')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_display_object_container() -> None:
    stage: ap.Stage = ap.Stage()
    display_validation.validate_display_object_container(
        container_object=stage)
    sprite: ap.Sprite = ap.Sprite()
    display_validation.validate_display_object_container(
        container_object=sprite)

    rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        x=0, y=0, width=50, height=50)
    assert_raises(
        expected_error_class=ValueError,
        callable_=display_validation.validate_display_object_container,
        match='\nTest error!',
        container_object=rectangle,
        additional_err_msg='Test error!')
