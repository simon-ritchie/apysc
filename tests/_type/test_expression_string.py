from random import randint

from retrying import retry

from apysc._type.expression_string import ExpressionString


class TestExpressionString:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        exp_str: ExpressionString = ExpressionString(value='Hello!')
        assert exp_str._value == 'Hello!'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        exp_str: ExpressionString = ExpressionString(value='Hello!')
        snapshot_name: str = exp_str._get_next_snapshot_name()
        exp_str._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert exp_str._value_snapshots[snapshot_name] == 'Hello!'

        exp_str._value = 'World!'
        exp_str._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert exp_str._value_snapshots[snapshot_name] == 'Hello!'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        exp_str: ExpressionString = ExpressionString(value='Hello!')
        snapshot_name: str = exp_str._get_next_snapshot_name()
        exp_str._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        exp_str._value = 'World!'
        exp_str._run_all_revert_methods(snapshot_name=snapshot_name)
        assert exp_str._value == 'Hello!'

        exp_str._value = 'World!'
        exp_str._run_all_revert_methods(snapshot_name=snapshot_name)
        assert exp_str._value == 'World!'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_value(self) -> None:
        exp_str: ExpressionString = ExpressionString(value='Hello!')
        assert exp_str.value == 'Hello!'
