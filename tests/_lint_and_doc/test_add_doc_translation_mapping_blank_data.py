from random import randint
from typing import Dict, List, Union

from retrying import retry

from apysc._lint_and_doc import add_doc_translation_mapping_blank_data
from apysc._lint_and_doc.add_doc_translation_mapping_blank_data import Lang, _MAPPING_CONST_NAME
from apysc._lint_and_doc.document_text_split_util import Heading, BodyText, CodeBlock
from apysc._file import file_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_src_docs_file_paths() -> None:
    src_docs_file_paths: List[str] = add_doc_translation_mapping_blank_data.\
        _get_src_docs_file_paths()
    assert './docs_src/source/sprite.md' in src_docs_file_paths
    assert './docs_src/source/_static/' not in src_docs_file_paths
    assert './docs_src/source/jp_sprite.md' not in src_docs_file_paths
    assert './docs_src/source/conf.py' not in src_docs_file_paths


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__is_translated_document() -> None:
    result: bool = add_doc_translation_mapping_blank_data.\
        _is_translated_document(path='./test/path.md')
    assert not result

    result = add_doc_translation_mapping_blank_data.\
        _is_translated_document(path='./test/jp_path.md')
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__convert_splitted_values_to_keys() -> None:
    splitted_values: List[Union[Heading, BodyText, CodeBlock]] = [
        Heading(heading_text='# Sprite'),
        BodyText(text='This page explains the `Sprite` class.'),
        CodeBlock(
            code_block=(
                '```py'
                '\n# runnable'
                '\nimport apysc as ap'
                "\nprint('Hello!')"
                '\n```'
            ))
    ]
    keys: List[str] = add_doc_translation_mapping_blank_data.\
        _convert_splitted_values_to_keys(splitted_values=splitted_values)
    assert len(keys) == 3
    assert keys[0] == '# Sprite'
    assert keys[1] == 'This page explains the `Sprite` class.'
    assert keys[2] == (
        '```py'
        '\n# runnable'
        '\nimport apysc as ap'
        "\nprint(\\'Hello!\\')"
        '\n```'
    )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_mapping_module_path() -> None:
    mapping_module_path: str = add_doc_translation_mapping_blank_data.\
        _get_mapping_module_path(
            src_doc_file_path='./docs_src/source/sprite.md',
            lang=Lang.JP)
    assert mapping_module_path == './apysc/_translation/jp/sprite.py'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__read_already_saved_mapping() -> None:
    test_src_doc_file_path: str = \
        './docs_src/source/test_add_doc_translation_mapping_blank_data_1.md'
    test_mapping_module_path: str = add_doc_translation_mapping_blank_data.\
        _get_mapping_module_path(
            src_doc_file_path=test_src_doc_file_path, lang=Lang.JP)
    file_util.remove_file_if_exists(file_path=test_mapping_module_path)
    already_saved_mapping: Dict[str, str] = \
        add_doc_translation_mapping_blank_data.\
        _read_already_saved_mapping(
            src_doc_file_path=test_src_doc_file_path, lang=Lang.JP)
    assert already_saved_mapping == {}

    file_util.save_plain_txt(
        txt='', file_path=test_mapping_module_path)
    already_saved_mapping = add_doc_translation_mapping_blank_data.\
        _read_already_saved_mapping(
            src_doc_file_path=test_src_doc_file_path, lang=Lang.JP)
    assert already_saved_mapping == {}

    file_util.save_plain_txt(
        txt=(
            'from typing import Dict'
            f'\n\n{_MAPPING_CONST_NAME}: Dict[str, str] = '
            "{'a': 'b'}"
        ),
        file_path=test_mapping_module_path)
    already_saved_mapping = add_doc_translation_mapping_blank_data.\
        _read_already_saved_mapping(
            src_doc_file_path=test_src_doc_file_path, lang=Lang.JP)
    assert already_saved_mapping == {'a': 'b'}

    file_util.remove_file_if_exists(file_path=test_mapping_module_path)
