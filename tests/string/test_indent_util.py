from apyscript.string import indent_util


def test_make_spaces_for_html() -> None:
    spaces: str = indent_util.make_spaces_for_html(indent_num=0)
    assert spaces == ''
    spaces = indent_util.make_spaces_for_html(indent_num=1)
    assert spaces == '  '
    spaces = indent_util.make_spaces_for_html(indent_num=2)
    assert spaces == '    '
