import hashlib
import os
import shutil
from random import randint
from typing import List
from typing import Optional

from retrying import retry

import scripts.build_docs as build_docs
from apysc._file import file_util
from apysc._string.docstring_util import _DOCSTRING_PATH_COMMENT_KEYWORD
from scripts.build_docs import HASHED_VALS_DIR_PATH
from scripts.build_docs import _CodeBlock
from scripts.build_docs import _CodeBlockFlake8Error
from scripts.build_docs import _CodeBlockMypyError
from scripts.build_docs import _CodeBlockNumdoclintError
from scripts.build_docs import _MarkdownData
from scripts.build_docs import _RunReturnData
from scripts.build_docs import _ScriptData
from tests.testing_helper import assert_attrs
from tests.testing_helper import assert_raises
from apysc._lint_and_doc import lint_and_doc_hash_util

_CHECKOUT_FILE_PATHS: List[str] = [
    'docs_src/hashed_vals/stage.md',
]


def teardown() -> None:
    """
    The function would be called when the test ended.
    """
    for checkout_file_path in _CHECKOUT_FILE_PATHS:
        os.system(f'git checkout {checkout_file_path}')


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
        f.write('"_static/groundwork.css"')
    pkl_path: str = os.path.join(tmp_dir_1, 'test.pkl')
    with open(pkl_path, 'w') as f:
        f.write('')
    jslib_path: str = os.path.join(tmp_dir_1, 'jquery.min.js')
    with open(jslib_path, 'w') as f:
        f.write('"_static/groundwork.css"')

    build_docs._replace_static_path_recursively(dir_path=tmp_dir_1)
    target_file_paths: List[str] = [html_path, js_path]
    for target_file_path in target_file_paths:
        with open(target_file_path) as f:
            file_txt: str = f.read()
        assert '_static' not in file_txt
        assert 'static' in file_txt

    with open(jslib_path) as f:
        file_txt = f.read()
        assert '_static' in file_txt

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
from apysc import save_overall_html

stage = Stage(stage_width=300, stage_height=180, background_color='#333')
save_overall_html(
    dest_dir_path='./quick_start_stage_creation')"""
    code = build_docs._replace_html_saving_export_path_by_doc_path(code=code)
    expected: str = """save_overall_html(
    dest_dir_path='./docs_src/source/_static/quick_start_stage_creation/')"""
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
save_overall_html(
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
         '\nsave_overall_html('
         "\n    dest_dir_path='./docs_src/source/_static/"
         "quick_start_stage_creation/',"
         "\n    js_lib_dir_path='../', skip_js_lib_exporting=True)"
         ]
    )

    file_util.remove_file_if_exists(file_path=tmp_md_file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__exec_document_lint_and_script() -> None:
    hash_file_path: str = os.path.join(
        build_docs.HASHED_VALS_DIR_PATH,
        'quick_start.md',
    )
    file_util.remove_file_if_exists(file_path=hash_file_path)

    executed_scripts: List[str] = build_docs._exec_document_lint_and_script(
        limit_count=10)
    assert len(executed_scripts) <= 10
    for executed_script in executed_scripts:
        if 'save_overall_html' not in executed_script:
            continue
        assert './docs_src/source/_static/' in executed_script


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__remove_runnable_inline_comment_from_code_blocks() -> None:
    tmp_dir_path: str = '../tmp_test_build_docs/'
    shutil.rmtree(tmp_dir_path, ignore_errors=True)
    tmp_subdir_path: str = os.path.join(tmp_dir_path, 'subdir/')
    os.makedirs(tmp_subdir_path)
    tmp_html_path_1: str = os.path.join(tmp_dir_path, 'tmp_1.html')
    tmp_html_path_2: str = os.path.join(tmp_subdir_path, 'tmp_2.html')
    tmp_txt_path_1: str = os.path.join(tmp_dir_path, 'tmp_1.txt')
    html_txt: str = (
        '<span>a</span>'
        '<span></span><span class="c1"># runnable</span>'
        '\n<span>b</span>'
    )
    for file_path in (tmp_html_path_1, tmp_html_path_2, tmp_txt_path_1):
        with open(file_path, 'w') as f:
            f.write(html_txt)
    build_docs._remove_runnable_inline_comment_from_code_blocks(
        dir_path=tmp_dir_path)
    expected: str = (
        '<span>a</span>'
        '\n<span>b</span>'
    )
    for file_path in (tmp_html_path_1, tmp_html_path_2):
        with open(file_path) as f:
            txt: str = f.read()
        assert txt == expected
    with open(tmp_txt_path_1) as f:
        txt = f.read()
        assert txt == html_txt

    shutil.rmtree(tmp_dir_path, ignore_errors=True)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__read_md_file_hashed_val_from_file() -> None:
    tmp_hash_file_path: str = '../tmp_test_build_docs_1.md'
    file_util.remove_file_if_exists(file_path=tmp_hash_file_path)
    hashed_val: str = build_docs._read_md_file_hashed_val_from_file(
        hash_file_path=tmp_hash_file_path)
    assert hashed_val == ''

    file_util.save_plain_txt(txt='1234567890', file_path=tmp_hash_file_path)
    hashed_val = build_docs._read_md_file_hashed_val_from_file(
        hash_file_path=tmp_hash_file_path)
    assert hashed_val == '1234567890'
    file_util.remove_file_if_exists(file_path=tmp_hash_file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__read_file_and_hash_it() -> None:
    tmp_file_path: str = '../test_build_docs_2.md'
    file_util.save_plain_txt(
        txt='1234567890', file_path=tmp_file_path)
    hashed_val: str = build_docs._read_file_and_hash_it(
        file_path=tmp_file_path)
    assert hashed_val == hashlib.sha1('1234567890'.encode()).hexdigest()


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_md_under_source_file_path() -> None:
    under_source_file_path: str = build_docs._get_md_under_source_file_path(
        md_file_path='./doc_src/source/any/path.md')
    assert under_source_file_path == 'any/path.md'


def test__save_md_hashed_val() -> None:
    original_hashed_vals_dir_path: str = build_docs.HASHED_VALS_DIR_PATH
    build_docs.HASHED_VALS_DIR_PATH = '../tmp_test_build_docs_5/hashed_vals/'
    expected_file_path: str = os.path.join(
        build_docs.HASHED_VALS_DIR_PATH,
        'any/path.md')
    file_util.remove_file_if_exists(file_path=expected_file_path)
    build_docs._save_md_hashed_val(
        md_file_path='./docs_src/source/any/path.md', hashed_val='1234')
    hashed_val: str = build_docs._read_md_file_hashed_val_from_file(
        hash_file_path=expected_file_path)
    assert hashed_val == '1234'

    build_docs.HASHED_VALS_DIR_PATH = original_hashed_vals_dir_path
    file_util.remove_file_if_exists(file_path=expected_file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__append_js_lib_path_and_skip_settings() -> None:
    """_append_js_lib_path_and_skip_settings 関数のテスト。
    """
    code: str = """print(200)
save_overall_html(
    dest_dir_path='quick_start_stage_creation/')"""
    code = build_docs._append_js_lib_path_and_skip_settings(
        code=code)
    expected: str = """print(200)
save_overall_html(
    dest_dir_path='quick_start_stage_creation/',
    js_lib_dir_path='../', skip_js_lib_exporting=True)"""
    assert code == expected


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__make_script_data_list() -> None:
    os.makedirs('./tmp/', exist_ok=True)
    tmp_file_path_1: str = './tmp/tmp_test_build_docs_1.md'
    tmp_file_path_2: str = './tmp/tmp_test_build_docs_2.md'
    with open(tmp_file_path_1, 'w') as f:
        f.write(
            '# heading'
            '\n\n```py'
            '\n# runnable'
            '\nprint(100)'
            '\n```'
            '\n\n```py'
            '\n# runnable'
            '\nprint(200)'
            '\n```'
            '\n'
        )
    with open(tmp_file_path_2, 'w') as f:
        f.write(
            '# heading'
            '\n\n```py'
            '\n# runnable'
            '\nprint(300)'
            '\n```'
            '\n'
        )
    markdown_data_list: List[_MarkdownData] = [{
        'md_file_path': tmp_file_path_1,
        'hashed_val': 'abc',
    }, {
        'md_file_path': tmp_file_path_2,
        'hashed_val': 'def',
    }]
    script_data_list: List[_ScriptData] = build_docs._make_script_data_list(
        markdown_data_list=markdown_data_list,
        limit_count=None)
    assert len(script_data_list) == 3
    assert script_data_list[0] == {
        'md_file_path': tmp_file_path_1,
        'hashed_val': 'abc',
        'runnable_script': 'print(100)',
    }
    assert script_data_list[1] == {
        'md_file_path': tmp_file_path_1,
        'hashed_val': 'abc',
        'runnable_script': 'print(200)',
    }
    assert script_data_list[2] == {
        'md_file_path': tmp_file_path_2,
        'hashed_val': 'def',
        'runnable_script': 'print(300)',
    }

    script_data_list = build_docs._make_script_data_list(
        markdown_data_list=markdown_data_list,
        limit_count=2)
    assert len(script_data_list) == 2

    file_util.remove_file_if_exists(file_path=tmp_file_path_1)
    file_util.remove_file_if_exists(file_path=tmp_file_path_2)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__run_code_block_script() -> None:
    return_data: _RunReturnData = build_docs._run_code_block_script(
        script_data={
            'md_file_path': 'test.md',
            'hashed_val': 'abc',
            'runnable_script': 'print(200)',
        })
    assert return_data == {
        'md_file_path': 'test.md',
        'runnable_script': 'print(200)',
        'stdout': '200\n',
    }


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__validate_script_return_data() -> None:
    build_docs._validate_script_return_data(
        return_data_list=[{
            'md_file_path': 'test.md',
            'runnable_script': 'print(100)',
            'stdout': '100\n',
        }])

    assert_raises(
        expected_error_class=Exception,
        func_or_method=build_docs._validate_script_return_data,
        kwargs={'return_data_list': [{
            'md_file_path': 'test.md',
            'runnable_script': 'print(100)',
            'stdout': 'Traceback: most recent call ...'
        }]},
        match='Error occurred while executing the document codeblock.')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__save_hashed_val() -> None:
    hashed_val: str = build_docs._read_md_file_hashed_val_from_file(
        hash_file_path='docs_src/hashed_vals/stage.md')
    os.remove('docs_src/hashed_vals/stage.md')
    build_docs._save_hashed_val(
        script_data_list=[{
            'md_file_path': 'docs_src/source/stage.md',
            'hashed_val': hashed_val,
            'runnable_script': 'print(100)',
        }])
    saved_hashed_val: str = build_docs._read_md_file_hashed_val_from_file(
        hash_file_path='docs_src/hashed_vals/stage.md')
    assert saved_hashed_val == hashed_val


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__check_code_block_with_flake8() -> None:
    script_data: _ScriptData = {
        'md_file_path': './tmp.py',
        'hashed_val': 'abc',
        'runnable_script':
        'a=10',
    }
    assert_raises(
        expected_error_class=_CodeBlockFlake8Error,
        func_or_method=build_docs._check_code_block_with_flake8,
        kwargs={'script_data': script_data},
        match=r'There is a flake8 error in the following document '
              r'code block:')

    script_data = {
        'md_file_path': './tmp.py',
        'hashed_val': 'abc',
        'runnable_script': 'a = 20',
    }
    build_docs._check_code_block_with_flake8(script_data=script_data)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__check_code_block_with_numdoclint() -> None:
    script_data: _ScriptData = {
        'md_file_path': './tmp.py',
        'hashed_val': 'abc',
        'runnable_script':
        'def func_1'
        '(a):\n    print(100)',
    }
    assert_raises(
        expected_error_class=_CodeBlockNumdoclintError,
        func_or_method=build_docs._check_code_block_with_numdoclint,
        kwargs={'script_data': script_data},
        match=r'There is a numdoclint error in the following '
              r'document code block')

    script_data = {
        'md_file_path': './tmp.py',
        'hashed_val': 'abc',
        'runnable_script':
        'def func_2'
        '(a):'
        '\n    """'
        '\n    test function.'
        '\n\n    Parameters'
        '\n    ----------'
        '\n    a : int'
        '\n        Test argument.'
        '\n    """'
        '\n    print(100)',
    }
    build_docs._check_code_block_with_numdoclint(script_data=script_data)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__check_code_block_with_mypy() -> None:
    script_data: _ScriptData = {
        'md_file_path': './tmp.py',
        'hashed_val': 'abc',
        'runnable_script':
        'def func_1'
        '(a):\n    print(100)',
    }
    assert_raises(
        expected_error_class=_CodeBlockMypyError,
        func_or_method=build_docs._check_code_block_with_mypy,
        kwargs={'script_data': script_data},
        match='There is a mypy error in the following document code block')

    script_data = {
        'md_file_path': './tmp.py',
        'hashed_val': 'abc',
        'runnable_script': 'print(100)',
    }
    build_docs._check_code_block_with_mypy(script_data=script_data)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_code_block_output_dir_paths() -> None:
    tmp_test_dir_path: str = 'tmp/test_build_docs_1/'
    shutil.rmtree(tmp_test_dir_path, ignore_errors=True)
    dir_paths: List[str] = build_docs._get_code_block_output_dir_paths(
        output_dir_path=tmp_test_dir_path)
    assert dir_paths == []

    tmp_subdir_path_1: str = os.path.join(
        tmp_test_dir_path, 'test_1/')
    os.makedirs(tmp_subdir_path_1, exist_ok=True)
    tmp_subdir_path_2: str = os.path.join(
        tmp_test_dir_path, 'test_2/')
    os.makedirs(tmp_subdir_path_2, exist_ok=True)
    tmp_index_path: str = os.path.join(
        tmp_subdir_path_2, 'index.html',
    )
    with open(tmp_index_path, 'w') as f:
        f.write('')
    tmp_static_file_path: str = os.path.join(
        tmp_test_dir_path, 'tmp_test.js')
    with open(tmp_static_file_path, 'w') as f:
        f.write('')
    dir_paths = build_docs._get_code_block_output_dir_paths(
        output_dir_path=tmp_test_dir_path)
    assert dir_paths == ['tmp/test_build_docs_1/test_2/']

    shutil.rmtree(tmp_test_dir_path, ignore_errors=True)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__move_code_block_outputs() -> None:
    tmp_test_dir_path: str = 'tmp/test_build_docs_2/'
    shutil.rmtree(tmp_test_dir_path, ignore_errors=True)
    tmp_subdir_path: str = os.path.join(
        tmp_test_dir_path, 'tmp_test_build_docs/')
    os.makedirs(tmp_subdir_path, exist_ok=True)
    tmp_index_path: str = os.path.join(tmp_subdir_path, 'index.html')
    with open(tmp_index_path, 'w') as f:
        f.write('')
    expected_dir_path: str = './docs/static/tmp_test_build_docs/'
    expected_file_path: str = os.path.join(
        expected_dir_path, 'index.html',
    )
    shutil.rmtree(expected_dir_path, ignore_errors=True)
    build_docs._move_code_block_outputs(
        output_dir_path=tmp_test_dir_path)
    assert os.path.isfile(expected_file_path)
    assert not os.path.isdir(tmp_subdir_path)

    shutil.rmtree(tmp_test_dir_path, ignore_errors=True)
    shutil.rmtree(expected_dir_path, ignore_errors=True)


def test__convert_path_to_markdown_data_with_hashed_val() -> None:
    test_md_file_path: str = './docs_src/source/test_build_docs.md'
    with open(test_md_file_path, 'w') as f:
        f.write('Hello')

    markdown_data: Optional[_MarkdownData] = build_docs.\
        _convert_path_to_markdown_data_with_hashed_val(
            md_file_path='./docs_src/hashed_vals/test_build_docs.md')
    assert markdown_data is None

    under_source_file_path: str = build_docs._get_md_under_source_file_path(
        md_file_path=test_md_file_path)
    hash_file_path: str = os.path.join(
        HASHED_VALS_DIR_PATH,
        under_source_file_path,
    )
    expected_md_hashed_val: str = build_docs._read_file_and_hash_it(
        file_path=test_md_file_path)
    file_util.remove_file_if_exists(file_path=hash_file_path)
    markdown_data = build_docs._convert_path_to_markdown_data_with_hashed_val(
        md_file_path=test_md_file_path)
    assert markdown_data == {
        'md_file_path': test_md_file_path,
        'hashed_val': expected_md_hashed_val,
    }

    with open(hash_file_path, 'w') as f:
        f.write(expected_md_hashed_val)
    markdown_data = build_docs._convert_path_to_markdown_data_with_hashed_val(
        md_file_path=test_md_file_path)
    assert markdown_data is None

    file_util.remove_file_if_exists(file_path=test_md_file_path)
    file_util.remove_file_if_exists(file_path=hash_file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__remove_none_from_markdown_data_list() -> None:
    markdown_data_list: List[Optional[_MarkdownData]] = [
        {
            'md_file_path': 'test_path.md',
            'hashed_val': 'abc',
        },
        None,
    ]
    markdown_data_list_: List[_MarkdownData] = build_docs.\
        _remove_none_from_markdown_data_list(
            markdown_data_list=markdown_data_list)
    assert markdown_data_list_ == [{
        'md_file_path': 'test_path.md',
        'hashed_val': 'abc',
    }]


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__replace_docstring_specification() -> None:
    tmp_dir_path: str = './tmp/'
    os.makedirs(tmp_dir_path, exist_ok=True)
    tmp_file_path: str = os.path.join(
        tmp_dir_path, 'test_build_docs.md',
    )
    file_util.save_plain_txt(
        txt=(
            '# Test document'
            '\n\nLorem ipsum dolor sit amet.'
            '\n\n## Constructor API'
            f'\n\n<!-- {_DOCSTRING_PATH_COMMENT_KEYWORD} '
            'apysc._display.sprite.Sprite.__init__ -->'
        ),
        file_path=tmp_file_path)
    build_docs._replace_docstring_specification(
        markdown_data={
            'md_file_path': tmp_file_path,
            'hashed_val': 'abc',
        })

    file_util.remove_file_if_exists(file_path=tmp_file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_doc_hash_file_path() -> None:
    hash_file_path: str = build_docs._get_doc_hash_file_path(
        md_file_path='./doc_src/source/any/path.md')
    assert hash_file_path == './docs_src/hashed_vals/any/path.md'
