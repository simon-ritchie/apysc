from random import randint
from typing import List, Union

from retrying import retry

from apysc._lint_and_doc import add_doc_translation_mapping_blank_data
from apysc._lint_and_doc.document_text_split_util import Heading, BodyText, CodeBlock


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
