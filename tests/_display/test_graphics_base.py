import apysc as ap
from apysc._display.fill_alpha_mixin import FillAlphaMixIn
from apysc._display.fill_color_mixin import FillColorMixIn
from apysc._display.flip_x_mixin import FlipXMixIn
from apysc._display.flip_y_mixin import FlipYMixIn
from apysc._display.get_bounds_mixin import GetBoundsMixIn
from apysc._display.graphics_base import GraphicsBase
from apysc._display.line_alpha_mixin import LineAlphaMixIn
from apysc._display.line_color_mixin import LineColorMixIn
from apysc._display.line_dash_dot_setting_mixin import LineDashDotSettingMixIn
from apysc._display.line_dash_setting_mixin import LineDashSettingMixIn
from apysc._display.line_dot_setting_mixin import LineDotSettingMixIn
from apysc._display.line_joints_mixin import LineJointsMixIn
from apysc._display.line_round_dot_setting_mixin import LineRoundDotSettingMixIn
from apysc._display.rotation_around_center_mixin import RotationAroundCenterMixIn
from apysc._display.rotation_around_point_mixin import RotationAroundPointMixIn
from apysc._display.scale_x_from_center_mixin import ScaleXFromCenterMixIn
from apysc._display.scale_x_from_point_mixin import ScaleXFromPointMixIn
from apysc._display.scale_y_from_center_mixin import ScaleYFromCenterMixIn
from apysc._display.scale_y_from_point_mixin import ScaleYFromPointMixIn
from apysc._display.skew_x_mixin import SkewXMixIn
from apysc._display.skew_y_mixin import SkewYMixIn
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings
from apysc._display.css_mixin import CssMixIn
from apysc._display.set_overflow_visible_setting_mixin import (
    SetOverflowVisibleSettingMixIn
)


class _TestGraphic(
    XMixIn,
    YMixIn,
    SetOverflowVisibleSettingMixIn,
    CssMixIn,
    GraphicsBase,
    RotationAroundCenterMixIn,
    RotationAroundPointMixIn,
    ScaleXFromCenterMixIn,
    ScaleYFromCenterMixIn,
    ScaleXFromPointMixIn,
    ScaleYFromPointMixIn,
    FlipXMixIn,
    FlipYMixIn,
    SkewXMixIn,
    SkewYMixIn,
    FillColorMixIn,
    FillAlphaMixIn,
    LineColorMixIn,
    LineAlphaMixIn,
    LineJointsMixIn,
    LineDotSettingMixIn,
    LineDashSettingMixIn,
    LineRoundDotSettingMixIn,
    LineDashDotSettingMixIn,
    GetBoundsMixIn,
):
    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            A string representation of this instance.
        """
        return f"_TestGraphic({self.variable_name})"

    @property
    def x(self) -> ap.Number:
        """
        Get an x-coordinate.

        Returns
        -------
        x : Number
            X-coordinate.
        """
        return self._x

    @x.setter
    def x(self, value: ap.Number) -> None:
        """
        Update x-coordinate.

        Parameters
        ----------
        value : Number
            X-coordinate value.
        """
        self._x = value

    @property
    def y(self) -> ap.Number:
        """
        Get a y-coordinate.

        Returns
        -------
        y : Number
            Y-coordinate.
        """
        return self._y

    @y.setter
    def y(self, value: ap.Number) -> None:
        """
        Update y-coordinate.

        Parameters
        ----------
        value : Number
            Y-coordinate value.
        """
        self._y = value


class TestGraphicsBase:
    @apply_test_settings()
    def test___init__(self) -> None:
        ap.Stage()

        graphics: _TestGraphic = _TestGraphic(variable_name="test_graphics_1")
        testing_helper.assert_attrs(
            expected_attrs={
                "_variable_name": "test_graphics_1",
            },
            any_obj=graphics,
        )

    @apply_test_settings()
    def test__set_initial_basic_values(self) -> None:
        ap.Stage()
        graphics: _TestGraphic = _TestGraphic(variable_name="test_graphics_1")
        graphics._set_initial_basic_values(
            fill_color="#00aaff",
            fill_alpha=0.5,
            line_color="#ffffff",
            line_thickness=3,
            line_alpha=0.3,
            line_cap=ap.LineCaps.ROUND,
            line_joints=ap.LineJoints.BEVEL,
        )
        testing_helper.assert_attrs(
            expected_attrs={
                "_fill_color": "#00aaff",
                "_fill_alpha": 0.5,
                "_line_color": "#ffffff",
                "_line_thickness": 3,
                "_line_alpha": 0.3,
                "_line_cap": ap.LineCaps.ROUND.value,
                "_line_joints": ap.LineJoints.BEVEL.value,
            },
            any_obj=graphics,
        )

    @apply_test_settings()
    def test__set_line_setting_if_not_none_value_exists(self) -> None:
        ap.Stage()
        graphics: _TestGraphic = _TestGraphic(variable_name="test_graphics")
        graphics._set_line_setting_if_not_none_value_exists(
            line_dot_setting=ap.LineDotSetting(dot_size=5),
            line_dash_setting=None,
            line_round_dot_setting=None,
            line_dash_dot_setting=None,
        )
        assert graphics.line_dot_setting == ap.LineDotSetting(dot_size=5)

        graphics = _TestGraphic(variable_name="test_graphics")
        graphics._set_line_setting_if_not_none_value_exists(
            line_dot_setting=None,
            line_dash_setting=ap.LineDashSetting(dash_size=10, space_size=5),
            line_round_dot_setting=None,
            line_dash_dot_setting=None,
        )
        assert graphics.line_dash_setting == ap.LineDashSetting(
            dash_size=10, space_size=5
        )

        graphics = _TestGraphic(variable_name="test_graphics")
        graphics._set_line_setting_if_not_none_value_exists(
            line_dot_setting=None,
            line_dash_setting=None,
            line_round_dot_setting=ap.LineRoundDotSetting(round_size=10, space_size=5),
            line_dash_dot_setting=None,
        )
        assert graphics.line_round_dot_setting == ap.LineRoundDotSetting(
            round_size=10, space_size=5
        )

        graphics = _TestGraphic(variable_name="test_graphics")
        graphics._set_line_setting_if_not_none_value_exists(
            line_dot_setting=None,
            line_dash_setting=None,
            line_round_dot_setting=None,
            line_dash_dot_setting=ap.LineDashDotSetting(
                dot_size=5, dash_size=10, space_size=5
            ),
        )
        assert graphics.line_dash_dot_setting == ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=5
        )

    @apply_test_settings()
    def test__add_to_parent(self) -> None:
        stage: ap.Stage = ap.Stage()
        graphics: _TestGraphic = _TestGraphic(variable_name="test_graphics_1")
        graphics._add_to_parent(parent=None)
        assert graphics.parent == stage

        sprite: ap.Sprite = ap.Sprite()
        graphics = _TestGraphic(variable_name="test_graphics_1")
        graphics._add_to_parent(parent=sprite)
        assert graphics.parent == sprite
