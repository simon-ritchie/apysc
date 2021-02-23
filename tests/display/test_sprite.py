from random import randint

from retrying import retry

from apyscript.display.graphics import Graphics
from apyscript.display.sprite import Sprite
from apyscript.display.stage import Stage
from apyscript.display.stage import get_stage_variable_name
from apyscript.expression import expression_file_util
from apyscript.file import file_util
from tests import testing_helper


class TestSprite:

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
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

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_add_child(self) -> None:
        stage: Stage = Stage()
        parent_sprite: Sprite = Sprite(stage=stage)
        child_sprite: Sprite = Sprite(stage=stage)
        parent_sprite.add_child(child=child_sprite)
        assert parent_sprite._childs == [child_sprite]

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test__append_constructor_expression(self) -> None:
        stage: Stage = Stage()
        stage_variable_name: str = get_stage_variable_name()
        file_util.remove_file_if_exists(
            file_path=expression_file_util.EXPRESSION_FILE_PATH)
        sprite: Sprite = Sprite(stage=stage)
        expression: str = file_util.read_txt(
            file_path=expression_file_util.EXPRESSION_FILE_PATH)
        expected: str = (
            '<script type="text/javascript">'
            f'\nvar {sprite.variable_name} = {stage_variable_name}.group();'
            '\n</script>'
        )
        assert expression.strip() == expected
        file_util.remove_file_if_exists(
            file_path=expression_file_util.EXPRESSION_FILE_PATH)

        class SubClass(Sprite):
            pass

        subclass_instance: SubClass = SubClass(stage=stage)
        appended: bool = subclass_instance._append_constructor_expression()
        assert not appended
