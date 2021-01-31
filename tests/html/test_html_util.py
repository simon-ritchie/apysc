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
