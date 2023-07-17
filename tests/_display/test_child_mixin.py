import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._display.child_mixin import ChildMixIn
from apysc._display.display_object import DisplayObject
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


class TestChildMixIn:
    """Because of `VariableNameMixIn` inheritance,
    each test will be executed with Stage and Sprite
    (ChildMixIn subclasses).
    """

    @apply_test_settings()
    def test_add_child(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        assert stage._children == ap.Array([sprite])
        assert sprite.parent == stage

    @apply_test_settings()
    def test_remove_child(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite_1: ap.Sprite = ap.Sprite()
        stage.add_child(child=sprite_1)
        sprite_2: ap.Sprite = ap.Sprite()
        stage.add_child(child=sprite_2)
        stage.remove_child(child=sprite_2)
        assert stage._children == ap.Array([sprite_1])
        assert sprite_2.parent is None

    @apply_test_settings()
    def test_contains(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite_1: ap.Sprite = ap.Sprite()
        stage.add_child(child=sprite_1)
        assert stage.contains(child=sprite_1)

        sprite_2: ap.Sprite = ap.Sprite()
        assert not sprite_1.contains(child=sprite_2)

    @apply_test_settings()
    def test__append_contains_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite_1: ap.Sprite = ap.Sprite()
        stage.add_child(child=sprite_1)
        result: ap.Boolean = stage.contains(sprite_1)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result._variable_name} = "
            f"{stage.variable_name}.has({sprite_1.variable_name});"
        )
        assert expected in expression

    @apply_test_settings()
    def test_num_children(self) -> None:
        stage: ap.Stage = ap.Stage()
        assert stage.num_children == 0
        sprite_1: ap.Sprite = ap.Sprite()
        stage.add_child(child=sprite_1)
        assert stage.num_children == 1
        sprite_2: ap.Sprite = ap.Sprite()
        stage.add_child(child=sprite_2)
        assert stage.num_children == 2

        sprite_3: ap.Sprite = ap.Sprite()
        sprite_1.add_child(child=sprite_3)
        assert sprite_1.num_children == 2

    @apply_test_settings()
    def test_get_child_at(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite_1: ap.Sprite = ap.Sprite()
        stage.add_child(child=sprite_1)
        child_1: DisplayObject = stage.get_child_at(index=0)
        assert child_1 == sprite_1

        child_2: DisplayObject = stage.get_child_at(index=1)
        assert not isinstance(child_2, ap.Sprite)
        assert isinstance(child_2, DisplayObject)

    @apply_test_settings()
    def test__append_num_children_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite_1: ap.Sprite = ap.Sprite()
        stage.add_child(child=sprite_1)
        num_children_1: ap.Int = stage.num_children
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{num_children_1.variable_name} = "
            f"{stage.variable_name}.children().length;"
        )
        assert expected in expression

        sprite_2: ap.Sprite = ap.Sprite()
        sprite_1.add_child(child=sprite_2)
        num_children_2 = sprite_1.num_children
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{num_children_2.variable_name} = "
            f"{sprite_1.variable_name}.children().length;"
        )
        assert expected in expression

    @apply_test_settings()
    def test__append_get_child_at_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite_1: ap.Sprite = ap.Sprite()
        stage.add_child(child=sprite_1)
        int_1: ap.Int = ap.Int(0)
        child_1: DisplayObject = stage.get_child_at(index=int_1)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"var {child_1.variable_name} = "
            f"{stage.variable_name}.children()"
            f"[{int_1.variable_name}];"
        )
        assert expected in expression

        sprite_2: ap.Sprite = ap.Sprite()
        sprite_1.add_child(child=sprite_2)
        child_2: DisplayObject = sprite_1.get_child_at(index=0)
        expression = expression_data_util.get_current_expression()
        expected = (
            f"var {child_2.variable_name} = " f"{sprite_1.variable_name}.children()[0];"
        )
        assert expected in expression

    @apply_test_settings()
    def test__initialize_children_if_not_initialized(self) -> None:
        child_interface: ChildMixIn = ChildMixIn()
        child_interface._initialize_children_if_not_initialized()
        assert child_interface._children == []

        sprite: ap.Sprite = ap.Sprite()
        child_interface._children = ap.Array([sprite])
        child_interface._initialize_children_if_not_initialized()
        assert child_interface._children == [sprite]

    @apply_test_settings()
    def test__make_snapshot(self) -> None:

        stage: ap.Stage = ap.Stage()
        sprite_1: ap.Sprite = ap.Sprite()
        stage.add_child(child=sprite_1)
        sprite_2: ap.Sprite = ap.Sprite()
        sprite_1.add_child(child=sprite_2)
        stage._children.append(100)  # type: ignore

        snapshot_name_1: str = stage._get_next_snapshot_name()
        stage._run_all_make_snapshot_methods(snapshot_name=snapshot_name_1)
        if stage._children_snapshots is None:
            raise AssertionError()
        assert stage._children_snapshots[snapshot_name_1] == [sprite_1, 100]
        assert stage._snapshot_exists(snapshot_name=snapshot_name_1)
        if sprite_1._children_snapshots is None:
            raise AssertionError()
        assert sprite_1._children_snapshots[snapshot_name_1] == [
            sprite_1.graphics,
            sprite_2,
        ]

        stage.remove_child(child=sprite_1)
        stage._run_all_make_snapshot_methods(snapshot_name=snapshot_name_1)
        assert stage._children_snapshots[snapshot_name_1] == [sprite_1, 100]

    @apply_test_settings()
    def test__revert(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite_1: ap.Sprite = ap.Sprite()
        stage.add_child(child=sprite_1)
        sprite_2: ap.Sprite = ap.Sprite()
        sprite_1.add_child(child=sprite_2)
        stage._children.append(100)  # type: ignore

        snapshot_name_1: str = sprite_1._get_next_snapshot_name()
        stage._run_all_make_snapshot_methods(snapshot_name=snapshot_name_1)
        stage.remove_child(child=sprite_1)
        sprite_1.remove_child(child=sprite_2)
        stage._run_all_revert_methods(snapshot_name=snapshot_name_1)
        assert stage._children == [sprite_1, 100]
        assert sprite_1._children == [sprite_1.graphics, sprite_2]
        assert not stage._snapshot_exists(snapshot_name=snapshot_name_1)
        assert not sprite_1._snapshot_exists(snapshot_name=snapshot_name_1)

        stage.remove_child(child=sprite_1)
        stage._run_all_revert_methods(snapshot_name=snapshot_name_1)
        assert stage._children == [100]

    @apply_test_settings()
    def test__append_expression_of_remove_children(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        sprite._append_expression_of_remove_children()
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"var children = {sprite.variable_name}.children();"
            "\nvar length = children.length;"
            "\nfor (var i = 0; i < length; i++) {"
            "\n  var child = children[i];"
            f"\n  {sprite.variable_name}.remove(child);"
            "\n}"
        )
        assert expected in expression

    @apply_test_settings()
    def test_remove_children(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
        sprite.remove_children()
        assert sprite._children.length == 0
        expression: str = expression_data_util.get_current_expression()
        assert ".children()" in expression


@apply_test_settings()
def test_append_expression_of_add_child() -> None:
    stage: ap.Stage = ap.Stage()
    sprite: ap.Sprite = ap.Sprite()
    stage.add_child(child=sprite)
    expected: str = f"{stage.variable_name}.add({sprite.variable_name});"
    expression: str = expression_data_util.get_current_expression()
    assert expected in expression


@apply_test_settings()
def test_append_expression_of_remove_child() -> None:
    stage: ap.Stage = ap.Stage()
    sprite: ap.Sprite = ap.Sprite()
    stage.add_child(child=sprite)
    stage.remove_child(child=sprite)
    expression: str = expression_data_util.get_current_expression()
    match: Optional[Match] = re.search(
        pattern=(
            rf"var {var_names.PARENT}_.+? = "
            rf"{sprite.variable_name}.parent\(\);"
            rf"\nif \({var_names.PARENT}_.+?\) {{"
            rf"\n  {var_names.PARENT}_.+?.removeElement\("
            rf"{sprite.variable_name}\);"
            r"\n}"
        ),
        string=expression,
        flags=re.MULTILINE | re.DOTALL,
    )
    assert match is not None
