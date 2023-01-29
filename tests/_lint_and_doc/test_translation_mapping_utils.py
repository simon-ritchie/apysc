from typing import Dict
from typing import List
from typing import Union

from apysc._file import file_util
from apysc._lint_and_doc import translation_mapping_utils
from apysc._lint_and_doc.docs_lang import Lang
from apysc._lint_and_doc.document_text_split_util import BodyText
from apysc._lint_and_doc.document_text_split_util import CodeBlock
from apysc._lint_and_doc.document_text_split_util import Heading
from apysc._lint_and_doc.lint_and_doc_hash_util import HashType
from apysc._lint_and_doc.translation_mapping_utils import MAPPING_CONST_NAME
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises


@apply_test_settings()
def test_read_mapping_data() -> None:
    test_src_doc_file_path: str = (
        "./docs_src/source/test_translation_mapping_utils_1.md"
    )
    test_mapping_module_path: str = translation_mapping_utils.get_mapping_module_path(
        src_doc_file_path=test_src_doc_file_path, lang=Lang.JP
    )
    file_util.remove_file_if_exists(file_path=test_mapping_module_path)
    already_saved_mapping: Dict[str, str] = translation_mapping_utils.read_mapping_data(
        src_doc_file_path=test_src_doc_file_path, lang=Lang.JP
    )
    assert already_saved_mapping == {}

    file_util.save_plain_txt(txt="", file_path=test_mapping_module_path)
    already_saved_mapping = translation_mapping_utils.read_mapping_data(
        src_doc_file_path=test_src_doc_file_path, lang=Lang.JP
    )
    assert already_saved_mapping == {}

    file_util.save_plain_txt(
        txt=(
            "from typing import Dict"
            f"\n\n{MAPPING_CONST_NAME}: Dict[str, str] = "
            "{'a': 'b'}"
        ),
        file_path=test_mapping_module_path,
    )
    already_saved_mapping = translation_mapping_utils.read_mapping_data(
        src_doc_file_path=test_src_doc_file_path, lang=Lang.JP
    )
    assert already_saved_mapping == {"a": "b"}

    file_util.remove_file_if_exists(file_path=test_mapping_module_path)


@apply_test_settings()
def test_get_mapping_module_path() -> None:
    mapping_module_path: str = translation_mapping_utils.get_mapping_module_path(
        src_doc_file_path="./docs_src/source/sprite.md", lang=Lang.JP
    )
    assert mapping_module_path == "./apysc/_translation/jp/sprite.py"


@apply_test_settings()
def test_convert_splitted_values_to_keys() -> None:
    splitted_values: List[Union[Heading, BodyText, CodeBlock]] = [
        Heading(heading_text="# Sprite"),
        BodyText(text="This page explains the `Sprite` class\\."),
        CodeBlock(
            code_block=(
                "```py"
                "\n# runnable"
                "\nimport apysc as ap"
                "\nprint('Hello!')"
                "\n```"
            )
        ),
        BodyText(text="Lorem ipsum dolor sit amet\n\nconsectetur adipiscing"),
    ]
    keys: List[str] = translation_mapping_utils.convert_splitted_values_to_keys(
        splitted_values=splitted_values
    )
    assert len(keys) == 5
    assert keys[0] == "# Sprite"
    assert keys[1] == "This page explains the `Sprite` class\\\\."
    assert keys[2] == (
        "```py"
        "\\n# runnable"
        "\\nimport apysc as ap"
        "\\nprint(\\'Hello!\\')"
        "\\n```"
    )
    assert keys[3] == "Lorem ipsum dolor sit amet"
    assert keys[4] == "consectetur adipiscing"


@apply_test_settings()
def test_escape_key_or_value() -> None:
    key_or_val: str = translation_mapping_utils.escape_key_or_value(
        key_or_val=(
            '- [Lorem\'s\\+ ipsum "dolar"](any/path_1.md)'
            "\n- [Dolor sit](any/path_2.md)"
        )
    )
    assert key_or_val == (
        '- [Lorem\\\'s\\\\+ ipsum \\"dolar\\"](any/path_1.md)'
        "\\n- [Dolor sit](any/path_2.md)"
    )


@apply_test_settings()
def test__append_body_text_keys_to_list() -> None:
    keys: List[str] = []
    translation_mapping_utils._append_body_text_keys_to_list(
        key="Lorem ipsum", keys=keys
    )
    assert keys == ["Lorem ipsum"]

    keys = []
    translation_mapping_utils._append_body_text_keys_to_list(
        key="Lorem ipsum\\n\\ndolor sit", keys=keys
    )
    assert keys == ["Lorem ipsum", "dolor sit"]

    keys = []
    translation_mapping_utils._append_body_text_keys_to_list(
        key=(
            "- `handler`: _Handler\\n"
            "  - A callable that an instance calls when an animation "
            "is complete."
            "\\n- `options`: dict or None, default None"
            "\\n  - Optional arguments dictionary to be passed to a "
            "handler."
        ),
        keys=keys,
    )
    assert keys == [
        "- `handler`: _Handler",
        "  - A callable that an instance " "calls when an animation is complete.",
        "- `options`: dict or None, default None",
        "  - Optional arguments dictionary to be passed to a handler.",
    ]

    keys = []
    translation_mapping_utils._append_body_text_keys_to_list(
        key=(
            "- ValueError: <br> ・If the animations' target "
            "is not this instance. <br> ・If there are changed "
            "duration, delay, or easing animation settings "
            "in the `animations` list."
        ),
        keys=keys,
    )
    assert keys == [
        "- ValueError: ",
        "<br> ・If the animations' target is not this instance. ",
        "<br> ・If there are changed "
        "duration, delay, or easing animation settings "
        "in the `animations` list.",
    ]


@apply_test_settings()
def test_remove_escaping_from_key_or_value() -> None:
    key_or_val: str = translation_mapping_utils.remove_escaping_from_key_or_value(
        key_or_val="\\\\Hello!\\n\\'World!\\\""
    )
    assert key_or_val == "\\Hello!\n'World!\""


@apply_test_settings()
def test_is_mapping_unnecessary_key() -> None:
    result: bool = translation_mapping_utils.is_mapping_unnecessary_key(
        key=(
            '<iframe src="static/sprite_graphics_attribute'
            '/index.html" width="150" height="150"></iframe>'
        )
    )
    assert result

    result = translation_mapping_utils.is_mapping_unnecessary_key(
        key="Lorem ipsum dolor sit."
    )
    assert not result


@apply_test_settings()
def test_is_translation_skipping_key() -> None:
    result: bool = translation_mapping_utils.is_translation_skipping_key(
        key="<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->"
    )
    assert result

    result = translation_mapping_utils.is_translation_skipping_key(
        key="Lorem ipsum dolor sit."
    )
    assert not result


@apply_test_settings()
def test_get_translated_file_path_from_src_path() -> None:
    test_source_doc_path: str = "./tmp/test_document.md"
    translated_file_path: str = (
        translation_mapping_utils.get_translated_file_path_from_src_path(
            source_doc_path=test_source_doc_path, lang=Lang.JP
        )
    )
    assert translated_file_path == "./tmp/jp_test_document.md"


@apply_test_settings()
def test_remove_empty_keys() -> None:
    keys: List[str] = [
        " ",
        "",
        "Lorem ipsum",
    ]
    result_keys: List[str] = translation_mapping_utils.remove_empty_keys(keys=keys)
    assert result_keys == ["Lorem ipsum"]


@apply_test_settings()
def test_get_hash_type_from_lang() -> None:
    hash_type: HashType = translation_mapping_utils.get_hash_type_from_lang(
        lang=Lang.JP
    )
    assert hash_type == HashType.TRANSLATION_MAPPING_JP

    assert_raises(
        expected_error_class=ValueError,
        callable_=translation_mapping_utils.get_hash_type_from_lang,
        lang=None,
    )


@apply_test_settings()
def test__key_is_api_docs_list() -> None:
    result: bool = translation_mapping_utils._key_is_api_docs_list(key_="Lorem ipsum")
    assert not result

    result = translation_mapping_utils._key_is_api_docs_list(
        key_=(
            "- [test document 1](test/document/path1.md)"
            "\\n- [test document 2](test/document/path2.md)"
        )
    )
    assert result

    result = translation_mapping_utils._key_is_api_docs_list(
        key_=(
            "- `handler`: _Handler\\n  - A callable that an "
            "instance calls when an animation is complete."
            "\\n- `options`: dict or None, default None\\n"
            "  - Optional arguments dictionary to be passed to "
            "a handler."
        )
    )
    assert result


@apply_test_settings()
def test__key_is_api_docs_br_tags_list() -> None:
    result: bool = translation_mapping_utils._key_is_api_docs_br_tags_list(
        key_="- ValueError: <br> ・If the animations' target "
        "is not this instance. <br> ・If there are changed "
        "duration, delay, or easing animation settings "
        "in the `animations` list."
    )
    assert result

    result = translation_mapping_utils._key_is_api_docs_br_tags_list(
        key_="Lorem ipsum dolor sit."
    )
    assert not result


@apply_test_settings()
def test__extend_keys_with_api_docs_br_tags_list() -> None:
    keys: List[str] = []
    translation_mapping_utils._extend_keys_with_api_docs_br_tags_list(
        keys=keys,
        key_=(
            "- ValueError: <br> ・If the animations' target "
            "is not this instance. <br> ・If there are changed "
            "duration, delay, or easing animation settings "
            "in the `animations` list."
        ),
    )
    assert keys == [
        "- ValueError: ",
        "<br> ・If the animations' target is not this instance. ",
        "<br> ・If there are changed duration, delay, or easing "
        "animation settings in the `animations` list.",
    ]
