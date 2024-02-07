import os
import re
import shutil
from typing import List

import scripts.build_docs as build_docs
from apysc._file import file_util
from apysc._jslib import jslib_util
from apysc._lint_and_doc import lint_and_doc_hash_util
from apysc._lint_and_doc.docs_lang import Lang
from apysc._lint_and_doc.docstring_util import DOCSTRING_PATH_COMMENT_KEYWORD
from apysc._lint_and_doc.lint_and_doc_hash_util import HashType
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs
from apysc._testing.testing_helper import assert_raises
from scripts.build_docs import _CodeBlock
from scripts.build_docs import _CodeBlockFlake8Error
from scripts.build_docs import _CodeBlockMypyError
from scripts.build_docs import _CodeBlockNumdoclintError
from scripts.build_docs import _RunReturnData
from scripts.build_docs import _ScriptData

_CHECKOUT_FILE_PATHS: List[str] = [
    ".lint_and_doc_hash/.document/docs_src/source/stage",
    ".lint_and_doc_hash/.document/docs_src/source/index",
    ".lint_and_doc_hash/.document/docs_src/source/jp_index",
    ".lint_and_doc_hash/.document/docs_src/source/sprite",
    ".lint_and_doc_hash/.document/docs_src/source/sprite",
    ".lint_and_doc_hash/.docstring_src/apysc/_display/sprite",
    "docs/en/index.html",
    "docs/jp/jp_index.html",
    "apysc/_display/sprite.py",
    ".lint_and_doc_hash/.applying_translation_mapping/docs_src/source/sprite",
]


def teardown() -> None:
    """
    The function would be called when the test ended.
    """
    _checkout_files()


def _checkout_files() -> None:
    """
    Run the git's checkout command to revert files.
    """
    for checkout_file_path in _CHECKOUT_FILE_PATHS:
        os.system(f"git checkout {checkout_file_path}")


@apply_test_settings()
def test__replace_static_path_recursively() -> None:
    jquery_file_name: str = jslib_util.get_jquery_file_name()
    tmp_dir_1: str = "../.tmp_test_build_docs/"
    shutil.rmtree(tmp_dir_1, ignore_errors=True)
    tmp_dir_2: str = os.path.join(tmp_dir_1, "subdir/")
    os.makedirs(tmp_dir_2, exist_ok=True)

    html_path: str = os.path.join(tmp_dir_1, "test.html")
    with open(html_path, "w") as f:
        f.write(
            '<link rel="stylesheet" type="text/css" ' 'href="_static/groundwork.css" />'
        )
    js_path: str = os.path.join(tmp_dir_2, "test.js")
    with open(js_path, "w") as f:
        f.write('"_static/groundwork.css"')
    pkl_path: str = os.path.join(tmp_dir_1, "test.pkl")
    with open(pkl_path, "w") as f:
        f.write("")
    jslib_path: str = os.path.join(tmp_dir_1, jquery_file_name)
    with open(jslib_path, "w") as f:
        f.write('"_static/groundwork.css"')

    build_docs._replace_static_path_recursively(dir_path=tmp_dir_1)
    target_file_paths: List[str] = [html_path, js_path]
    for target_file_path in target_file_paths:
        with open(target_file_path) as f:
            file_txt: str = f.read()
        assert "_static" not in file_txt
        assert "static" in file_txt

    with open(jslib_path) as f:
        file_txt = f.read()
        assert "_static" in file_txt

    shutil.rmtree(tmp_dir_1, ignore_errors=True)


class Test_CodeBlock:
    @apply_test_settings()
    def test___init__(self) -> None:
        code_block: _CodeBlock = _CodeBlock(
            code_type="py", code="print(100)", runnable=True
        )
        assert_attrs(
            expected_attrs={"code_type": "py", "code": "print(100)", "runnable": True},
            any_obj=code_block,
        )


@apply_test_settings()
def test__get_code_blocks_from_txt() -> None:
    md_txt: str = (
        "Hello"
        "\n\n```py"
        "\nprint(100)"
        "\nprint(200)"
        "\n```"
        "\n\nWorld"
        "\n```py"
        "\n# runnable"
        "\nprint(300)"
        "\n```"
        "\n"
        "\n```"
        "\n$ ls -l"
        "\n```"
    )
    code_blocks: List[_CodeBlock] = build_docs._get_code_blocks_from_txt(md_txt=md_txt)
    assert len(code_blocks) == 3

    assert code_blocks[0].code_type == "py"
    assert code_blocks[0].code == "print(100)\nprint(200)"
    assert not code_blocks[0].runnable

    assert code_blocks[1].code == "print(300)"
    assert code_blocks[1].runnable

    assert code_blocks[2].code_type == ""
    assert code_blocks[2].code == "$ ls -l"
    assert not code_blocks[2].runnable


@apply_test_settings()
def test__replace_html_saving_export_path_by_doc_path() -> None:
    code: str = """from apysc import Stage
from apysc import save_overall_html

stage = Stage(stage_width=300, stage_height=180, background_color='#333')
save_overall_html(
    dest_dir_path="./quick_start_stage_creation")"""
    code = build_docs._replace_html_saving_export_path_by_doc_path(code=code)
    expected: str = """save_overall_html(
    dest_dir_path="./docs_src/source/_static/quick_start_stage_creation/")"""
    assert expected in code


@apply_test_settings()
def test_get_runnable_scripts_in_md_code_blocks() -> None:
    tmp_md_file_path: str = "../tmp_test_get_runnable_scripts_in_md_code_blocks.md"
    md_txt: str = """Hello

```py
print(100)
```

World!

```py
# runnable
print(200)
save_overall_html(
    dest_dir_path="quick_start_stage_creation/")
```

```
# runnable
print(300)
```
"""
    with open(tmp_md_file_path, "w") as f:
        f.write(md_txt)
    runnable_scripts: List[str] = build_docs.get_runnable_scripts_in_md_code_blocks(
        md_file_path=tmp_md_file_path
    )
    assert len(runnable_scripts) == 1
    assert runnable_scripts == (
        [
            "print(200)"
            "\nsave_overall_html("
            '\n    dest_dir_path="./docs_src/source/_static/'
            'quick_start_stage_creation/",'
            '\n    js_lib_dir_path="../", skip_js_lib_exporting=True)'
        ]
    )

    file_util.remove_file_if_exists(file_path=tmp_md_file_path)


@apply_test_settings()
def test__exec_document_lint_and_script() -> None:
    hash_file_path: str = lint_and_doc_hash_util.get_target_file_hash_file_path(
        file_path="./docs_src/source/quick_start.md", hash_type=HashType.DOCUMENT
    )
    file_util.remove_file_if_exists(file_path=hash_file_path)

    executed_scripts: List[str] = build_docs._exec_document_lint_and_script(
        limit_count=10
    )
    assert len(executed_scripts) <= 10
    for executed_script in executed_scripts:
        if "save_overall_html" not in executed_script:
            continue
        assert "./docs_src/source/_static/" in executed_script


@apply_test_settings()
def test__remove_runnable_inline_comment_from_code_blocks() -> None:
    tmp_dir_path: str = "../tmp_test_build_docs/"
    shutil.rmtree(tmp_dir_path, ignore_errors=True)
    tmp_subdir_path: str = os.path.join(tmp_dir_path, "subdir/")
    os.makedirs(tmp_subdir_path)
    tmp_html_path_1: str = os.path.join(tmp_dir_path, "tmp_1.html")
    tmp_html_path_2: str = os.path.join(tmp_subdir_path, "tmp_2.html")
    tmp_txt_path_1: str = os.path.join(tmp_dir_path, "tmp_1.txt")
    html_txt: str = (
        "<span>a</span>"
        '<span></span><span class="c1"># runnable</span>'
        "\n<span>b</span>"
    )
    for file_path in (tmp_html_path_1, tmp_html_path_2, tmp_txt_path_1):
        with open(file_path, "w") as f:
            f.write(html_txt)
    build_docs._remove_runnable_inline_comment_from_code_blocks(dir_path=tmp_dir_path)
    expected: str = "<span>a</span>" "\n<span>b</span>"
    for file_path in (tmp_html_path_1, tmp_html_path_2):
        with open(file_path) as f:
            txt: str = f.read()
        assert txt == expected
    with open(tmp_txt_path_1) as f:
        txt = f.read()
        assert txt == html_txt

    shutil.rmtree(tmp_dir_path, ignore_errors=True)


@apply_test_settings()
def test__append_js_lib_path_and_skip_settings() -> None:
    """_append_js_lib_path_and_skip_settings 関数のテスト。"""
    code: str = """print(200)
save_overall_html(
    dest_dir_path="quick_start_stage_creation/")"""
    code = build_docs._append_js_lib_path_and_skip_settings(code=code)
    expected: str = """print(200)
save_overall_html(
    dest_dir_path="quick_start_stage_creation/",
    js_lib_dir_path="../", skip_js_lib_exporting=True)"""
    assert code == expected

    code = """save_overall_html(
    dest_dir_path="quick_start_stage_creation/"
)"""
    code = build_docs._append_js_lib_path_and_skip_settings(code=code)
    expected = """save_overall_html(
    dest_dir_path="quick_start_stage_creation/",
    js_lib_dir_path="../", skip_js_lib_exporting=True)"""
    assert code == expected


@apply_test_settings()
def test__make_script_data_list() -> None:
    os.makedirs("./tmp/", exist_ok=True)
    tmp_file_path_1: str = "./tmp/tmp_test_build_docs_1.md"
    tmp_file_path_2: str = "./tmp/tmp_test_build_docs_2.md"
    with open(tmp_file_path_1, "w") as f:
        f.write(
            "# heading"
            "\n\n```py"
            "\n# runnable"
            "\nprint(100)"
            "\n```"
            "\n\n```py"
            "\n# runnable"
            "\nprint(200)"
            "\n```"
            "\n"
        )
    with open(tmp_file_path_2, "w") as f:
        f.write("# heading" "\n\n```py" "\n# runnable" "\nprint(300)" "\n```" "\n")
    md_file_paths: List[str] = [tmp_file_path_1, tmp_file_path_2]
    script_data_list: List[_ScriptData] = build_docs._make_script_data_list(
        md_file_paths=md_file_paths, limit_count=None
    )
    assert len(script_data_list) == 3
    assert script_data_list[0] == {
        "md_file_path": tmp_file_path_1,
        "runnable_script": "print(100)",
    }
    assert script_data_list[1] == {
        "md_file_path": tmp_file_path_1,
        "runnable_script": "print(200)",
    }
    assert script_data_list[2] == {
        "md_file_path": tmp_file_path_2,
        "runnable_script": "print(300)",
    }

    script_data_list = build_docs._make_script_data_list(
        md_file_paths=md_file_paths, limit_count=2
    )
    assert len(script_data_list) == 2

    file_util.remove_file_if_exists(file_path=tmp_file_path_1)
    file_util.remove_file_if_exists(file_path=tmp_file_path_2)


@apply_test_settings()
def test__run_code_block_script() -> None:
    return_data: _RunReturnData = build_docs._run_code_block_script(
        script_data={
            "md_file_path": "test.md",
            "runnable_script": "print(200)",
        }
    )
    assert return_data == {
        "md_file_path": "test.md",
        "runnable_script": "print(200)",
        "stdout": "200\n",
    }


@apply_test_settings()
def test__validate_script_return_data() -> None:
    build_docs._validate_script_return_data(
        return_data_list=[
            {
                "md_file_path": "test.md",
                "runnable_script": "print(100)",
                "stdout": "100\n",
            }
        ]
    )

    assert_raises(
        expected_error_class=Exception,
        callable_=build_docs._validate_script_return_data,
        match="Error occurred while executing the document codeblock.",
        return_data_list=[
            {
                "md_file_path": "test.md",
                "runnable_script": "print(100)",
                "stdout": "Traceback: most recent call ...",
            }
        ],
    )


@apply_test_settings()
def test__check_code_block_with_flake8() -> None:
    script_data: _ScriptData = {
        "md_file_path": "./tmp.py",
        "runnable_script": "a=10",
    }
    assert_raises(
        expected_error_class=_CodeBlockFlake8Error,
        callable_=build_docs._check_code_block_with_flake8,
        match=r"There is a flake8 error in the following document " r"code block:",
        script_data=script_data,
    )

    script_data = {
        "md_file_path": "./tmp.py",
        "runnable_script": "a = 20",
    }
    build_docs._check_code_block_with_flake8(script_data=script_data)


@apply_test_settings()
def test__check_code_block_with_numdoclint() -> None:
    script_data: _ScriptData = {
        "md_file_path": "./tmp.py",
        "runnable_script": "def func_1" "(a):\n    print(100)",
    }
    assert_raises(
        expected_error_class=_CodeBlockNumdoclintError,
        callable_=build_docs._check_code_block_with_numdoclint,
        match=r"There is a numdoclint error in the following " r"document code block",
        script_data=script_data,
    )

    script_data = {
        "md_file_path": "./tmp.py",
        "runnable_script": "def func_2"
        "(a):"
        '\n    """'
        "\n    test function."
        "\n\n    Parameters"
        "\n    ----------"
        "\n    a : int"
        "\n        Test argument."
        '\n    """'
        "\n    print(100)",
    }
    build_docs._check_code_block_with_numdoclint(script_data=script_data)


@apply_test_settings()
def test__check_code_block_with_mypy() -> None:
    script_data: _ScriptData = {
        "md_file_path": "./tmp.py",
        "runnable_script": "def func_1" "(a):\n    print(100)",
    }
    assert_raises(
        expected_error_class=_CodeBlockMypyError,
        callable_=build_docs._check_code_block_with_mypy,
        match="There is a mypy error in the following document code block",
        script_data=script_data,
    )

    script_data = {
        "md_file_path": "./tmp.py",
        "runnable_script": "print(100)",
    }
    build_docs._check_code_block_with_mypy(script_data=script_data)


@apply_test_settings()
def test__get_code_block_output_dir_paths() -> None:
    tmp_test_dir_path: str = "tmp/test_build_docs_1/"
    shutil.rmtree(tmp_test_dir_path, ignore_errors=True)
    dir_paths: List[str] = build_docs._get_code_block_output_dir_paths(
        output_dir_path=tmp_test_dir_path
    )
    assert dir_paths == []

    tmp_subdir_path_1: str = os.path.join(tmp_test_dir_path, "test_1/")
    os.makedirs(tmp_subdir_path_1, exist_ok=True)
    tmp_subdir_path_2: str = os.path.join(tmp_test_dir_path, "test_2/")
    os.makedirs(tmp_subdir_path_2, exist_ok=True)
    tmp_index_path: str = os.path.join(
        tmp_subdir_path_2,
        "index.html",
    )
    with open(tmp_index_path, "w") as f:
        f.write("")
    tmp_static_file_path: str = os.path.join(tmp_test_dir_path, "tmp_test.js")
    with open(tmp_static_file_path, "w") as f:
        f.write("")
    dir_paths = build_docs._get_code_block_output_dir_paths(
        output_dir_path=tmp_test_dir_path
    )
    assert dir_paths == ["tmp/test_build_docs_1/test_2/"]

    shutil.rmtree(tmp_test_dir_path, ignore_errors=True)


@apply_test_settings()
def test__copy_code_block_outputs() -> None:
    tmp_test_dir_path: str = "tmp/test_build_docs_2/"
    shutil.rmtree(tmp_test_dir_path, ignore_errors=True)
    tmp_subdir_path: str = os.path.join(tmp_test_dir_path, "tmp_test_build_docs/")
    os.makedirs(tmp_subdir_path, exist_ok=True)
    tmp_index_path: str = os.path.join(tmp_subdir_path, "index.html")
    with open(tmp_index_path, "w") as f:
        f.write("")
    expected_dir_path: str = "./docs/en/static/tmp_test_build_docs/"
    expected_file_path: str = os.path.join(
        expected_dir_path,
        "index.html",
    )
    shutil.rmtree(expected_dir_path, ignore_errors=True)
    build_docs._copy_code_block_outputs(output_dir_path=tmp_test_dir_path)
    assert os.path.isfile(expected_file_path)

    shutil.rmtree(tmp_test_dir_path, ignore_errors=True)
    shutil.rmtree(expected_dir_path, ignore_errors=True)


@apply_test_settings()
def test__replace_docstring_specification() -> None:
    tmp_dir_path: str = "./tmp/"
    os.makedirs(tmp_dir_path, exist_ok=True)
    tmp_file_path: str = os.path.join(
        tmp_dir_path,
        "test_build_docs_1.md",
    )
    file_util.save_plain_txt(
        txt=(
            "# Test document"
            "\n\nLorem ipsum dolor sit amet."
            "\n\n## Constructor API"
            f"\n\n<!-- {DOCSTRING_PATH_COMMENT_KEYWORD} "
            "apysc._display.sprite.Sprite.__init__ -->"
            "\n\n## stage_elem_id property API"
            f"\n\n<!-- {DOCSTRING_PATH_COMMENT_KEYWORD} "
            "apysc._display.stage.Stage.stage_elem_id -->"
        ),
        file_path=tmp_file_path,
    )
    build_docs._replace_docstring_specification(md_file_path=tmp_file_path)

    file_util.remove_file_if_exists(file_path=tmp_file_path)


@apply_test_settings()
def test__remove_document_hash_files_if_docstring_src_modified() -> None:
    _checkout_files()

    module_paths: List[str] = (
        build_docs._remove_document_hash_files_if_docstring_src_modified(
            md_file_path="./docs_src/source/index.md"
        )
    )
    assert module_paths == []

    docstring_src_hash_file_path: str = (
        lint_and_doc_hash_util.get_target_file_hash_file_path(
            file_path="./apysc/_display/sprite.py", hash_type=HashType.DOCSTRING_SRC
        )
    )
    file_util.remove_file_if_exists(file_path=docstring_src_hash_file_path)
    module_paths = build_docs._remove_document_hash_files_if_docstring_src_modified(
        md_file_path="./docs_src/source/sprite.md"
    )
    expected_document_hash_file_path: str = (
        lint_and_doc_hash_util.get_target_file_hash_file_path(
            file_path="./docs_src/source/sprite.md", hash_type=HashType.DOCUMENT
        )
    )
    assert not os.path.exists(expected_document_hash_file_path)
    assert "./apysc/_display/sprite.py" in module_paths

    _checkout_files()
    lint_and_doc_hash_util.save_target_file_hash(
        file_path="./apysc/_display/sprite.py", hash_type=HashType.DOCSTRING_SRC
    )
    module_paths = build_docs._remove_document_hash_files_if_docstring_src_modified(
        md_file_path="./docs_src/source/sprite.md"
    )
    assert os.path.exists(expected_document_hash_file_path)

    _checkout_files()


@apply_test_settings()
def test__flatten_2dim_module_paths_and_make_it_unique() -> None:
    flattened_module_paths: List[str] = (
        build_docs._flatten_2dim_module_paths_and_make_it_unique(
            docstring_module_paths=[
                [
                    "./apysc/_display/sprite.py",
                    "./apysc/_display/display_object.py",
                ],
                [
                    "./apysc/_display/sprite.py",
                ],
            ]
        )
    )
    assert sorted(flattened_module_paths) == sorted(
        ["./apysc/_display/sprite.py", "./apysc/_display/display_object.py"]
    )


@apply_test_settings()
def test__save_docstring_module_hash() -> None:
    test_module_path: str = "./tests/test_build_docs.py"
    test_hash_file_path: str = lint_and_doc_hash_util.get_target_file_hash_file_path(
        file_path=test_module_path,
        hash_type=lint_and_doc_hash_util.HashType.DOCSTRING_SRC,
    )
    file_util.remove_file_if_exists(file_path=test_hash_file_path)
    build_docs._save_docstring_module_hash(module_path=test_module_path)
    assert os.path.isfile(test_hash_file_path)

    file_util.remove_file_if_exists(file_path=test_hash_file_path)


@apply_test_settings()
def test_check_each_doc_has_single_h1_symbol() -> None:
    file_names: List[str] = os.listdir("./docs_src/source/")
    doc_file_paths: List[str] = []
    for file_name in file_names:
        file_path: str = os.path.join(
            "./docs_src/source/",
            file_name,
        )
        if not os.path.isfile(file_path):
            continue
        if not file_path.endswith(".md"):
            continue
        doc_file_paths.append(file_path)

    for doc_file_path in doc_file_paths:
        doc_txt: str = file_util.read_txt(file_path=doc_file_path)
        doc_txt = re.sub(
            pattern=r"```.+?```",
            repl="",
            string=doc_txt,
            flags=re.MULTILINE | re.DOTALL,
        )
        found_txts: List[str] = re.findall(
            pattern=r"^# ", string=doc_txt, flags=re.MULTILINE
        )
        assert len(found_txts) == 1, doc_file_path


@apply_test_settings()
def test__get_build_command() -> None:
    command: str = build_docs._get_build_command(lang=Lang.EN)
    assert command == (
        "sphinx-build ./docs_src/source/ ./docs/en/ " "-c ./docs_src/source/conf_en/"
    )

    command = build_docs._get_build_command(lang=Lang.JP)
    assert command == (
        "sphinx-build ./docs_src/source/ ./docs/jp/ " "-c ./docs_src/source/conf_jp/"
    )


@apply_test_settings()
def test__sync_js_libs() -> None:
    jquery_file_name: str = jslib_util.get_jquery_file_name()
    test_file_path: str = f"./docs_src/source/_static/{jquery_file_name}"
    file_util.remove_file_if_exists(file_path=test_file_path)

    build_docs._sync_js_libs()
    assert os.path.exists(test_file_path)


@apply_test_settings()
def test__get_excluding_file_names_prefix_list() -> None:
    excluding_file_names_prefix_list: List[str] = (
        build_docs._get_excluding_file_names_prefix_list()
    )
    assert "jp_" in excluding_file_names_prefix_list
    assert "en_" not in excluding_file_names_prefix_list


@apply_test_settings()
def test__apply_black_formatting_to_code_block() -> None:
    tmp_md_str: str = "Hello!\n\n```py\nprint('100')\n```"
    os.makedirs("./tmp/", exist_ok=True)
    tmp_md_path: str = os.path.join("./tmp/test_build_docs_2.md")
    file_util.save_plain_txt(txt=tmp_md_str, file_path=tmp_md_path)
    build_docs._apply_black_formatting_to_code_block(md_file_path=tmp_md_path)
    result_md_str: str = file_util.read_txt(file_path=tmp_md_path)
    expected_str: str = "Hello!\n\n```py" '\nprint("100")' "\n```"
    assert result_md_str == expected_str

    file_util.remove_file_if_exists(file_path=tmp_md_path)


@apply_test_settings()
def test__delete_unnecessary_js_files() -> None:
    build_docs._delete_unnecessary_js_files()
    assert not os.path.exists("docs/en/static/jquery-3.5.1.js")
    assert not os.path.exists("docs/jp/static/jquery-3.5.1.js")
