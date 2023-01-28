from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util
from tests._display.test_graphics_expression import assert_stroke_attr_expression_exists
from apysc._testing.testing_helper import apply_test_settings


class TestPolygonAppendConstructorExpressionMixIn:
    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        expression_data_util.empty_expression()
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        points: ap.Array[ap.Point2D] = ap.Array(
            [ap.Point2D(50, 50), ap.Point2D(150, 50), ap.Point2D(100, 100)]
        )
        sprite.graphics.line_style(color="#333")
        polygon: ap.Polygon = sprite.graphics.draw_polygon(points=points)
        expression: str = expression_data_util.get_current_expression()
        assert_stroke_attr_expression_exists(expression=expression)
        expected: str = (
            f"\nvar {polygon.variable_name} = {stage.variable_name}" f"\n  .polygon("
        )
        assert expected in expression
        assert "\n  .attr({" in expression
