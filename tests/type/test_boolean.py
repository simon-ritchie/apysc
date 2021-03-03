from typing import Any, Dict
from apyscript.type import Int
from apyscript.type import Boolean
from tests import testing_helper


class TestBoolean:

    def test___init__(self) -> None:
        boolean_1: Boolean = Boolean(value=Int(1))
        expected_attrs: Dict[str, Any] = {
            '_initial_value': Int(1),
            '_value': True,
            '_type_name': 'boolean',
        }
        testing_helper.assert_attrs(
            expected_attrs=expected_attrs, any_obj=boolean_1)
        assert boolean_1.variable_name.startswith('boolean_')

        boolean_2: Boolean = Boolean(value=boolean_1)
        expected_attrs: Dict[str, Any] = {
            '_initial_value': boolean_1,
            '_value': True,
        }
        testing_helper.assert_attrs(
            expected_attrs=expected_attrs, any_obj=boolean_2)

        boolean_3: Boolean = Boolean(value=False)
        assert not boolean_3._value
