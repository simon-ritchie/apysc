from random import randint

from retrying import retry

import apysc as ap
from apysc._display.graphics_base import GraphicsBase
from tests import testing_helper


class TestGraphicsBase:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        graphics_base: GraphicsBase = GraphicsBase(
            parent=sprite.graphics, x=ap.Int(100), y=ap.Int(200),
            variable_name='test_graphics')
        testing_helper.assert_attrs(
            expected_attrs={
                'parent_graphics': sprite.graphics,
                '_x': 100,
                '_y': 200,
                '_variable_name': 'test_graphics',
                'stage': stage,
            },
            any_obj=graphics_base)

        graphics_base = GraphicsBase(
            parent=sprite.graphics, x=300, y=400,
            variable_name='test_graphics')
        testing_helper.assert_attrs(
            expected_attrs={
                'parent_graphics': sprite.graphics,
                '_x': 300,
                '_y': 400,
            },
            any_obj=graphics_base)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_x(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        graphics_base: GraphicsBase = GraphicsBase(
            parent=sprite.graphics, x=ap.Int(100), y=ap.Int(200),
            variable_name='test_graphics')
        graphics_base.x = ap.Int(300)
        assert graphics_base.x == 300

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_y(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        graphics_base: GraphicsBase = GraphicsBase(
            parent=sprite.graphics, x=ap.Int(100), y=ap.Int(200),
            variable_name='test_graphics')
        graphics_base.y = ap.Int(400)
        assert graphics_base.y == 400

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_variable_name(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        graphics_base: GraphicsBase = GraphicsBase(
            parent=sprite.graphics, x=ap.Int(100), y=ap.Int(200),
            variable_name='test_graphics_1')
        assert graphics_base.variable_name == 'test_graphics_1'
        graphics_base.variable_name = 'test_graphics_2'
        assert graphics_base.variable_name == 'test_graphics_2'
