import os
import shutil
from random import randint
from typing import List, Match, Optional
import re

from retrying import retry

from apysc import Stage
from apysc import append_js_expression
from apysc import document
from apysc import save_overall_html
from apysc._expression import expression_file_util
from apysc._expression import js_functions
from apysc._expression.event_handler_scope import HandlerScope
from apysc._file import file_util
from apysc._html import exporter


@retry(stop_max_attempt_number=5, wait_fixed=300)
def test__export_js_libs() -> None:
    tmp_dir_path: str = '../.tmp_apysc_test_exporter/'
    shutil.rmtree(tmp_dir_path, ignore_errors=True)

    saved_js_file_paths: List[str] = exporter._export_js_libs(
        dest_dir_path=tmp_dir_path, skip_js_lib_exporting=False)
    for saved_js_file_path in saved_js_file_paths:
        assert os.path.isfile(saved_js_file_path)

    expected_file_path: str = os.path.join(
        tmp_dir_path, 'jquery.min.js')
    assert expected_file_path in saved_js_file_paths

    shutil.rmtree(tmp_dir_path, ignore_errors=True)

    saved_js_file_paths = exporter._export_js_libs(
        dest_dir_path=tmp_dir_path, skip_js_lib_exporting=True)
    assert saved_js_file_paths == []
    assert not os.path.exists(tmp_dir_path)


def test__append_head_to_html_str() -> None:
    html_str: str = '<html>'
    html_str = exporter._append_head_to_html_str(
        html_str=html_str, js_lib_dir_path='./',
        embed_js_libs=False)

    expected_str: str = '<html>\n<head>\n'
    assert html_str.startswith(expected_str)

    expected_str = '  <meta charset="utf-8">'
    assert expected_str in html_str

    expected_str = \
        '  <script type="text/javascript" src="./jquery.min.js"></script>'
    assert expected_str in html_str

    expected_str = '</head>'
    assert html_str.endswith(expected_str)

    html_str = exporter._append_head_to_html_str(
        html_str=html_str, js_lib_dir_path='../',
        embed_js_libs=False)
    expected_str = \
        '  <script type="text/javascript" src="../jquery.min.js"></script>'
    assert expected_str in html_str


@retry(stop_max_attempt_number=5, wait_fixed=300)
def test__append_expression_to_html_str() -> None:
    html_str: str = '<html>\n<body>'
    stage: Stage = Stage(stage_elem_id='test_stage')
    html_str = exporter._append_expression_to_html_str(
        html_str=html_str)
    assert 'id="test_stage"' in html_str
    assert f'function main_{stage.variable_name}() {{' in html_str


@retry(stop_max_attempt_number=5, wait_fixed=300)
def test_save_overall_html() -> None:
    tmp_dir_path: str = '../.tmp_apysc_test_exporter/'
    shutil.rmtree(tmp_dir_path, ignore_errors=True)
    Stage(stage_elem_id='test_stage')
    save_overall_html(
        dest_dir_path=tmp_dir_path, minify=False,
        js_lib_dir_path='../')
    expected_index_file_path: str = os.path.join(tmp_dir_path, 'index.html')
    assert os.path.isfile(expected_index_file_path)
    html_str: str = file_util.read_txt(file_path=expected_index_file_path)
    assert html_str.startswith('<html>\n<head>')
    assert html_str.endswith('\n</html>')
    assert 'id="test_stage"' in html_str
    assert 'text/javascript" src="../jquery.min.js' in html_str
    shutil.rmtree(tmp_dir_path, ignore_errors=True)

    save_overall_html(
        dest_dir_path=tmp_dir_path, minify=True)
    html_str = file_util.read_txt(file_path=expected_index_file_path)
    assert html_str.startswith('<html><head>')

    shutil.rmtree(tmp_dir_path, ignore_errors=True)
    save_overall_html(
        dest_dir_path=tmp_dir_path,
        skip_js_lib_exporting=True)
    file_names: List[str] = os.listdir(tmp_dir_path)
    for file_name in file_names:
        file_path: str = os.path.join(tmp_dir_path, file_name)
        if not os.path.isfile(file_path):
            continue
        assert not file_name.endswith('.js')

    shutil.rmtree(tmp_dir_path, ignore_errors=True)
    save_overall_html(
        dest_dir_path=tmp_dir_path,
        html_file_name='root.html')
    expected_file_path: str = os.path.join(tmp_dir_path, 'root.html')
    assert os.path.isfile(expected_file_path)

    shutil.rmtree(tmp_dir_path, ignore_errors=True)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__append_entry_point_function_call() -> None:
    stage: Stage = Stage()
    html_str: str = '<html>'
    html_str = exporter._append_entry_point_function_call(
        html_str=html_str)
    expected: str = (
        '<html>'
        '\n<script type="text/javascript">'
        f'\n$({document.variable_name}).ready(function() {{'
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


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_entry_point_func_name() -> None:
    stage: Stage = Stage()
    entry_point_func_name: str = exporter.get_entry_point_func_name()
    expected: str = f'main_{stage.variable_name}'
    assert entry_point_func_name == expected


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_var_name_from_line() -> None:
    var_name: str = exporter._get_var_name_from_line(
        line='any_value = 200;')
    assert var_name == ''

    var_name = exporter._get_var_name_from_line(
        line='var any_value = 200;')
    assert var_name == 'any_value'

    var_name = exporter._get_var_name_from_line(
        line='  var any_value = 200;')
    assert var_name == 'any_value'

    var_name = exporter._get_var_name_from_line(
        line='for (var i = 0; i < 10; i++) {')
    assert var_name == ''


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__target_js_variable_is_used() -> None:
    var_name: str = 'i_10'
    exp_lines: List[str] = [
        'var i_10 = 20;'
    ]
    result: bool = exporter._target_js_variable_is_used(
        var_name=var_name, exp_lines=exp_lines)
    assert not result

    exp_lines = [
        'var i_10 = 20;',
        'i_20 = 30;',
        'b_5 = true;',
        'i_10 = 20;',
    ]
    result = exporter._target_js_variable_is_used(
        var_name=var_name, exp_lines=exp_lines)
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__remove_unused_js_vars() -> None:
    expression: str = (
        'var i_10 = 10;'
        '\nvar i_11 = 20;'
        '\ni_10 = 20;'
        '\nvar b_5 = true;'
        '\nvar i_12 = 30;'
        '\nany_func(i_12);'
        '\nvar i_13 = i_11;'
    )
    expression = exporter._remove_unused_js_vars(expression=expression)
    expected: str = (
        'var i_10 = 10;'
        '\ni_10 = 20;'
        '\nvar i_12 = 30;'
        '\nany_func(i_12);'
    )
    assert expression == expected

    expression = (
        '\nvar s_1 = "";'
        '\ns_1 = "#00aaff";'
        '\nvar s_3 = JSON.parse(JSON.stringify(s_1));'
        '\nvar s_5 = JSON.parse(JSON.stringify(s_3));'
        '\ns_5 = "00aaff";'
    )
    result = exporter._remove_unused_js_vars(expression=expression)
    assert result == expression


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__append_common_js_functions() -> None:
    expression: str = exporter._append_common_js_functions(
        expression='console.log("Hello!");')
    assert js_functions.FUNC_COPY in expression
    assert expression.endswith('\nconsole.log("Hello!");')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__remove_blank_lines() -> None:
    expression: str = (
        'console.log("Hello!");'
        '\n'
        '\n  '
        '\nconsole.log("World!");'
    )
    expression = exporter._remove_blank_lines(expression=expression)
    expected: str = (
        'console.log("Hello!");'
        '\nconsole.log("World!");'
    )
    assert expression == expected


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__minify_html() -> None:
    html_str: str = (
        '<html>'
        '\n<body>'
        '\n  <span>a</span>'
        '\n</body>'
        '\n</html>'
    )
    html_str = exporter._minify_html(html_str=html_str, minify=False)
    assert html_str.startswith('<html>\n<body>')

    html_str = exporter._minify_html(html_str=html_str, minify=True)
    assert html_str.startswith('<html><body>')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__append_event_handler_expressions() -> None:
    expression_file_util.remove_expression_file()

    with HandlerScope():
        append_js_expression(
            expression='console.log("world!");')
    expression: str = exporter._append_event_handler_expressions(
        expression='console.log("Hello!");')
    expected: str = (
        'console.log("Hello!");'
        '\nconsole.log("world!");'
    )
    assert expression == expected


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__append_jslib_str_to_html() -> None:
    html_str: str = exporter._append_jslib_str_to_html(
        html_str='<body>',
        js_lib_dir_path='./',
        jslib_file_name='jquery.min.js',
        embed_js_libs=False)
    expected: str = (
        '<body>'
        '\n  <script type="text/javascript" src="./jquery.min.js">'
        '</script>'
    )
    assert html_str == expected

    html_str = exporter._append_jslib_str_to_html(
        html_str='<body>',
        js_lib_dir_path='./',
        jslib_file_name='jquery.min.js',
        embed_js_libs=True)
    match: Optional[Match] = re.search(
        pattern=(
            r'\<body\>'
            r'\n  \<script type="text/javascript"\>'
            r'\n  .*\/\*\! jQuery.*'
            r'\n  \</script\>'

        ),
        string=html_str,
        flags=re.MULTILINE | re.DOTALL)
    assert match is not None
