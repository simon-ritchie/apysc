from apysc._testing.testing_helper import apply_test_settings
from apysc._type.expression_string import ExpressionString


class TestExpressionString:
    @apply_test_settings()
    def test___init__(self) -> None:
        exp_str: ExpressionString = ExpressionString(value="Hello!")
        assert exp_str._value == "Hello!"

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        exp_str: ExpressionString = ExpressionString(value="Hello!")
        snapshot_name: str = exp_str._get_next_snapshot_name()
        exp_str._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if exp_str._value_snapshots is None:
            raise AssertionError()
        assert exp_str._value_snapshots[snapshot_name] == "Hello!"

        exp_str._value = "World!"
        exp_str._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert exp_str._value_snapshots[snapshot_name] == "Hello!"

    @apply_test_settings()
    def test__revert(self) -> None:
        exp_str: ExpressionString = ExpressionString(value="Hello!")
        snapshot_name: str = exp_str._get_next_snapshot_name()
        exp_str._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        exp_str._value = "World!"
        exp_str._run_all_revert_methods(snapshot_name=snapshot_name)
        assert exp_str._value == "Hello!"

        exp_str._value = "World!"
        exp_str._run_all_revert_methods(snapshot_name=snapshot_name)
        assert exp_str._value == "World!"

    @apply_test_settings()
    def test_value(self) -> None:
        exp_str: ExpressionString = ExpressionString(value="Hello!")
        assert exp_str.value == "Hello!"
