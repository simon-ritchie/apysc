import os

from apyscript.expression import expression_file


def test_empty_expression_dir() -> None:
    os.makedirs(expression_file.EXPRESSION_ROOT_DIR, exist_ok=True)
    test_file_path: str = os.path.join(
        expression_file.EXPRESSION_ROOT_DIR,
        'test_file.txt',
    )
    with open(test_file_path, 'w') as f:
        f.write('\n')
    expression_file.empty_expression_dir()
    assert not os.path.exists(test_file_path)
    assert os.path.exists(expression_file.EXPRESSION_ROOT_DIR)


def test_append_expression() -> None:
    expression_file.empty_expression_dir()

    expected_expression_1: str = (
        '<script>console.log("test")</script>'
    )
    expected_expression_2: str = '<span>test</span>'
    expression_file.append_expression(expression=expected_expression_1)
    expression_file.append_expression(
        expression=expected_expression_2,
        scope=expression_file.ROOT_SCOPE)
    root_scope_file_path:str = os.path.join(
        expression_file.EXPRESSION_ROOT_DIR,
        f'{expression_file.ROOT_SCOPE}.html',
    )
    with open(root_scope_file_path, 'r') as f:
        scope_txt: str = f.read()
    expected_str: str = (
        f'{expected_expression_1}\n{expected_expression_2}\n'
    )
    print(scope_txt)
    print(expected_str)
    assert scope_txt == expected_str

    expression_file.empty_expression_dir()
