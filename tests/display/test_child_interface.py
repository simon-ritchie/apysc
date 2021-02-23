from random import randint

from retrying import retry

from apyscript.display.sprite import Sprite
from apyscript.display.stage import Stage
from apyscript.expression import expression_file_util
from tests import testing_helper


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

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_remove_child(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite)
        stage.remove_child(child=sprite)
        assert stage._childs == []

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=stage.remove_child,
            kwargs={'child': sprite})
