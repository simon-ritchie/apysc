import os
import shutil
from random import randint
from typing import List

from retrying import retry

from apyscript.display.stage import Stage
from apyscript.file import file_util
from apyscript.html import exporter


@retry(stop_max_attempt_number=5, wait_fixed=300)
def test__export_js_libs() -> None:
    tmp_dir_path: str = '../.tmp_action_py_script_test_exporter/'
    shutil.rmtree(tmp_dir_path, ignore_errors=True)

    saved_js_file_paths: List[str] = exporter._export_js_libs(
        dest_dir_path=tmp_dir_path)
    for saved_js_file_path in saved_js_file_paths:
        assert os.path.isfile(saved_js_file_path)

    expected_file_path: str = os.path.join(
        tmp_dir_path, 'jquery.min.js')
    assert expected_file_path in saved_js_file_paths

    shutil.rmtree(tmp_dir_path, ignore_errors=True)


def test__append_head_to_html_str() -> None:
    html_str: str = '<html>'
    html_str = exporter._append_head_to_html_str(html_str=html_str)

    expected_str: str = '<html>\n<head>\n'
    assert html_str.startswith(expected_str)

    expected_str = '  <meta charset="utf-8">'
    assert expected_str in html_str

    expected_str = \
        '  <script type="text/javascript" src="./jquery.min.js"></script>'
    assert expected_str in html_str

    expected_str = '</head>'
    assert html_str.endswith(expected_str)


@retry(stop_max_attempt_number=5, wait_fixed=300)
def test__append_expression_to_html_str() -> None:
    html_str: str = '<html>\n<body>'
    stage: Stage = Stage(stage_elem_id='test_stage')
    html_str = exporter._append_expression_to_html_str(
        html_str=html_str)
    assert 'id="test_stage"' in html_str
    assert f'function main_{stage.variable_name}() {{' in html_str


@retry(stop_max_attempt_number=5, wait_fixed=300)
def test_save_expressions_overall_html() -> None:
    tmp_dir_path: str = '../.tmp_action_py_script_test_exporter/'
    shutil.rmtree(tmp_dir_path, ignore_errors=True)
    Stage(stage_elem_id='test_stage')
    exporter.save_expressions_overall_html(dest_dir_path=tmp_dir_path)
    expected_index_file_path: str = os.path.join(tmp_dir_path, 'index.html')
    assert os.path.isfile(expected_index_file_path)
    html_str: str = file_util.read_txt(file_path=expected_index_file_path)
    assert html_str.startswith('<html>\n<head>')
    assert html_str.endswith('\n</html>')
    assert 'id="test_stage"' in html_str

    shutil.rmtree(tmp_dir_path, ignore_errors=True)


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test__append_entry_point_function_call() -> None:
    stage: Stage = Stage()
    html_str: str = '<html>'
    html_str = exporter._append_entry_point_function_call(
        html_str=html_str)
    expected: str = (
        '<html>'
        '\n<script type="text/javascript">'
        '\n$(document).ready(function() {'
        f'\n  main_{stage.variable_name}();'
        '\n});'
        '\n</script>'
    )
    assert html_str == expected


@retry(stop_max_attempt_number=5, wait_fixed=300)
def test__append_stage_global_variable_to_html() -> None:
    Stage(stage_elem_id='test_stage')
    html_str: str = '<html>'
    html_str = exporter._append_stage_global_variable_to_html(
        html_str=html_str)
    expected: str = (
        '<html>'
        '\n<script type="text/javascript">'
        '\nvar test_stage;'
        '\n</script>'
    )
    assert html_str == expected


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_get_entry_point_func_name() -> None:
    stage: Stage = Stage()
    entry_point_func_name: str = exporter.get_entry_point_func_name()
    expected: str = f'main_{stage.variable_name}'
    assert entry_point_func_name == expected
