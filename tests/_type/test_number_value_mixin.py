import re
from typing import Any
from typing import Match
from typing import Optional
from typing import Tuple

import pytest

import apysc as ap
from apysc._display.x_mixin import XMixIn
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings
from apysc._type import number_value_mixin
from apysc._type.number_value_mixin import NumberValueMixIn
from apysc._validation import arg_validation_decos


class _TestNumberClass(NumberValueMixIn):
    def __init__(
        self,
        *,
        value: number_value_mixin._NumType,
        type_name: str,
        variable_name_suffix: str = "",
    ) -> None:
        """
        Test class for number value mix-in.

        Parameters
        ----------
        value : NumberValueMixIn or int or float
            Initial number value.
        type_name : str
            This instance expression's type name (e.g., int, number).
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        super(_TestNumberClass, self).__init__(
            value=value, type_name=type_name, variable_name_suffix=variable_name_suffix
        )

    @arg_validation_decos.is_num(arg_position_index=1)
    def _set_value_and_skip_expression_appending(
        self, *, value: number_value_mixin._NumType
    ) -> None:
        """
        Update value attribute and skip expression appending.

        Parameters
        ----------
        value : NumberValueMixIn or int or float
            Any number value to set.
        """
        if isinstance(value, NumberValueMixIn):
            value_: Any = value._value
        else:
            value_ = value  # type: ignore
        self._value = value_


class TestNumberValueMixIn:
    @apply_test_settings()
    def test___init__(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=100, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        testing_helper.assert_attrs(
            expected_attrs={
                "_initial_value": 100,
                "_value": 100,
                "_type_name": "test_mixin",
            },
            any_obj=mixin_1,
        )

        mixin_2: _TestNumberClass = _TestNumberClass(
            value=mixin_1, type_name="test_mixin"
        )
        mixin_2.variable_name = "test_mixin_2"
        testing_helper.assert_attrs(
            expected_attrs={
                "_initial_value": mixin_1,
                "_value": 100,
            },
            any_obj=mixin_2,
        )

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            callable_=_TestNumberClass,
            value="Hello!",
            type_name="test_mixin",
        )

    @apply_test_settings()
    def test_value(self) -> None:
        expression_data_util.empty_expression()
        mixin: _TestNumberClass = _TestNumberClass(value=100, type_name="test_mixin")
        mixin.variable_name = "test_number_value_mixin"
        mixin.value = 200
        assert mixin.value == 200

        with pytest.raises(ValueError):  # type: ignore
            mixin.value = "Hello!"  # type: ignore

    @apply_test_settings()
    def test_append_constructor_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestNumberClass = _TestNumberClass(value=100, type_name="test_mixin")
        mixin_1.variable_name = "test_number_value_mixin_1"
        mixin_1._append_constructor_expression()
        expression: str = expression_data_util.get_current_expression()
        expected: str = "var test_number_value_mixin_1 = 100;"
        assert expected in expression

        mixin_2: _TestNumberClass = _TestNumberClass(
            value=mixin_1, type_name="test_mixin"
        )
        mixin_2.variable_name = "test_number_value_mixin_2"
        mixin_2._append_constructor_expression()
        expression = expression_data_util.get_current_expression()
        expected = "var test_number_value_mixin_2 = " "test_number_value_mixin_1"
        assert expected in expression

    @apply_test_settings()
    def test__append_value_setter_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestNumberClass = _TestNumberClass(value=100, type_name="test_mixin")
        mixin_1.variable_name = "test_number_value_mixin_1"
        mixin_1.value = 200
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin_1.variable_name} = 200;"
        assert expected in expression

        mixin_2: _TestNumberClass = _TestNumberClass(value=100, type_name="test_mixin")
        mixin_2.variable_name = "test_number_value_mixin_2"
        mixin_2.value = mixin_1
        expression = expression_data_util.get_current_expression()
        expected = f"{mixin_2.variable_name} = {mixin_1.variable_name};"
        assert expected in expression

    @apply_test_settings()
    def test_type_name(self) -> None:
        mixin: _TestNumberClass = _TestNumberClass(value=100, type_name="test_mixin")
        assert mixin.type_name == "test_mixin"

    @apply_test_settings()
    def test___add__(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        mixin_2: NumberValueMixIn = mixin_1 + 20
        assert mixin_2.value == 30
        assert mixin_1.variable_name != mixin_2.variable_name

        mixin_3: NumberValueMixIn = mixin_1 + mixin_2
        assert mixin_3.value == 40
        assert mixin_3.variable_name != mixin_2.variable_name

    @apply_test_settings()
    def test__copy(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_0"
        mixin_2: NumberValueMixIn = mixin_1._copy()
        assert mixin_1.value == mixin_2.value
        assert mixin_1.variable_name != mixin_2.variable_name
        assert mixin_2.variable_name.startswith("test_mixin")

    @apply_test_settings()
    def test__append_addition_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_0"
        mixin_2: NumberValueMixIn = mixin_1 + 10
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"var {mixin_2.variable_name} = " f"{mixin_1.variable_name} + 10;"
        )
        assert expected in expression

        mixin_3: NumberValueMixIn = mixin_1 + mixin_2
        expression = expression_data_util.get_current_expression()
        expected = (
            f"var {mixin_3.variable_name} = "
            f"{mixin_1.variable_name} + {mixin_2.variable_name};"
        )
        assert expected in expression

    @apply_test_settings()
    def test___sub__(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=20, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_0"
        mixin_2: NumberValueMixIn = mixin_1 - 15
        assert mixin_2.value == 5

        mixin_3: NumberValueMixIn = mixin_1 - mixin_2
        assert mixin_3.value == 15

    @apply_test_settings()
    def test__append_subtraction_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestNumberClass = _TestNumberClass(value=20, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_0"
        mixin_2: NumberValueMixIn = mixin_1 - 15
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin_2.variable_name} = {mixin_1.variable_name} - 15;"
        assert expected in expression

        mixin_3: NumberValueMixIn = mixin_1 - mixin_2
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{mixin_3.variable_name} = {mixin_1.variable_name} "
            f"- {mixin_2.variable_name};"
        )
        assert expected in expression

    @apply_test_settings()
    def test___mul__(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=20, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_0"
        mixin_2: NumberValueMixIn = mixin_1 * 3
        assert mixin_2.value == 60

        mixin_3: NumberValueMixIn = mixin_1 * mixin_2
        assert mixin_3.value == 1200

    @apply_test_settings()
    def test__append_multiplication_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestNumberClass = _TestNumberClass(value=20, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_0"
        mixin_2: NumberValueMixIn = mixin_1 * 3
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin_2.variable_name} = {mixin_1.variable_name} * 3;"
        assert expected in expression

        mixin_3: NumberValueMixIn = mixin_1 * mixin_2
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{mixin_3.variable_name} = {mixin_1.variable_name}"
            f" * {mixin_2.variable_name};"
        )
        assert expected in expression

    @apply_test_settings()
    def test___truediv__(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_0"
        mixin_2: NumberValueMixIn = mixin_1 / 4
        assert mixin_2.value == 2.5
        assert isinstance(mixin_2, ap.Number)

        mixin_3: NumberValueMixIn = mixin_2 / mixin_1
        assert mixin_3.value == 0.25

    @apply_test_settings()
    def test__append_true_division_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_0"
        mixin_2: NumberValueMixIn = mixin_1 / 4
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin_2.variable_name} = {mixin_1.variable_name};"
            f"\n{mixin_2.variable_name} = {mixin_1.variable_name}"
            " / 4;"
        )
        assert expected in expression

        mixin_3: NumberValueMixIn = mixin_2 / mixin_1
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{mixin_3.variable_name} = {mixin_2.variable_name};"
            f"\n{mixin_3.variable_name} = {mixin_2.variable_name}"
            f" / {mixin_1.variable_name};"
        )
        assert expected in expression

    @apply_test_settings()
    def test___floordiv__(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_0"
        mixin_2: NumberValueMixIn = mixin_1 // 4
        assert mixin_2.value == 2
        assert isinstance(mixin_2, ap.Int)

        mixin_3: _TestNumberClass = _TestNumberClass(value=6, type_name="test_mixin")
        mixin_3.variable_name = "test_mixin_2"
        mixin_4: NumberValueMixIn = mixin_1 // mixin_3
        assert mixin_4.value == 1

    @apply_test_settings()
    def test__append_floor_division_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_0"
        mixin_2: NumberValueMixIn = mixin_1 // 4
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin_2.variable_name} = " f"Math.trunc({mixin_1.variable_name} / 4);"
        )
        assert expected in expression

        mixin_3: NumberValueMixIn = mixin_1 // mixin_2
        expression = expression_data_util.get_current_expression()
        expected = f"{mixin_3.variable_name} = {mixin_1.variable_name};"
        assert expected in expression
        expected = (
            f"{mixin_3.variable_name} = Math.trunc("
            f"{mixin_1.variable_name} / {mixin_2.variable_name});"
        )
        assert expected in expression

    def _make_x_mixin_instance(self) -> Tuple[XMixIn, str]:
        """
        Make the x mixin instance and it's x value variable name.

        Returns
        -------
        x_mixin : XMixIn
            Created x mixin instance.
        x_variable_name : str
            Variable name of the x_mixin x attribute.
        """
        x_mixin: XMixIn = XMixIn()
        x_mixin.variable_name = "test_x_mixin"
        x_mixin.x = ap.Number(10)
        x_variable_name: str = x_mixin._x.variable_name
        return x_mixin, x_variable_name

    def _assert_substitution_expression_to_prev_var_exists(
        self, x_mixin: XMixIn, previous_x_variable_name: str
    ) -> None:
        """
        Assert the substitution expression to the previous x
        variable name exists.

        Parameters
        ----------
        x_mixin : XMixIn
            Targe x mixin instance.
        previous_x_variable_name : str
            Variable name before a calculation.

        Raises
        ------
        AssertionError
            If the substitution expression does not exist.
        """
        expression = expression_data_util.get_current_expression()
        expected: str = f"{previous_x_variable_name} = {x_mixin._x.variable_name};"
        assert expected in expression

    def _assert_substitution_expression_to_prev_var_not_exist(
        self, x_mixin: XMixIn, previous_x_variable_name: str
    ) -> None:
        """
        Assert the substitution expression to the previous x
        variable name does not exist.

        Parameters
        ----------
        x_mixin : XMixIn
            Targe x mixin instance.
        previous_x_variable_name : str
            Variable name before a calculation.

        Raises
        ------
        AssertionError
            If the substitution expression exists.
        """
        expression = expression_data_util.get_current_expression()
        expected: str = f"{previous_x_variable_name} = {x_mixin._x.variable_name};"
        assert expected not in expression

    @apply_test_settings()
    def test___iadd__(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_0"
        int_1: ap.Int = ap.Int(5)
        mixin_1 += int_1
        assert mixin_1.value == 15
        assert mixin_1.variable_name == "test_mixin_0"

        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                r"test_mixin_[0-9]+ = test_mixin_0 \+ "
                rf"{int_1.variable_name};"
                r"\ntest_mixin_0 = test_mixin_[0-9]+;"
            ),
            string=expression,
            flags=re.MULTILINE | re.DOTALL,
        )
        assert match is not None

        expression_data_util.empty_expression()
        x_mixin, previous_variable_name = self._make_x_mixin_instance()
        x_mixin.x += 20
        self._assert_substitution_expression_to_prev_var_exists(
            x_mixin=x_mixin, previous_x_variable_name=previous_variable_name
        )

        expression_data_util.empty_expression()
        x_mixin, previous_variable_name = self._make_x_mixin_instance()
        x: ap.Number = x_mixin.x
        x += 20
        self._assert_substitution_expression_to_prev_var_not_exist(
            x_mixin=x_mixin, previous_x_variable_name=previous_variable_name
        )

    @apply_test_settings()
    def test___isub__(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_0"
        mixin_1 -= 3
        assert mixin_1.value == 7
        assert mixin_1.variable_name == "test_mixin_0"

        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                r"test_mixin_[0-9]+ = test_mixin_0 - 3;"
                r"\ntest_mixin_0 = test_mixin_[0-9]+;"
            ),
            string=expression,
            flags=re.MULTILINE | re.DOTALL,
        )
        assert match is not None

        expression_data_util.empty_expression()
        x_mixin, previous_variable_name = self._make_x_mixin_instance()
        x_mixin.x -= 5
        self._assert_substitution_expression_to_prev_var_exists(
            x_mixin=x_mixin, previous_x_variable_name=previous_variable_name
        )

        expression_data_util.empty_expression()
        x_mixin, previous_variable_name = self._make_x_mixin_instance()
        x: ap.Number = x_mixin.x
        x -= 20
        self._assert_substitution_expression_to_prev_var_not_exist(
            x_mixin=x_mixin, previous_x_variable_name=previous_variable_name
        )

    @apply_test_settings()
    def test___imul__(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_0"
        mixin_1 *= 3
        assert mixin_1.value == 30
        assert mixin_1.variable_name == "test_mixin_0"

        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                r"test_mixin_[0-9]+ = test_mixin_0 \* 3;"
                r"\ntest_mixin_0 = test_mixin_[0-9]+;"
            ),
            string=expression,
            flags=re.MULTILINE | re.DOTALL,
        )
        assert match is not None

        expression_data_util.empty_expression()
        x_mixin, previous_variable_name = self._make_x_mixin_instance()
        x_mixin.x *= 2
        self._assert_substitution_expression_to_prev_var_exists(
            x_mixin=x_mixin, previous_x_variable_name=previous_variable_name
        )

        expression_data_util.empty_expression()
        x_mixin, previous_variable_name = self._make_x_mixin_instance()
        x: ap.Number = x_mixin.x
        x *= 2
        self._assert_substitution_expression_to_prev_var_not_exist(
            x_mixin=x_mixin, previous_x_variable_name=previous_variable_name
        )

    @apply_test_settings()
    def test___itruediv__(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_0"
        mixin_1 /= 4
        assert mixin_1.value == 2.5
        assert mixin_1.variable_name == "test_mixin_0"

        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(r"var n_[0-9]+ = test_mixin_0;" r"\nn_[0-9]+ = test_mixin_0 / 4;"),
            string=expression,
            flags=re.MULTILINE | re.DOTALL,
        )
        assert match is not None

        expression_data_util.empty_expression()
        x_mixin, previous_variable_name = self._make_x_mixin_instance()
        x_mixin.x /= 2
        self._assert_substitution_expression_to_prev_var_exists(
            x_mixin=x_mixin, previous_x_variable_name=previous_variable_name
        )

        expression_data_util.empty_expression()
        x_mixin, previous_variable_name = self._make_x_mixin_instance()
        x: ap.Number = x_mixin.x
        x /= 2
        self._assert_substitution_expression_to_prev_var_not_exist(
            x_mixin=x_mixin, previous_x_variable_name=previous_variable_name
        )

    @apply_test_settings()
    def test___str__(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        assert str(mixin_1) == "10"

        del mixin_1._value
        assert str(mixin_1) == "0"

    @apply_test_settings()
    def test___eq__(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_0"
        mixin_2: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_2.variable_name = "test_mixin_1"
        mixin_3: _TestNumberClass = _TestNumberClass(value=11, type_name="test_mixin")
        mixin_3.variable_name = "test_mixin_3"

        assert mixin_1 == 10
        assert mixin_1 == mixin_2
        assert not mixin_1 == 11
        assert not mixin_1 == mixin_3

        assert isinstance(mixin_1 == 10, ap.Boolean)
        assert isinstance(mixin_1 == mixin_2, ap.Boolean)

    @apply_test_settings()
    def test___ne__(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        mixin_2: _TestNumberClass = _TestNumberClass(value=11, type_name="test_mixin")
        mixin_2.variable_name = "test_mixin_2"
        assert mixin_1 != 11
        assert mixin_1 != mixin_2

        assert isinstance(mixin_1 != 11, ap.Boolean)
        assert isinstance(mixin_1 != mixin_2, ap.Boolean)

    @apply_test_settings()
    def test___lt__(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        mixin_2: _TestNumberClass = _TestNumberClass(value=11, type_name="test_mixin")
        mixin_2.variable_name = "test_mixin_2"
        mixin_3: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_3.variable_name = "test_mixin_3"

        assert mixin_1 < 11
        assert mixin_1 < mixin_2
        assert not mixin_1 < 10
        assert not mixin_1 < mixin_3
        assert isinstance(mixin_1 < 11, ap.Boolean)
        assert isinstance(mixin_1 < mixin_2, ap.Boolean)

    @apply_test_settings()
    def test___le__(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        mixin_2: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_2.variable_name = "test_mixin_2"
        mixin_3: _TestNumberClass = _TestNumberClass(value=11, type_name="test_mixin")
        mixin_3.variable_name = "test_mixin_3"
        mixin_4: _TestNumberClass = _TestNumberClass(value=9, type_name="test_mixin")
        mixin_4.variable_name = "test_mixin_4"

        assert mixin_1 <= 10
        assert mixin_1 <= 11
        assert mixin_1 <= mixin_2
        assert mixin_1 <= mixin_3
        assert not mixin_1 <= 9
        assert not mixin_1 <= mixin_4

        assert isinstance(mixin_1 <= 10, ap.Boolean)
        assert isinstance(mixin_1 <= mixin_2, ap.Boolean)

    @apply_test_settings()
    def test___gt__(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        mixin_2: _TestNumberClass = _TestNumberClass(value=9, type_name="test_mixin")
        mixin_2.variable_name = "test_mixin_2"
        mixin_3: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_3.variable_name = "test_mixin_3"

        assert mixin_1 > 9
        assert mixin_1 > mixin_2
        assert not mixin_1 > 10
        assert not mixin_1 > mixin_3

        assert isinstance(mixin_1 > 9, ap.Boolean)
        assert isinstance(mixin_1 > mixin_2, ap.Boolean)

    @apply_test_settings()
    def test___ge__(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        mixin_2: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_2.variable_name = "test_mixin_2"
        mixin_3: _TestNumberClass = _TestNumberClass(value=9, type_name="test_mixin")
        mixin_3.variable_name = "test_mixin_3"
        mixin_4: _TestNumberClass = _TestNumberClass(value=11, type_name="test_mixin")
        mixin_4.variable_name = "test_mixin_4"

        assert mixin_1 >= 10
        assert mixin_1 >= 9
        assert mixin_1 >= mixin_2
        assert mixin_1 >= mixin_3
        assert not mixin_1 >= 11
        assert not mixin_1 >= mixin_4

        assert isinstance(mixin_1 >= 10, ap.Boolean)
        assert isinstance(mixin_1 >= mixin_2, ap.Boolean)

    @apply_test_settings()
    def test___int__(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        integer: int = int(mixin_1)
        assert mixin_1 == 10
        assert isinstance(integer, int)

    @apply_test_settings()
    def test___float__(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=10.5, type_name="test_mixin")
        float_val: float = float(mixin_1)
        assert float_val == 10.5
        assert isinstance(float_val, float)

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=10.5, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        snapshot_name: str = "snapshot_1"
        mixin_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if mixin_1._value_snapshots is None:
            raise AssertionError()
        assert mixin_1._value_snapshots[snapshot_name] == 10.5

        mixin_1.value = 20
        mixin_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin_1._value_snapshots[snapshot_name] == 10.5

    @apply_test_settings()
    def test__revert(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=10.5, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        snapshot_name: str = "snapshot_1"
        mixin_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin_1.value = 20
        mixin_1._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin_1.value == 10.5

        mixin_1.value = 20
        mixin_1._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin_1.value == 20

    @apply_test_settings()
    def test__append_eq_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        mixin_2: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_2.variable_name = "test_mixin_2"
        result: ap.Boolean = mixin_1 == mixin_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{mixin_1.variable_name} === {mixin_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = mixin_1 == 10
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{mixin_1.variable_name} === "
                rf"{var_names.INT}\_.+?\;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__append_ne_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        mixin_2: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_2.variable_name = "test_mixin_2"
        result: ap.Boolean = mixin_1 != mixin_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{mixin_1.variable_name} !== "
            f"{mixin_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = mixin_1 != 20
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{mixin_1.variable_name} !== "
                rf"{var_names.INT}\_.+?;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__append_lt_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        mixin_2: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_2.variable_name = "test_mixin_2"
        result: ap.Boolean = mixin_1 < mixin_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{mixin_1.variable_name} < {mixin_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = mixin_1 < 10
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{mixin_1.variable_name} \< "
                rf"{var_names.INT}\_.+;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__append_le_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        mixin_2: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_2.variable_name = "test_mixin_2"
        result: ap.Boolean = mixin_1 <= mixin_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{mixin_1.variable_name} <= {mixin_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = mixin_1 <= 10
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{mixin_1.variable_name} <= "
                rf"{var_names.INT}\_.+;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__append_gt_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        mixin_2: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_2.variable_name = "test_mixin_2"
        result: ap.Boolean = mixin_1 > mixin_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{mixin_1.variable_name} > {mixin_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = mixin_1 > 10
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{mixin_1.variable_name} > "
                rf"{var_names.INT}\_.+;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__append_ge_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        mixin_2: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_2.variable_name = "test_mixin_2"
        result: ap.Boolean = mixin_1 >= mixin_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{mixin_1.variable_name} >= {mixin_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = mixin_1 >= 10
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{mixin_1.variable_name} >= "
                rf"{var_names.INT}\_.+?;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__convert_other_val_to_int_or_number(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        converted_val: Any = mixin_1._convert_other_val_to_int_or_number(other=10)
        assert isinstance(converted_val, ap.Int)
        assert converted_val == 10

        converted_val = mixin_1._convert_other_val_to_int_or_number(other=10.5)
        assert isinstance(converted_val, ap.Number)
        assert converted_val == 10.5

        converted_val = mixin_1._convert_other_val_to_int_or_number(other="Hello")
        assert converted_val == "Hello"

    @apply_test_settings()
    def test__append_incremental_calc_substitution_expression(self) -> None:
        expression_data_util.empty_expression()
        x_mixin, previous_variable_name = self._make_x_mixin_instance()
        x_mixin.x += 10
        self._assert_substitution_expression_to_prev_var_exists(
            x_mixin=x_mixin, previous_x_variable_name=previous_variable_name
        )
        assert x_mixin._x._incremental_calc_prev_name == ""

    @apply_test_settings()
    def test__append_modulo_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        mixin_2: NumberValueMixIn = mixin_1 % 10
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin_2.variable_name} = " f"{mixin_1.variable_name} % 10;"
        assert expected in expression

    @apply_test_settings()
    def test___mod__(self) -> None:
        mixin_1: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        mixin_2: NumberValueMixIn = mixin_1 % 3
        assert mixin_2 == 1

        mixin_1 = _TestNumberClass(value=10.5, type_name="test_mixin")
        mixin_1.variable_name = "test_mixin_1"
        mixin_3: NumberValueMixIn = mixin_1 % ap.Int(3)
        assert mixin_3 == 1.5

    @apply_test_settings()
    def test__create_substitution_expression(self) -> None:
        mixin: _TestNumberClass = _TestNumberClass(value=10, type_name="test_mixin")
        expression: str = mixin._create_initial_substitution_expression()
        assert expression == f"{mixin.variable_name} = 10;"

        int_val: ap.Int = ap.Int(10)
        mixin = _TestNumberClass(value=int_val, type_name="test_mixin")
        expression = mixin._create_initial_substitution_expression()
        assert expression == f"{mixin.variable_name} = {int_val.variable_name};"
