from typing import Any, Dict, Type
from apysc.branch.if_base import IfBase
from apysc.type import Boolean
from tests import testing_helper


class IfSubClass(IfBase):

    def __enter__(self) -> None:
        """
        Method to be called when begining of with statement.
        """

    def __exit__(
            self, exc_type: Type,
            exc_value: Any,
            traceback: Any) -> None:
        """
        Method to be called when end of with statement.

        Parameters
        ----------
        exc_type : Type
            Exception type.
        exc_value : *
            Exception value.
        traceback : *
            Traceback value.
        """


class TestIfBase:

    def test___init__(self) -> None:
        condition: Boolean = Boolean(True)
        locals_: Dict[str, Any] = {'value1': 10}
        globals_: Dict[str, Any] = {'value2': 20}
        instance: IfSubClass = IfSubClass(
            condition=condition, locals_=locals_, globals_=globals_)
        testing_helper.assert_attrs(
            expected_attrs={
                '_condition': condition,
                '_locals': locals_,
                '_globals': globals_,
            },
            any_obj=instance)
