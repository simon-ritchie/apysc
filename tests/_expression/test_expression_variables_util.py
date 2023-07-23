import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import expression_variables_util
from apysc._expression import indent_num
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test__get_next_variable_num() -> None:
    ap.Stage()
    next_variable_num: int = expression_variables_util._get_next_variable_num(
        type_name="sprite"
    )
    assert next_variable_num == 1

    for _ in range(2):
        expression_variables_util._save_next_variable_name_count(type_name="sprite")
    next_variable_num = expression_variables_util._get_next_variable_num(
        type_name="sprite"
    )
    assert next_variable_num == 3


@apply_test_settings()
def test__make_variable_name() -> None:
    variable_name: str = expression_variables_util._make_variable_name(
        type_name="i", variable_num=3
    )
    assert variable_name == "i_3"


@apply_test_settings()
def test_get_next_variable_name() -> None:
    expression_data_util.empty_expression(skip_variable_name_count=False)
    variable_name: str = expression_variables_util.get_next_variable_name(
        type_name="sprite"
    )
    assert variable_name == "sprite_1"

    variable_name = expression_variables_util.get_next_variable_name(type_name="sprite")
    assert variable_name == "sprite_2"


@apply_test_settings()
def test_append_substitution_expression() -> None:
    indent_num.reset()
    ap.Stage()
    int_1: ap.Int = ap.Int(10)
    int_2: ap.Int = ap.Int(20)
    expression_variables_util.append_substitution_expression(
        left_value=int_2, right_value=int_1
    )
    expression: str = expression_data_util.get_current_expression()
    expected: str = f"{int_2.variable_name} = {int_1.variable_name};"
    assert expected in expression


@apply_test_settings()
def test_append_substitution_expression_with_names() -> None:
    ap.Stage()
    expression_variables_util.append_substitution_expression_with_names(
        left_variable_name="i_5", right_variable_name="i_6"
    )
    expression: str = expression_data_util.get_current_expression()
    expected: str = "i_5 = i_6"
    assert expected in expression

    expression_data_util.empty_expression()
    expression_variables_util.append_substitution_expression_with_names(
        left_variable_name="", right_variable_name="i_6"
    )
    expression = expression_data_util.get_current_expression()
    assert " = i_6" not in expression

    expression_variables_util.append_substitution_expression_with_names(
        left_variable_name="i_5", right_variable_name=""
    )
    expression = expression_data_util.get_current_expression()
    assert "i_5 = " not in expression


@apply_test_settings()
def test__save_next_variable_name_count() -> None:
    """_save_next_variable_name_count 関数のテスト。"""
    expression_data_util.empty_expression(skip_variable_name_count=False)
    expression_variables_util._save_next_variable_name_count(type_name="sp")
    next_variable_num: int = expression_variables_util._get_next_variable_num(
        type_name="sp"
    )
    assert next_variable_num == 2

    expression_variables_util._save_next_variable_name_count(type_name="sp")
    next_variable_num = expression_variables_util._get_next_variable_num(type_name="sp")
    assert next_variable_num == 3
