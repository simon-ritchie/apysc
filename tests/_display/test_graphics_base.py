from random import randint
from typing import Union

from retrying import retry

import apysc as ap
from apysc._display.fill_alpha_mixin import FillAlphaMixIn
from apysc._display.fill_color_mixin import FillColorMixIn
from apysc._display.graphics_base import GraphicsBase
from apysc._testing import testing_helper
from tests._display.test_graphics_expression import assert_fill_attr_expression_exists
from tests._display.test_graphics_expression import (
    assert_fill_opacity_attr_expression_exists,
)
from tests._display.test_graphics_expression import assert_stroke_attr_expression_exists
from tests._display.test_graphics_expression import (
    assert_stroke_linecap_attr_expression_exists,
)
from tests._display.test_graphics_expression import (
    assert_stroke_linejoin_attr_expression_exists,
)
from tests._display.test_graphics_expression import (
    assert_stroke_opacity_attr_expression_exists,
)
from tests._display.test_graphics_expression import (
    assert_stroke_width_attr_expression_exists,
)
from tests._display.test_graphics_expression import assert_x_attr_expression_exists
from tests._display.test_graphics_expression import assert_y_attr_expression_exists


class _TestGraphic(GraphicsBase, FillColorMixIn, FillAlphaMixIn):
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
    def x(self) -> ap.Int:
        """
        Get an x-coordinate.

        Returns
        -------
        x : Int
            X-coordinate.
        """
        return self._x

    @x.setter
    def x(self, value: ap.Int) -> None:
        """
        Update x-coordinate.

        Parameters
        ----------
        value : Int
            X-coordinate value.
        """
        self._x = value

    @property
    def y(self) -> ap.Int:
        """
        Get a y-coordinate.

        Returns
        -------
        y : Int
            Y-coordinate.
        """
        return self._y

    @y.setter
    def y(self, value: ap.Int) -> None:
        """
        Update y-coordinate.

        Parameters
        ----------
        value : Int
            Y-coordinate value.
        """
        self._y = value

    def _update_x_and_skip_appending_exp(self, *, x: Union[int, ap.Int]) -> None:
        """
        Update x-coordinate and skip appending an expression.

        Parameters
        ----------
        x : int or Int
            X-coordinate value.
        """
        self._x = ap.Int(x)

    def _update_y_and_skip_appending_exp(self, *, y: Union[int, ap.Int]) -> None:
        """
        Update y-coordinate and skip appending an expression.

        Parameters
        ----------
        y : int or Int
            Y-coordinate value.
        """
        self._y = ap.Int(y)

    def _initialize_x_if_not_initialized(self) -> None:
        """
        Initialize the _x attribute if this instance does not
        initialize it yet.
        """
        if hasattr(self, "_x"):
            return
        self._x = ap.Int(0)

    def _initialize_y_if_not_initialized(self) -> None:
        """
        Initialize the _y attribute if this instance does not
        initialize it yet.
        """
        if hasattr(self, "_y"):
            return
        self._y = ap.Int(0)


class TestGraphicsBase:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite()

        graphics: _TestGraphic = _TestGraphic(
            parent=None, variable_name="test_graphics_1"
        )
        testing_helper.assert_attrs(
            expected_attrs={
                "_parent": stage,
                "_variable_name": "test_graphics_1",
            },
            any_obj=graphics,
        )

        graphics = _TestGraphic(parent=sprite, variable_name="test_graphics_2")
        testing_helper.assert_attrs(
            expected_attrs={
                "_parent": sprite,
                "_variable_name": "test_graphics_2",
            },
            any_obj=graphics,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_initial_basic_values(self) -> None:
        ap.Stage()
        graphics: _TestGraphic = _TestGraphic(
            parent=None, variable_name="test_graphics_1"
        )
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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_line_setting_if_not_none_value_exists(self) -> None:
        ap.Stage()
        graphics: _TestGraphic = _TestGraphic(
            parent=None, variable_name="test_graphics"
        )
        graphics._set_line_setting_if_not_none_value_exists(
            line_dot_setting=ap.LineDotSetting(dot_size=5),
            line_dash_setting=None,
            line_round_dot_setting=None,
            line_dash_dot_setting=None,
        )
        assert graphics.line_dot_setting == ap.LineDotSetting(dot_size=5)

        graphics = _TestGraphic(parent=None, variable_name="test_graphics")
        graphics._set_line_setting_if_not_none_value_exists(
            line_dot_setting=None,
            line_dash_setting=ap.LineDashSetting(dash_size=10, space_size=5),
            line_round_dot_setting=None,
            line_dash_dot_setting=None,
        )
        assert graphics.line_dash_setting == ap.LineDashSetting(
            dash_size=10, space_size=5
        )

        graphics = _TestGraphic(parent=None, variable_name="test_graphics")
        graphics._set_line_setting_if_not_none_value_exists(
            line_dot_setting=None,
            line_dash_setting=None,
            line_round_dot_setting=ap.LineRoundDotSetting(round_size=10, space_size=5),
            line_dash_dot_setting=None,
        )
        assert graphics.line_round_dot_setting == ap.LineRoundDotSetting(
            round_size=10, space_size=5
        )

        graphics = _TestGraphic(parent=None, variable_name="test_graphics")
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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_basic_vals_expression(self) -> None:
        ap.Stage()
        graphics: _TestGraphic = _TestGraphic(
            parent=None, variable_name="test_graphics_1"
        )
        graphics._set_initial_basic_values(
            fill_color="#00aaff",
            fill_alpha=0.5,
            line_color="#ffffff",
            line_thickness=3,
            line_alpha=0.3,
            line_cap=ap.LineCaps.ROUND,
            line_joints=ap.LineJoints.BEVEL,
        )
        graphics._update_x_and_skip_appending_exp(x=50)
        graphics._update_y_and_skip_appending_exp(y=50)
        expression: str = ""
        expression = graphics._append_basic_vals_expression(
            expression=expression, indent_num=2
        )
        assert_fill_attr_expression_exists(expression=expression)
        assert_fill_opacity_attr_expression_exists(expression=expression)
        assert_stroke_attr_expression_exists(expression=expression)
        assert_stroke_linecap_attr_expression_exists(expression=expression)
        assert_stroke_linejoin_attr_expression_exists(expression=expression)
        assert_stroke_opacity_attr_expression_exists(expression=expression)
        assert_stroke_width_attr_expression_exists(expression=expression)
        assert_x_attr_expression_exists(expression=expression)
        assert_y_attr_expression_exists(expression=expression)
