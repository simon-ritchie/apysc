import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


class TestWheelEvent:
    @apply_test_settings()
    def test___init__(self) -> None:
        e: ap.WheelEvent = ap.WheelEvent(this=ap.document)
        assert e.variable_name.startswith(f"{var_names.WHEEL_EVENT}_")

    @apply_test_settings()
    def test_delta_y(self) -> None:
        e: ap.WheelEvent = ap.WheelEvent(this=ap.document)
        delta_y: ap.Number = e.delta_y
        assert isinstance(delta_y, ap.Number)
        assert delta_y == 0

    @apply_test_settings()
    def test__append_delta_y_getter_expression(self) -> None:
        ap.Stage()
        e: ap.WheelEvent = ap.WheelEvent(this=ap.document)
        delta_y: ap.Number = e.delta_y
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{delta_y.variable_name} = " f"{e.variable_name}.deltaY;"
        assert expected in expression

    @apply_test_settings()
    def test_delta_x(self) -> None:
        e: ap.WheelEvent = ap.WheelEvent(this=ap.document)
        delta_x: ap.Number = e.delta_x
        assert isinstance(delta_x, ap.Number)
        assert delta_x == 0

    @apply_test_settings()
    def test__append_delta_x_getter_expression(self) -> None:
        ap.Stage()
        e: ap.WheelEvent = ap.WheelEvent(this=ap.document)
        delta_x: ap.Number = e.delta_x
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{delta_x.variable_name} = " f"{e.variable_name}.deltaX;"
        assert expected in expression
