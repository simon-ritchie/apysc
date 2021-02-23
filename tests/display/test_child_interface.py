from random import randint

from retrying import retry

from apyscript.display.child_interface import ChildInterface
from apyscript.display.sprite import Sprite
from apyscript.display.stage import Stage
from apyscript.expression import expression_file_util


class TestChildInterface:
    """Because of `VariableNameInterface` inheritance,
    each test will be executed with Stage and Sprite
    (ChildInterface subclasses).
    """

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_add_child(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite)
        assert stage._childs == [sprite]
        assert sprite.parent == stage

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test__append_expression_of_add_child(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite)
        expected: str = (
            f'{stage.variable_name}.add({sprite.variable_name});'
        )
        expression: str = expression_file_util.get_current_expression()
        assert expected in expression
