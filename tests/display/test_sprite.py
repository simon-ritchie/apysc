from retrying import retry

from apyscript.display.sprite import Sprite
from apyscript.display.stage import Stage
from apyscript.display.graphics import Graphics
from tests import testing_helper


class TestSprite:

    @retry(stop_max_attempt_number=5, wait_fixed=300)
    def test___init__(self):
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        testing_helper.assert_attrs(
            expected_attrs={
                'stage': stage,
            },
            any_obj=sprite)
        testing_helper.assert_attrs_type(
            expected_types={
                'graphics': Graphics,
            },
            any_obj=sprite)

    def test_add_child(self):
        stage: Stage = Stage()
        parent_sprite: Sprite = Sprite(stage=stage)
        child_sprite: Sprite = Sprite(stage=stage)
        parent_sprite.add_child(child=child_sprite)
        assert parent_sprite._childs == [child_sprite]
