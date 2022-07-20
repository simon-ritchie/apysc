import importlib
import os
from random import randint
from types import ModuleType
from typing import Dict
from typing import List

from retrying import retry

from apysc._file import file_util
from apysc._file import module_util
from apysc._lint_and_doc import add_doc_translation_mapping_blank_data as mod
from apysc._lint_and_doc import lint_and_doc_hash_util
from apysc._lint_and_doc.docs_lang import Lang
from apysc._lint_and_doc.lint_and_doc_hash_util import HashType
from apysc._lint_and_doc.translation_mapping_utils import MAPPING_CONST_NAME


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_src_docs_file_paths() -> None:
    src_docs_file_paths: List[
        str
    ] = mod._get_src_docs_file_paths()
    assert "./docs_src/source/sprite.md" in src_docs_file_paths
    assert "./docs_src/source/_static/" not in src_docs_file_paths
    assert "./docs_src/source/jp_sprite.md" not in src_docs_file_paths
    assert "./docs_src/source/conf.py" not in src_docs_file_paths


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__is_translated_document() -> None:
    result: bool = mod._is_translated_document(
        path="./test/path.md"
    )
    assert not result

    result = mod._is_translated_document(
        path="./test/jp_path.md"
    )
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__make_mappings_from_keys() -> None:
    test_src_doc_file_path: str = (
        "./docs_src/source/test_add_doc_translation_mapping_blank_data_2.md"
    )
    test_mapping_module_path: str = (
        mod.get_mapping_module_path(
            src_doc_file_path=test_src_doc_file_path, lang=Lang.JP
        )
    )
    file_util.remove_file_if_exists(file_path=test_mapping_module_path)

    file_util.save_plain_txt(
        txt=(
            "from typing import Dict"
            f"\n\n{MAPPING_CONST_NAME}: Dict[str, str] = "
            "{'a': 'b', 'd\\ne': 'f'}"
        ),
        file_path=test_mapping_module_path,
    )
    mappings: List[
        Dict[str, str]
    ] = mod._make_mappings_from_keys(
        keys=["a", "c", "d\\ne"],
        src_doc_file_path=test_mapping_module_path,
        lang=Lang.JP,
    )
    assert mappings == [
        {"a": "b"},
        {"c": ""},
        {"d\\ne": "f"},
    ]

    file_util.remove_file_if_exists(file_path=test_mapping_module_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__save_mapping_data() -> None:
    test_src_doc_file_path: str = (
        "./docs_src/source/test_add_doc_translation_mapping_blank_data_3.md"
    )
    test_mapping_module_path: str = (
        mod.get_mapping_module_path(
            src_doc_file_path=test_src_doc_file_path, lang=Lang.JP
        )
    )
    file_util.remove_file_if_exists(file_path=test_mapping_module_path)

    mod._save_mapping_data(
        mappings=[
            {
                "a": "b",
            },
            {
                "c": "Lorem ipsum dolor sit amet, consectetur adipiscing "
                "elit, sed do eiusmod tempor.",
            },
            {
                "Lorem ipsum dolor sit amet, consectetur adipiscing "
                "elit, sed do eiusmod tempor.": "d",
            },
        ],
        src_doc_file_path=test_src_doc_file_path,
        lang=Lang.JP,
    )
    module: ModuleType = module_util.read_target_path_module(
        module_path=test_mapping_module_path
    )
    importlib.reload(module)
    assert module.__doc__ == (
        "This module is for the translation mapping data of the"
        "\nfollowing document:"
        "\n\nDocument file: test_add_doc_translation_mapping_blank_data_3.md"
        "\nLanguage: jp"
        "\n"
    )
    mapping: Dict[str, str] = getattr(module, MAPPING_CONST_NAME)
    assert mapping == {
        "a": "b",
        "c": "Lorem ipsum dolor sit amet, consectetur adipiscing "
        "elit, sed do eiusmod tempor.",
        "Lorem ipsum dolor sit amet, consectetur adipiscing "
        "elit, sed do eiusmod tempor.": "d",
    }

    module_str: str = file_util.read_txt(file_path=test_mapping_module_path)
    expected_strs: List[str] = [
        "\n    'Lorem ipsum dolor sit amet, consectetur "
        "adipiscing elit, sed do eiusmod tempor.',  # noqa",
        "\n    'Lorem ipsum dolor sit amet, consectetur adipiscing "
        "elit, sed do eiusmod tempor.':  # noqa",
    ]
    for expected_str in expected_strs:
        assert expected_str in module_str

    file_util.remove_file_if_exists(file_path=test_mapping_module_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_add_mapping_blank_data() -> None:
    file_path: str = lint_and_doc_hash_util.get_target_file_hash_file_path(
        file_path="./docs_src/source/sprite.md",
        hash_type=HashType.TRANSLATION_MAPPING_JP,
    )
    file_util.remove_file_if_exists(file_path=file_path)

    mod.add_mapping_blank_data(lang=Lang.JP)
    assert os.path.isfile(file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__remove_skipping_pattern_keys_from_list() -> None:
    result_keys: List[
        str
    ] = mod._remove_skipping_pattern_keys_from_list(
        keys=[
            "Lorem ipsum",
            "<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->",
            "**[Interface signature]** `__init__(self, *, "
            "variable_name:Union[str, NoneType]=None) -> None`<hr>",
            "Dolor sit amet, consectetur adipiscing.",
            '<iframe src="static/sprite_move_instances_simultaneously'
            '/index.html" width="250" height="250"></iframe>',
        ]
    )
    assert result_keys == [
        "Lorem ipsum",
        "Dolor sit amet, consectetur adipiscing.",
    ]


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__set_fixed_translation_value_if_exists() -> None:
    fixed_value: str = (
        mod._set_fixed_translation_value_if_exists(
            key="**[Parameters]**", value="Lorem ipsum."
        )
    )
    assert fixed_value == "**[引数]**"

    fixed_value = (
        mod._set_fixed_translation_value_if_exists(
            key="Not existing key", value="Lorem ipsum."
        )
    )
    assert fixed_value == "Lorem ipsum."


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__set_same_value_if_code_block_mapping_is_blank() -> None:
    value: str = mod._set_same_value_if_code_block_mapping_is_blank(
        key="```py\nprint(10)\n```", value="Lorem ipsum."
    )
    assert value == "Lorem ipsum."

    value = mod._set_same_value_if_code_block_mapping_is_blank(
        key="Lorem ipsum.", value=""
    )
    assert value == ""

    value = mod._set_same_value_if_code_block_mapping_is_blank(
        key="```py\nprint(10)\n```", value=""
    )
    assert value == "```py\nprint(10)\n```"


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__convert_link_list_by_lang() -> None:
    value: str = mod._convert_link_list_by_lang(
        key="Lorem ipsum.", value="Dolor sit.", lang=Lang.JP
    )
    assert value == "Dolor sit."

    value = mod._convert_link_list_by_lang(
        key="- Lorem ipsum.\n- Dolor sit.", value="Dolor sit.", lang=Lang.JP
    )
    assert value == "Dolor sit."

    value = mod._convert_link_list_by_lang(
        key=(
            "- [Graphics class](any/path_1.md)"
            "\n- [Graphics begin_fill interface](any/path_2.md)"
        ),
        value="",
        lang=Lang.JP,
    )
    assert value == (
        "- [Graphics クラス](any/jp_path_1.md)"
        "\\n- [Graphics クラス begin_fill （塗り設定）の"
        "インターフェイス](any/jp_path_2.md)"
    )


def _read_added_mapping_modules_recursively(*, dir_path: str) -> None:
    """
    Read specified directory path's modules recursively
    to check it does not raise an exception.

    Parameters
    ----------
    dir_path : str
        A target directory path.
    """
    if not os.path.isdir(dir_path):
        return
    file_or_dir_names: List[str] = os.listdir(dir_path)
    for file_or_dir_name in file_or_dir_names:
        if "__pycache__" in file_or_dir_name:
            continue
        if file_or_dir_name.endswith(".pyc"):
            continue
        if file_or_dir_name == "__init__.py":
            continue
        file_or_dir_path: str = os.path.join(dir_path, file_or_dir_name)
        print("Checking a mapping module's importing:", file_or_dir_path)
        if os.path.isdir(file_or_dir_path):
            _read_added_mapping_modules_recursively(dir_path=file_or_dir_path)
            continue
        module: ModuleType = module_util.read_target_path_module(
            module_path=file_or_dir_path
        )
        importlib.reload(module)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_can_read_added_mapping_modules() -> None:
    _read_added_mapping_modules_recursively(dir_path="./apysc/_translation/")


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__extract_link_texts() -> None:
    link_texts: List[str] = mod._extract_link_texts(
        value=("- [Lorem ipsum](any/path_1.md)" "\n- [Dolar sit](any/path_2.md)")
    )
    assert link_texts == ["Lorem ipsum", "Dolar sit"]


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__replace_link_text_by_fixed_mapping() -> None:
    value: str = (
        mod._replace_link_text_by_fixed_mapping(
            value="- [Lorem ipsum](any/path_1.md)", lang=Lang.JP
        )
    )
    assert value == ""

    value = mod._replace_link_text_by_fixed_mapping(
        value=(
            "- [Graphics class](graphics.md)"
            "\n- [Graphics line_style interface](graphics_line_style.md)"
        ),
        lang=Lang.JP,
    )
    expected: str = (
        "- [Graphics クラス](graphics.md)"
        "\n- [Graphics クラス line_style （線設定）のインターフェイス]"
        "(graphics_line_style.md)"
    )
    assert value == expected


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__set_same_value_if_api_params_or_returns_list() -> None:
    value: str = mod._set_same_value_if_api_params_or_returns_list(
        key="Lorem ipsum", value="テストテキスト"
    )
    assert value == "テストテキスト"

    value = mod._set_same_value_if_api_params_or_returns_list(
        key="- `self`: AnimatonBase", value="テストテキスト"
    )
    assert value == "- `self`: AnimatonBase"


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__set_same_value_if_key_is_no_mapping_fixed_string() -> None:
    value: str = mod._set_same_value_if_key_is_no_mapping_fixed_string(
        key="</details>", value=""
    )
    assert value == "</details>"

    value = mod._set_same_value_if_key_is_no_mapping_fixed_string(
        key="Lorem ipsum", value=""
    )
    assert value == ""


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__set_same_value_if_key_is_image_link() -> None:
    value: str = (
        mod._set_same_value_if_key_is_image_link(
            key="Lorem ipsum", value=""
        )
    )
    assert value == ""

    value = mod._set_same_value_if_key_is_image_link(
        key="![](_static/colaboratory_interface.png)", value=""
    )
    assert value == "![](_static/colaboratory_interface.png)"


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__set_translated_file_names_to_toc_code_block() -> None:
    value: str = "Lorem ipsum"
    value = mod._set_translated_file_names_to_toc_code_block(
        lang=Lang.JP, value=value
    )
    assert value == "Lorem ipsum"

    value = "```{toctree}" "\\nlorem_ipsum" "\njp_dolor_sit_amet_2" "\n```"
    value = mod._set_translated_file_names_to_toc_code_block(
        lang=Lang.JP, value=value
    )
    assert value == ("```{toctree}" "\njp_lorem_ipsum" "\njp_dolor_sit_amet_2" "\n```")
