from random import randint
import os
import shutil
from typing import List

from retrying import retry

import build_docs
from build_docs import _CodeBlock
from tests.testing_helper import assert_attrs
from apysc.file import file_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
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


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
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


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__replace_html_saving_export_path_by_doc_path() -> None:
    code: str = """from apysc import Stage
from apysc import save_expressions_overall_html

stage = Stage(stage_width=300, stage_height=180, background_color='#333')
save_expressions_overall_html(
    dest_dir_path='./quick_start_stage_creation')"""
    code = build_docs._replace_html_saving_export_path_by_doc_path(code=code)
    expected: str = """save_expressions_overall_html(
    dest_dir_path='./docs_src/_static/quick_start_stage_creation/')"""
    assert expected in code


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_runnable_scripts_in_md_code_blocks() -> None:
    tmp_md_file_path: str = (
        '../tmp_test__get_runnable_scripts_in_md_code_blocks.md')
    md_txt: str = """Hello

```py
print(100)
```

World!

```py
# runnable
print(200)
save_expressions_overall_html(
    dest_dir_path='quick_start_stage_creation/')
```

```
# runnable
print(300)
```
"""
    with open(tmp_md_file_path, 'w') as f:
        f.write(md_txt)
    runnable_scripts: List[str] = \
        build_docs._get_runnable_scripts_in_md_code_blocks(
            md_file_path=tmp_md_file_path)
    assert len(runnable_scripts) == 1
    assert runnable_scripts == (
        ['print(200)'
         '\nsave_expressions_overall_html('
         "\n    dest_dir_path='./docs_src/_static/"
         "quick_start_stage_creation/')"
        ]
    )

    file_util.remove_file_if_exists(file_path=tmp_md_file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__exec_document_script() -> None:
    executed_scripts: List[str] = build_docs._exec_document_script(
        limit_count=10)
    assert len(executed_scripts) == 1
    for executed_script in executed_scripts:
        if 'save_expressions_overall_html' not in executed_script:
            continue
        assert './docs_src/_static/' in executed_script
