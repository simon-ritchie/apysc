from random import randint

from retrying import retry

from apysc import LineCaps
from apysc import LineDashDotSetting
from apysc import LineDashSetting
from apysc import LineDotSetting
from apysc import LineJoints
from apysc import LineRoundDotSetting
from apysc import Sprite
from apysc import Stage
from apysc import String
from apysc._display.display_object import DisplayObject
from apysc.validation import display_validation
from tests import testing_helper
from tests.testing_helper import assert_raises


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_stage() -> None:
    stage: Stage = Stage()
    display_validation.validate_stage(stage=stage)
    sprite: Sprite = Sprite(stage=stage)
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=display_validation.validate_stage,
        kwargs={'stage': sprite})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_display_object() -> None:
    stage: Stage = Stage()
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=display_validation.validate_display_object,
        kwargs={'display_object': stage})

    sprite: Sprite = Sprite(stage=stage)
    display_validation.validate_display_object(display_object=sprite)

    display_object: DisplayObject = DisplayObject(
        stage=stage, variable_name='test_display_object')
    display_validation.validate_display_object(display_object=display_object)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_graphics() -> None:
    stage: Stage = Stage()
    sprite: Sprite = Sprite(stage=stage)
    display_validation.validate_graphics(graphics=sprite.graphics)

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=display_validation.validate_graphics,
        kwargs={'graphics': sprite})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_sprite() -> None:
    stage: Stage = Stage()
    sprite: Sprite = Sprite(stage=stage)
    display_validation.validate_sprite(sprite=sprite)

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=display_validation.validate_sprite,
        kwargs={'sprite': stage})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_line_cap() -> None:
    display_validation.validate_line_cap(cap=LineCaps.BUTT)
    display_validation.validate_line_cap(cap=LineCaps.ROUND)
    display_validation.validate_line_cap(cap=LineCaps.SQUARE)
    display_validation.validate_line_cap(
        cap=String(LineCaps.SQUARE.value))

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=display_validation.validate_line_cap,
        kwargs={'cap': String('not_defined_cap')},
        match='Not defined cap string is specified:')
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=display_validation.validate_line_cap,
        kwargs={'cap': 'square'},
        match='Specified cap style type is not LineCaps or String one: ')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_line_joints() -> None:
    display_validation.validate_line_joints(joints=LineJoints.MITER)
    display_validation.validate_line_joints(joints=LineJoints.ROUND)
    display_validation.validate_line_joints(joints=LineJoints.BEVEL)
    display_validation.validate_line_joints(
        joints=String(LineJoints.MITER.value))

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=display_validation.validate_line_joints,
        kwargs={'joints': String('not_defined_joints')},
        match=r'Not defined joints string is specified: ')
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=display_validation.validate_line_joints,
        kwargs={'joints': 'miter'},
        match=r'Specified joints type is not LineJoints or String one: ')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_multiple_line_settings_isnt_set() -> None:
    stage: Stage = Stage()
    sprite: Sprite = Sprite(stage=stage)
    display_validation.validate_multiple_line_settings_isnt_set(
        any_instance=sprite.graphics)

    sprite.graphics._line_dot_setting = LineDotSetting(dot_size=5)
    display_validation.validate_multiple_line_settings_isnt_set(
        any_instance=sprite.graphics)

    sprite.graphics._line_dash_setting = LineDashSetting(
        dash_size=10, space_size=5)
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=display_validation.
        validate_multiple_line_settings_isnt_set,
        kwargs={'any_instance': sprite.graphics},
        match=r"'LineDotSetting', 'LineDashSetting'")
    delattr(sprite.graphics, '_line_dot_setting')

    sprite.graphics._line_round_dot_setting = LineRoundDotSetting(
        round_size=5, space_size=5)
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=display_validation.
        validate_multiple_line_settings_isnt_set,
        kwargs={'any_instance': sprite.graphics},
        match=r"'LineDashSetting', 'LineRoundDotSetting'")
    delattr(sprite.graphics, '_line_dash_setting')

    sprite.graphics._line_dash_dot_setting = LineDashDotSetting(
        dot_size=5, dash_size=10, space_size=7)
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=display_validation.
        validate_multiple_line_settings_isnt_set,
        kwargs={'any_instance': sprite.graphics},
        match=r"'LineRoundDotSetting', 'LineDashDotSetting'")
    delattr(sprite.graphics, '_line_round_dot_setting')
