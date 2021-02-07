from typing import List, Tuple
from apyscript.html import html_util
from apyscript.html.html_util import _ScriptLineUtil

from tests import testing_helper


def test_remove_first_selector_symbol_char() -> None:
    str_val: str = html_util.remove_first_selector_symbol_char(
        str_val='.line-graph')
    assert str_val == 'line-graph'

    str_val = html_util.remove_first_selector_symbol_char(
        str_val='#line-graph')
    assert str_val == 'line-graph'

    str_val = html_util.remove_first_selector_symbol_char(
        str_val='line-graph')
    assert str_val == 'line-graph'


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
        '\n</html>'
    )
    result_html: str = html_util.append_indent_to_each_script_line(
        html=html, indent_num=1)
    expected_html: str = (
        '  <html>'
        '\n  </html>'
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


class Test_ScriptLineUtil:

    def test___init__(self) -> None:
        html: str = '<html>\n</html>'
        script_line_util: _ScriptLineUtil = _ScriptLineUtil(
            html=html)
        testing_helper.assert_attrs(
            expected_attrs={
                'html': html,
            },
            any_obj=script_line_util,
        )

    def test__set_script_line_ranges(self) -> None:
        html: str = (
            '<html>'
            '\n<script type="text/javascript">'
            '\nconsole.log('
            '\n  "Hello apyscript!");'
            '\n</script>'
            '\n<span>It is not in the stars to hold our destiny.</span>'
            '\n<script type="text/javascript">'
            '\nconsole.log("Hello apyscript!");'
            '\n</script>'
            '\n</html>'
        )
        script_line_util: _ScriptLineUtil = _ScriptLineUtil(html=html)
        expected: List[Tuple[int, int]] = [
            (3, 4),
            (8, 8),
        ]
        assert script_line_util.script_line_ranges == expected
