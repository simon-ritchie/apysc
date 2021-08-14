from apysc._type.expression_string import ExpressionString


class TestExpressionString:

    def test___init__(self) -> None:
        exp_str: ExpressionString = ExpressionString(value='Hello!')
        assert exp_str._value == 'Hello!'
