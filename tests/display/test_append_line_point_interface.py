from random import randint

from retrying import retry

from apysc.display.append_line_point_interface import AppendLinePointInterface
from apysc import Int
from apysc.expression import expression_file_util
from tests.testing_helper import assert_raises


class TestAppendLinePointInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_append_line_point(self) -> None:
        expression_file_util.remove_expression_file()
        interface: AppendLinePointInterface = AppendLinePointInterface()
        interface.variable_name = 'test_append_line_point_interface'
        x: Int = Int(50)
        y: Int = Int(100)
        assert_raises(
            expected_error_class=AttributeError,
            func_or_method=interface.append_line_point,
            kwargs={'x': x, 'y': y},
            match=r'_points_var_name attribute is not set.',
        )

        interface._points_var_name = 'test_points'
        interface.append_line_point(x=x, y=y)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'test_points.push([{x.variable_name}, {y.variable_name}]);'
            f'\n{interface.variable_name}.plot(test_points);'
        )
        assert expected in expression
