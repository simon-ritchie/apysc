from apysc._type.expression_string import ExpressionString


class TestExpressionString:

    def test___init__(self) -> None:
        exp_str: ExpressionString = ExpressionString(value='Hello!')
        assert exp_str._value == 'Hello!'

    def test__make_snapshot(self) -> None:
        exp_str: ExpressionString = ExpressionString(value='Hello!')
        snapshot_name: str = exp_str._get_next_snapshot_name()
        exp_str._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert exp_str._value_snapshots[snapshot_name] == 'Hello!'

        exp_str._value = 'World!'
        exp_str._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert exp_str._value_snapshots[snapshot_name] == 'Hello!'
