import os
import shutil
from typing import List

import build_docs
from build_docs import _CodeBlock
from tests.testing_helper import assert_attrs


def test__replace_static_path_recursively() -> None:
    tmp_dir_1: str = '../.tmp_test_build_docs/'
    shutil.rmtree(tmp_dir_1, ignore_errors=True)
    tmp_dir_2: str = os.path.join(tmp_dir_1, 'subdir/')
    os.makedirs(tmp_dir_2, exist_ok=True)

    html_path: str = os.path.join(tmp_dir_1, 'test.html')
    with open(html_path, 'w') as f:
        f.write(
            '<link rel="stylesheet" type="text/css" '
            'href="_static/groundwork.css" />')
    js_path: str = os.path.join(tmp_dir_2, 'test.js')
    with open(js_path, 'w') as f:
        f.write('""_static/groundwork.css""')
    pkl_path: str = os.path.join(tmp_dir_1, 'test.pkl')
    with open(pkl_path, 'w') as f:
        f.write('')

    build_docs._replace_static_path_recursively(dir_path=tmp_dir_1)
    target_file_paths: List[str] = [html_path, js_path]
    for target_file_path in target_file_paths:
        with open(target_file_path) as f:
            file_txt: str = f.read()
        assert '_static' not in file_txt
        assert 'static' in file_txt

    shutil.rmtree(tmp_dir_1, ignore_errors=True)


class Test_CodeBlock:

    def test___init__(self) -> None:
        code_block: _CodeBlock = _CodeBlock(
            code_type='py', code='print(100)', runnable=True)
        assert_attrs(
            expected_attrs={
                'code_type': 'py',
                'code': 'print(100)',
                'runnable': True
            },
            any_obj=code_block)


def test__get_code_blocks_from_txt() -> None:
    md_txt: str = (
        'Hello'
        '\n\n```py'
        '\nprint(100)'
        '\nprint(200)'
        '\n```'
        '\n\nWorld'
        '\n```py'
        '\n# runnable'
        '\nprint(300)'
        '\n```'
        '\n'
        '\n```'
        '\n$ ls -l'
        '\n```'
    )
    code_blocks: List[_CodeBlock] = build_docs._get_code_blocks_from_txt(
        md_txt=md_txt)
    assert len(code_blocks) == 3

    assert code_blocks[0].code_type == 'py'
    assert code_blocks[0].code == 'print(100)\nprint(200)'
    assert not code_blocks[0].runnable

    assert code_blocks[1].code == 'print(300)'
    assert code_blocks[1].runnable

    assert code_blocks[2].code_type == ''
    assert code_blocks[2].code == '$ ls -l'
    assert not code_blocks[2].runnable
