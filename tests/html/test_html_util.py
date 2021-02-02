from apyscript.html import html_util


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


def test_add_html_to_str() -> None:
    result: str = html_util.add_html_to_str(
        to_append_html='<body>',
        dest_html='<html>',
        indent_num=1)
    expected_str: str = (
        '<html>'
        '\n  <body>'
    )
    assert result == expected_str

    result = html_util.add_html_to_str(
        to_append_html='<html>',
        dest_html='',
        indent_num=0)
    assert result == '<html>'
