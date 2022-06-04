import apysc as ap
from apysc._testing.testing_helper import assert_raises
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._validation import variable_name_validation


def test_validate_variable_name_interface_type() -> None:
    assert_raises(
        expected_error_class=TypeError,
        callable_=variable_name_validation.
        validate_variable_name_interface_type,
        match='Specified instance type is not VariableNameInterface',
        instance=10)
    assert_raises(
        expected_error_class=TypeError,
        callable_=variable_name_validation.
        validate_variable_name_interface_type,
        match='\nTest error!',
        instance=10,
        additional_err_msg='Test error!')

    int_1: ap.Int = ap.Int(10)
    instance: VariableNameInterface = variable_name_validation.\
        validate_variable_name_interface_type(instance=int_1)
    assert isinstance(instance, ap.Int)
    assert instance == 10
