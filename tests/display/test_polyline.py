from random import randint

from retrying import retry

from apysc import Array
from apysc import Point2D
from apysc import Polyline
from apysc import Sprite
from apysc import Stage
from tests.testing_helper import assert_attrs


class TestPolyline:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        points: Array = Array([Point2D(10, 20), Point2D(30, 40)])
        polyline: Polyline = Polyline(
            parent=sprite.graphics,
            points=points,
            fill_color='0af',
            fill_alpha=0.5,
            line_color='f0a',
            line_thickness=2,
            line_alpha=0.7)
        assert_attrs(
            expected_attrs={
                '_points': points,
                '_fill_color': '#00aaff',
                '_fill_alpha': 0.5,
                '_line_color': '#ff00aa',
                '_line_thickness': 2,
                '_line_alpha': 0.7,
            },
            any_obj=polyline)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        points: Array = Array([Point2D(10, 20), Point2D(30, 40)])
        polyline: Polyline = Polyline(
            parent=sprite.graphics,
            points=points,
            fill_color='0af',
            fill_alpha=0.5,
            line_color='f0a',
            line_thickness=2,
            line_alpha=0.7)
        repr_str: str = repr(polyline)
        expected: str = (
            f"Polyline('{polyline.variable_name}')"
        )
        assert repr_str == expected
