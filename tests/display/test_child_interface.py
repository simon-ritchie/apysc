from random import randint

from retrying import retry

from apyscript.display import Sprite
from apyscript.display.display_object import DisplayObject
from apyscript.display.stage import Stage
from apyscript.expression import expression_file_util
from apyscript.type import Array
from tests import testing_helper


class TestChildInterface:
    """Because of `VariableNameInterface` inheritance,
    each test will be executed with Stage and Sprite
    (ChildInterface subclasses).
    """

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_add_child(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite)
        assert stage._childs == Array([sprite])
        assert sprite.parent == stage

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_expression_of_add_child(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite)
        expected: str = (
            f'{stage.variable_name}.add({sprite.variable_name});'
        )
        expression: str = expression_file_util.get_current_expression()
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_remove_child(self) -> None:
        stage: Stage = Stage()
        sprite_1: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite_1)
        sprite_2: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite_2)
        stage.remove_child(child=sprite_2)
        assert stage._childs == Array([sprite_1])
        assert sprite_2.parent is None

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_expression_of_remove_child(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite)
        stage.remove_child(child=sprite)
        expected: str = (
            f'{stage.variable_name}.removeElement({sprite.variable_name});'
        )
        expression: str = expression_file_util.get_current_expression()
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_contains(self) -> None:
        stage: Stage = Stage()
        sprite_1: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite_1)
        assert stage.contains(child=sprite_1)

        sprite_2: Sprite = Sprite(stage=stage)
        assert not stage.contains(child=sprite_2)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_num_children(self) -> None:
        stage: Stage = Stage()
        assert stage.num_children == 0
        sprite_1: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite_1)
        assert stage.num_children == 1
        sprite_2: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite_2)
        assert stage.num_children == 2

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_get_child_at(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite)
        child: DisplayObject = stage.get_child_at(index=0)
        assert child == sprite

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=stage.get_child_at,
            kwargs={'index': 1})
