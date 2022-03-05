from random import randint
from typing import Dict, List, Union

from retrying import retry

from apysc._file import file_util
from apysc._lint_and_doc import translation_mapping_utils
from apysc._lint_and_doc.docs_lang import Lang
from apysc._lint_and_doc.translation_mapping_utils import MAPPING_CONST_NAME
from apysc._lint_and_doc.document_text_split_util import BodyText
from apysc._lint_and_doc.document_text_split_util import CodeBlock
from apysc._lint_and_doc.document_text_split_util import Heading


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_read_mapping_data() -> None:
    test_src_doc_file_path: str = \
        './docs_src/source/test_translation_mapping_utils_1.md'
    test_mapping_module_path: str = translation_mapping_utils.\
        get_mapping_module_path(
            src_doc_file_path=test_src_doc_file_path, lang=Lang.JP)
    file_util.remove_file_if_exists(file_path=test_mapping_module_path)
    already_saved_mapping: Dict[str, str] = \
        translation_mapping_utils.\
        read_mapping_data(
            src_doc_file_path=test_src_doc_file_path, lang=Lang.JP)
    assert already_saved_mapping == {}

    file_util.save_plain_txt(
        txt='', file_path=test_mapping_module_path)
    already_saved_mapping = translation_mapping_utils.\
        read_mapping_data(
            src_doc_file_path=test_src_doc_file_path, lang=Lang.JP)
    assert already_saved_mapping == {}

    file_util.save_plain_txt(
        txt=(
            'from typing import Dict'
            f'\n\n{MAPPING_CONST_NAME}: Dict[str, str] = '
            "{'a': 'b'}"
        ),
        file_path=test_mapping_module_path)
    already_saved_mapping = translation_mapping_utils.\
        read_mapping_data(
            src_doc_file_path=test_src_doc_file_path, lang=Lang.JP)
    assert already_saved_mapping == {'a': 'b'}

    file_util.remove_file_if_exists(file_path=test_mapping_module_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_mapping_module_path() -> None:
    mapping_module_path: str = translation_mapping_utils.\
        get_mapping_module_path(
            src_doc_file_path='./docs_src/source/sprite.md',
            lang=Lang.JP)
    assert mapping_module_path == './apysc/_translation/jp/sprite.py'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_convert_splitted_values_to_keys() -> None:
    splitted_values: List[Union[Heading, BodyText, CodeBlock]] = [
        Heading(heading_text='# Sprite'),
        BodyText(text='This page explains the `Sprite` class\\.'),
        CodeBlock(
            code_block=(
                '```py'
                '\n# runnable'
                '\nimport apysc as ap'
                "\nprint('Hello!')"
                '\n```'
            )),
        BodyText(text='Lorem ipsum dolor sit amet\n\nconsectetur adipiscing')
    ]
    keys: List[str] = translation_mapping_utils.\
        convert_splitted_values_to_keys(splitted_values=splitted_values)
    assert len(keys) == 5
    assert keys[0] == '# Sprite'
    assert keys[1] == 'This page explains the `Sprite` class\\\\.'
    assert keys[2] == (
        '```py'
        '\\n# runnable'
        '\\nimport apysc as ap'
        "\\nprint(\\'Hello!\\')"
        '\\n```'
    )
    assert keys[3] == 'Lorem ipsum dolor sit amet'
    assert keys[4] == 'consectetur adipiscing'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_escape_key_or_value() -> None:
    key_or_val: str = translation_mapping_utils.escape_key_or_value(
        key_or_val=(
            "- [Lorem's\\+ ipsum](any/path_1.md)"
            '\n- [Dolor sit](any/path_2.md)'
        ))
    assert key_or_val == (
        "- [Lorem\\'s\\\\+ ipsum](any/path_1.md)"
        '\\n- [Dolor sit](any/path_2.md)'
    )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__append_body_text_keys_to_list() -> None:
    keys: List[str] = []
    translation_mapping_utils._append_body_text_keys_to_list(
        key='Lorem ipsum', keys=keys)
    assert keys == ['Lorem ipsum']

    keys = []
    translation_mapping_utils._append_body_text_keys_to_list(
        key='Lorem ipsum\\n\\ndolor sit', keys=keys)
    assert keys == ['Lorem ipsum', 'dolor sit']


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_remove_escaping_from_key_or_value() -> None:
    key_or_val: str = translation_mapping_utils.\
        remove_escaping_from_key_or_value(
            key_or_val="\\\\Hello!\\n\\'World!")
    assert key_or_val == "\\Hello!\n'World!"


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_mapping_unnecessary_key() -> None:
    result: bool = translation_mapping_utils.\
        is_mapping_unnecessary_key(
            key=(
                '<iframe src="static/sprite_graphics_attribute'
                '/index.html" width="150" height="150"></iframe>'))
    assert result

    result = translation_mapping_utils.is_mapping_unnecessary_key(
        key='Lorem ipsum dolor sit.')
    assert not result
