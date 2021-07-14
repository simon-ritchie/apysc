import apysc as ap
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._validation import variable_name_validation
from tests.testing_helper import assert_raises


def test_validate_variable_name_interface_type() -> None:
    assert_raises(
        expected_error_class=TypeError,
        func_or_method=variable_name_validation.
        validate_variable_name_interface_type,
        kwargs={'instance': 10},
        match='Specified instance type is not VariableNameInterface')

    int_1: ap.Int = ap.Int(10)
    instance: VariableNameInterface = variable_name_validation.\
        validate_variable_name_interface_type(instance=int_1)
    assert isinstance(instance, ap.Int)
    assert instance == 10
