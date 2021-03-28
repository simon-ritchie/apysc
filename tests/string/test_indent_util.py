from apysc.string import indent_util


def test_make_spaces_for_html() -> None:
    spaces: str = indent_util.make_spaces_for_html(indent_num=0)
    assert spaces == ''
    spaces = indent_util.make_spaces_for_html(indent_num=1)
    assert spaces == '  '
    spaces = indent_util.make_spaces_for_html(indent_num=2)
    assert spaces == '    '


def test_append_spaces_to_expression() -> None:
    expression: str = (
        'console.log("Hello!");'
        '\nconsole.log("World!");'
    )
    result_expression: str = indent_util.append_spaces_to_expression(
        expression=expression, indent_num=0)
    assert result_expression == expression

    result_expression = indent_util.append_spaces_to_expression(
        expression=expression, indent_num=2)
    expected: str = (
        '    console.log("Hello!");'
        '\n    console.log("World!");'
    )
    assert result_expression == expected
