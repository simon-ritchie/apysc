import os

from apyscript.expression import expression_file


def test_empty_expression_dir() -> None:
    os.makedirs(expression_file.EXPRESSION_ROOT_DIR)
    test_file_path: str = os.path.join(
        expression_file.EXPRESSION_ROOT_DIR,
        'test_file.txt',
    )
    with open(test_file_path, 'w') as f:
        f.write('\n')
    expression_file.empty_expression_dir()
    assert not os.path.exists(expression_file.EXPRESSION_ROOT_DIR)
