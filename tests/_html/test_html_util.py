from random import randint
from typing import Dict
from typing import List
from typing import Tuple

from retrying import retry

import apysc as ap
from apysc._expression import expression_file_util
from apysc._html import html_util
from apysc._html.html_util import ScriptLineUtil
from tests import testing_helper


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_remove_first_selector_symbol_char() -> None:
    str_val_1: str = html_util.remove_first_selector_symbol_char(
        str_val='.line-graph')
    assert str_val_1 == 'line-graph'
    assert isinstance(str_val_1, str)

    str_val_2: str = html_util.remove_first_selector_symbol_char(
        str_val='#line-graph')
    assert str_val_2 == 'line-graph'
    assert isinstance(str_val_2, str)

    str_val_3: str = html_util.remove_first_selector_symbol_char(
        str_val='line-graph')
    assert str_val_3 == 'line-graph'
    assert isinstance(str_val_3, str)

    str_val_4: ap.String = ap.String('.line-graph')
    str_val_5: ap.String = html_util.remove_first_selector_symbol_char(
        str_val=str_val_4)
    assert str_val_4.variable_name != str_val_5.variable_name
    assert str_val_5 == 'line-graph'
    assert isinstance(str_val_5, ap.String)

    testing_helper.assert_raises(
        expected_error_class=TypeError,
        func_or_method=html_util.remove_first_selector_symbol_char,
        kwargs={'str_val': 100})


def test_append_html_to_str() -> None:
    result: str = html_util.append_html_to_str(
        to_append_html='<body>',
        dest_html='<html>',
        indent_num=1)
    expected_str: str = (
        '<html>'
        '\n  <body>'
    )
    assert result == expected_str

    result = html_util.append_html_to_str(
        to_append_html='<html>',
        dest_html='',
        indent_num=0)
    assert result == '<html>'


def test_append_indent_to_each_script_line() -> None:
    html: str = (
        '<html>'
        '\n<script type="text/javascript">'
        '\nconsole.log("Hello!");'
        '\nconsole.log("World!");'
        '\n</script>'
        '\n</html>'
    )
    result_html: str = html_util.append_indent_to_each_script_line(
        html=html, indent_num=1)
    expected_html: str = (
        '<html>'
        '\n<script type="text/javascript">'
        '\n  console.log("Hello!");'
        '\n  console.log("World!");'
        '\n</script>'
        '\n</html>'
    )
    assert result_html == expected_html


def test_is_script_start_tag_line() -> None:
    result: bool = html_util.is_script_start_tag_line(
        line='<html>')
    assert not result

    result = html_util.is_script_start_tag_line(
        line='<script type="text/javascript" src="./jquery.js"></script>')
    assert not result

    result = html_util.is_script_start_tag_line(
        line='<script type="text/javascript">')
    assert result


def test_is_script_end_tag_line() -> None:
    result: bool = html_util.is_script_end_tag_line(line='<html>')
    assert not result

    result = html_util.is_script_end_tag_line(
        line='<script src="jquery.min.js"></script>')
    assert not result

    result = html_util.is_script_end_tag_line(line='</script>')
    assert result


class TestScriptLineUtil:

    _TEST_HTML: str = (
        '<html>'
        '\n<script type="text/javascript">'
        '\nconsole.log('
        '\n  "Hello apysc!");'
        '\n</script>'
        '\n<span>It is not in the stars to hold our destiny.</span>'
        '\n<script type="text/javascript">'
        '\nconsole.log("Hello apysc!");'
        '\n</script>'
        '\n</html>'
    )

    def test___init__(self) -> None:
        html: str = '<html>\n</html>'
        script_line_util: ScriptLineUtil = ScriptLineUtil(
            html=html)
        testing_helper.assert_attrs(
            expected_attrs={
                'html': html,
                'script_line_ranges': [],
            },
            any_obj=script_line_util,
        )

    def test__set_script_line_ranges(self) -> None:
        script_line_util: ScriptLineUtil = ScriptLineUtil(
            html=self._TEST_HTML)
        expected: List[Tuple[int, int]] = [
            (3, 4),
            (8, 8),
        ]
        assert script_line_util.script_line_ranges == expected

    def test_is_script_line(self) -> None:
        script_line_util: ScriptLineUtil = ScriptLineUtil(
            html=self._TEST_HTML)

        expected_values: Dict[int, bool] = {
            2: False,
            3: True,
            4: True,
            5: False,
            7: False,
            8: True,
            9: False,
        }
        for line_number, expected in expected_values.items():
            result: bool = script_line_util.is_script_line(
                line_number=line_number)
            assert result == expected


def test_wrap_expression_by_script_tag() -> None:
    expression: str = 'console.log("Hello!");'
    expression = html_util.wrap_expression_by_script_tag(
        expression=expression)
    assert expression == (
        '<script type="text/javascript">'
        '\nconsole.log("Hello!");'
        '\n</script>'
    )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__append_remove_first_selector_symbol_char_expression() -> None:
    expression_file_util.remove_expression_file()
    str_val_1: ap.String = ap.String('.line-graph')
    str_val_2: ap.String = html_util.remove_first_selector_symbol_char(
        str_val=str_val_1)
    var_name: str = str_val_2.variable_name
    expression: str = expression_file_util.get_current_expression()
    expected = f"""var first_char = {var_name}.slice(0, 1);
if (first_char === "." || first_char === "#") {{
  {var_name} = {var_name}.slice(1);
}}"""
    assert expected in expression
