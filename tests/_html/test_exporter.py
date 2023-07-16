import os
import re
import shutil
from typing import List
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import js_functions
from apysc._expression.event_handler_scope import HandlerScope
from apysc._file import file_util
from apysc._html import exporter
from apysc._jslib import jslib_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn


@apply_test_settings(retrying_sleep_seconds=0.3)
def test__export_js_libs() -> None:
    jquery_file_name: str = jslib_util.get_jquery_file_name()
    tmp_dir_path: str = "../.tmp_apysc_test_exporter/"
    shutil.rmtree(tmp_dir_path, ignore_errors=True)

    saved_js_file_paths: List[str] = exporter._export_js_libs(
        dest_dir_path=tmp_dir_path, skip_js_lib_exporting=False
    )
    for saved_js_file_path in saved_js_file_paths:
        assert os.path.isfile(saved_js_file_path)

    expected_file_path: str = os.path.join(tmp_dir_path, jquery_file_name)
    assert expected_file_path in saved_js_file_paths

    shutil.rmtree(tmp_dir_path, ignore_errors=True)

    saved_js_file_paths = exporter._export_js_libs(
        dest_dir_path=tmp_dir_path, skip_js_lib_exporting=True
    )
    assert saved_js_file_paths == []
    assert not os.path.exists(tmp_dir_path)


def test__append_head_to_html_str() -> None:
    html_str: str = "<html>"
    html_str = exporter._append_head_to_html_str(
        html_str=html_str, js_lib_dir_path="./", embed_js_libs=False
    )
    jquery_file_name: str = jslib_util.get_jquery_file_name()

    expected_str: str = "<html>\n<head>\n"
    assert html_str.startswith(expected_str)

    expected_str = '  <meta charset="utf-8">'
    assert expected_str in html_str

    expected_str = (
        f'  <script type="text/javascript" src="./{jquery_file_name}"></script>'
    )
    assert expected_str in html_str

    expected_str = "</head>"
    assert html_str.endswith(expected_str)

    html_str = exporter._append_head_to_html_str(
        html_str=html_str, js_lib_dir_path="../", embed_js_libs=False
    )
    expected_str = (
        f'  <script type="text/javascript" src="../{jquery_file_name}"></script>'
    )
    assert expected_str in html_str


@apply_test_settings(retrying_sleep_seconds=0.3)
def test__append_expression_to_html_str() -> None:
    html_str: str = "<html>\n<body>"
    stage: ap.Stage = ap.Stage(stage_elem_id="test_stage")
    html_str = exporter._append_expression_to_html_str(html_str=html_str, verbose=1)
    assert 'id="test_stage"' in html_str
    assert f"function main_{stage.variable_name}() {{" in html_str


@apply_test_settings(retrying_sleep_seconds=0.3)
def test_save_overall_html() -> None:
    jquery_file_name: str = jslib_util.get_jquery_file_name()
    tmp_dir_path: str = "../.tmp_apysc_test_exporter/"
    shutil.rmtree(tmp_dir_path, ignore_errors=True)
    ap.Stage(stage_elem_id="test_stage")
    ap.save_overall_html(
        dest_dir_path=tmp_dir_path, minify=False, js_lib_dir_path="../"
    )
    expected_index_file_path: str = os.path.join(tmp_dir_path, "index.html")
    assert os.path.isfile(expected_index_file_path)
    html_str: str = file_util.read_txt(file_path=expected_index_file_path)
    assert html_str.startswith("<html>\n<head>")
    assert html_str.endswith("\n</html>")
    assert 'id="test_stage"' in html_str
    assert f'text/javascript" src="../{jquery_file_name}' in html_str
    shutil.rmtree(tmp_dir_path, ignore_errors=True)

    ap.save_overall_html(dest_dir_path=tmp_dir_path, minify=True)
    html_str = file_util.read_txt(file_path=expected_index_file_path)
    assert html_str.startswith("<html><head>")

    shutil.rmtree(tmp_dir_path, ignore_errors=True)
    ap.save_overall_html(dest_dir_path=tmp_dir_path, skip_js_lib_exporting=True)
    file_names: List[str] = os.listdir(tmp_dir_path)
    for file_name in file_names:
        file_path: str = os.path.join(tmp_dir_path, file_name)
        if not os.path.isfile(file_path):
            continue
        assert not file_name.endswith(".js")

    shutil.rmtree(tmp_dir_path, ignore_errors=True)
    ap.save_overall_html(dest_dir_path=tmp_dir_path, html_file_name="root.html")
    expected_file_path: str = os.path.join(tmp_dir_path, "root.html")
    assert os.path.isfile(expected_file_path)

    shutil.rmtree(tmp_dir_path, ignore_errors=True)


@apply_test_settings()
def test__append_entry_point_function_call() -> None:
    stage: ap.Stage = ap.Stage()
    html_str: str = "<html>"
    html_str = exporter._append_entry_point_function_call(html_str=html_str)
    expected: str = (
        "<html>"
        '\n<script type="text/javascript">'
        f"\n$({ap.document.variable_name}).ready(function() {{"
        f"\n  main_{stage.variable_name}();"
        "\n});"
        "\n</script>"
    )
    assert html_str == expected


@apply_test_settings(retrying_sleep_seconds=0.3)
def test__append_stage_global_variable_to_html() -> None:
    ap.Stage(stage_elem_id="test_stage")
    html_str: str = "<html>"
    html_str = exporter._append_stage_global_variable_to_html(html_str=html_str)
    expected: str = (
        "<html>" '\n<script type="text/javascript">' "\nvar test_stage;" "\n</script>"
    )
    assert html_str == expected


@apply_test_settings(retrying_sleep_seconds=0.5)
def test_get_entry_point_func_name() -> None:
    stage: ap.Stage = ap.Stage()
    entry_point_func_name: str = exporter.get_entry_point_func_name()
    expected: str = f"main_{stage.variable_name}"
    assert entry_point_func_name == expected


@apply_test_settings()
def test__get_var_name_from_line() -> None:
    var_name: str = exporter._get_var_name_from_line(line="any_value = 200;")
    assert var_name == ""

    var_name = exporter._get_var_name_from_line(line="var any_value = 200;")
    assert var_name == "any_value"

    var_name = exporter._get_var_name_from_line(line="  var any_value = 200;")
    assert var_name == "any_value"

    var_name = exporter._get_var_name_from_line(line="for (var i = 0; i < 10; i++) {")
    assert var_name == ""


@apply_test_settings()
def test__target_js_variable_is_used() -> None:
    var_name: str = "i_10"
    exp_lines: List[str] = ["// i_10 info", "var i_10 = 20;"]
    result: bool = exporter._target_js_variable_is_used(
        var_name=var_name, exp_lines=exp_lines
    )
    assert not result

    exp_lines = [
        "// any info.",
        "var i_10 = 20;",
        "i_20 = 30;",
        "b_5 = true;",
        "i_10 = 20;",
    ]
    result = exporter._target_js_variable_is_used(
        var_name=var_name, exp_lines=exp_lines
    )
    assert result

    exp_lines = ["var i_10 = 20;", "var dict_val = {", '  "a": i_10', "}"]
    result = exporter._target_js_variable_is_used(
        var_name=var_name, exp_lines=exp_lines
    )
    assert result


@apply_test_settings()
def test__remove_unused_js_vars() -> None:
    expression: str = (
        "var i_10 = 10;"
        "\nvar i_11 = 20;"
        "\ni_10 = 20;"
        "\nvar b_5 = true;"
        "\nvar i_12 = 30;"
        "\nany_func(i_12);"
        "\nvar i_13 = i_11;"
    )
    expression = exporter._remove_unused_js_vars(expression=expression)
    expected: str = (
        "var i_10 = 10;" "\ni_10 = 20;" "\nvar i_12 = 30;" "\nany_func(i_12);"
    )
    assert expression == expected

    expression = (
        '\nvar s_1 = "";'
        '\ns_1 = "#00aaff";'
        "\nvar s_3 = JSON.parse(JSON.stringify(s_1));"
        "\nvar s_5 = JSON.parse(JSON.stringify(s_3));"
        '\ns_5 = "00aaff";'
    )
    result = exporter._remove_unused_js_vars(expression=expression)
    assert result == expression


@apply_test_settings()
def test__append_common_js_functions() -> None:
    expression: str = exporter._append_common_js_functions(
        expression='console.log("Hello!");'
    )
    assert js_functions.FUNC_COPY in expression
    assert expression.endswith('\nconsole.log("Hello!");')


@apply_test_settings()
def test__remove_blank_lines() -> None:
    expression: str = 'console.log("Hello!");' "\n" "\n  " '\nconsole.log("World!");'
    expression = exporter._remove_blank_lines(expression=expression)
    expected: str = 'console.log("Hello!");' '\nconsole.log("World!");'
    assert expression == expected


@apply_test_settings()
def test__minify_html() -> None:
    ap.Stage()
    html_str: str = "<html>" "\n<body>" "\n  <span>a</span>" "\n</body>" "\n</html>"
    html_str = exporter._minify_html(html_str=html_str, minify=False)
    assert html_str.startswith("<html>\n<body>")

    ap.set_debug_mode()
    html_str = exporter._minify_html(html_str=html_str, minify=True)
    assert html_str.startswith("<html>\n<body>")

    ap.Stage()
    html_str = exporter._minify_html(html_str=html_str, minify=True)
    assert html_str.startswith("<html><body>")


@apply_test_settings()
def test__append_event_handler_expressions() -> None:
    ap.Stage()
    instance: VariableNameMixIn = VariableNameMixIn()
    instance.variable_name = "test_instance"

    with HandlerScope(handler_name="test_handler_1", instance=instance):
        ap.append_js_expression(expression='console.log("world!");')
    expression: str = exporter._append_event_handler_expressions(
        expression='console.log("Hello!");'
    )
    expected: str = 'console.log("Hello!");' '\nconsole.log("world!");'
    assert expression == expected


@apply_test_settings()
def test__append_jslib_str_to_html() -> None:
    jquery_file_name: str = jslib_util.get_jquery_file_name()
    html_str: str = exporter._append_jslib_str_to_html(
        html_str="<body>",
        js_lib_dir_path="./",
        jslib_file_name=jquery_file_name,
        embed_js_libs=False,
    )
    expected: str = (
        "<body>"
        f'\n  <script type="text/javascript" src="./{jquery_file_name}">'
        "</script>"
    )
    assert html_str == expected

    html_str = exporter._append_jslib_str_to_html(
        html_str="<body>",
        js_lib_dir_path="./",
        jslib_file_name=jquery_file_name,
        embed_js_libs=True,
    )
    match: Optional[Match] = re.search(
        pattern=(
            r"\<body\>"
            r'\n  \<script type="text/javascript"\>'
            r"\n  .*\/\*\! jQuery.*"
            r"\n  \</script\>"
        ),
        string=html_str,
        flags=re.MULTILINE | re.DOTALL,
    )
    assert match is not None


@apply_test_settings()
def test__display_info() -> None:
    msg: str = exporter._display_info(msg="Hello", verbose=0)
    assert msg == ""

    msg = exporter._display_info(msg="Hello", verbose=1)
    assert msg == "Hello"


@apply_test_settings()
def test__display_debug_mode_ignoring_minify_setting_info() -> None:
    ap.Stage()
    ap.set_debug_mode()
    msg: str = exporter._display_debug_mode_ignoring_minify_setting_info(
        minify=False, verbose=1
    )
    assert msg == ""

    ap.Stage()
    msg = exporter._display_debug_mode_ignoring_minify_setting_info(
        minify=True, verbose=1
    )
    assert msg == ""

    ap.set_debug_mode()
    msg = exporter._display_debug_mode_ignoring_minify_setting_info(
        minify=True, verbose=1
    )
    assert msg != ""
