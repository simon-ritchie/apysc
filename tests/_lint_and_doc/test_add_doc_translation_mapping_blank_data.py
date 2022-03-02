import os
from random import randint
from types import ModuleType
from typing import Dict, List, Union
import importlib

from retrying import retry

from apysc._lint_and_doc import add_doc_translation_mapping_blank_data
from apysc._lint_and_doc.docs_lang import Lang
from apysc._lint_and_doc.translation_mapping_utils import MAPPING_CONST_NAME, read_mapping_data, get_mapping_module_path
from apysc._lint_and_doc.document_text_split_util import Heading, BodyText, CodeBlock
from apysc._file import file_util, module_util
from apysc._lint_and_doc import lint_and_doc_hash_util
from apysc._lint_and_doc.lint_and_doc_hash_util import HashType
from tests.testing_helper import assert_raises


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
    keys: List[str] = add_doc_translation_mapping_blank_data.\
        _convert_splitted_values_to_keys(splitted_values=splitted_values)
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
def test__make_mappings_from_keys() -> None:
    test_src_doc_file_path: str = \
        './docs_src/source/test_add_doc_translation_mapping_blank_data_2.md'
    test_mapping_module_path: str = add_doc_translation_mapping_blank_data.\
        get_mapping_module_path(
            src_doc_file_path=test_src_doc_file_path, lang=Lang.JP)
    file_util.remove_file_if_exists(file_path=test_mapping_module_path)

    file_util.save_plain_txt(
        txt=(
            'from typing import Dict'
            f'\n\n{MAPPING_CONST_NAME}: Dict[str, str] = '
            "{'a': 'b', 'd\\ne': 'f'}"
        ),
        file_path=test_mapping_module_path)
    mappings: List[Dict[str, str]] = add_doc_translation_mapping_blank_data.\
        _make_mappings_from_keys(
            keys=['a', 'c', 'd\\ne'],
            src_doc_file_path=test_mapping_module_path,
            lang=Lang.JP)
    assert mappings == [
        {'a': 'b'},
        {'c': ''},
        {'d\\ne': 'f'},
    ]

    file_util.remove_file_if_exists(file_path=test_mapping_module_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__save_mapping_data() -> None:
    test_src_doc_file_path: str = \
        './docs_src/source/test_add_doc_translation_mapping_blank_data_3.md'
    test_mapping_module_path: str = add_doc_translation_mapping_blank_data.\
        get_mapping_module_path(
            src_doc_file_path=test_src_doc_file_path, lang=Lang.JP)
    file_util.remove_file_if_exists(file_path=test_mapping_module_path)

    add_doc_translation_mapping_blank_data._save_mapping_data(
        mappings=[{
            'a': 'b',
        }, {
            'c':
            'Lorem ipsum dolor sit amet, consectetur adipiscing '
            'elit, sed do eiusmod tempor.',
        }, {
            'Lorem ipsum dolor sit amet, consectetur adipiscing '
            'elit, sed do eiusmod tempor.':
            'd',
        }],
        src_doc_file_path=test_src_doc_file_path,
        lang=Lang.JP)
    module: ModuleType = module_util.read_target_path_module(
        module_path=test_mapping_module_path)
    importlib.reload(module)
    assert module.__doc__ == (
        'This module is for the translation mapping data of the'
        '\nfollowing document:'
        '\n\nDocument file: test_add_doc_translation_mapping_blank_data_3.md'
        '\nLanguage: jp'
        '\n'
    )
    mapping: Dict[str, str] = getattr(module, MAPPING_CONST_NAME)
    assert mapping == {
        'a': 'b',
        'c':
        'Lorem ipsum dolor sit amet, consectetur adipiscing '
        'elit, sed do eiusmod tempor.',
        'Lorem ipsum dolor sit amet, consectetur adipiscing '
        'elit, sed do eiusmod tempor.':
        'd',
    }

    module_str: str = file_util.read_txt(
        file_path=test_mapping_module_path)
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
def test__get_hash_type_from_lang() -> None:
    hash_type: HashType = add_doc_translation_mapping_blank_data.\
        _get_hash_type_from_lang(lang=Lang.JP)
    assert hash_type == HashType.TRANSLATION_MAPPING_JP

    assert_raises(
        expected_error_class=ValueError,
        func_or_method=add_doc_translation_mapping_blank_data.
        _get_hash_type_from_lang,
        kwargs={'lang': None})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_add_mapping_blank_data() -> None:
    file_path: str = lint_and_doc_hash_util.get_target_file_hash_file_path(
        file_path='./docs_src/source/sprite.md',
        hash_type=HashType.TRANSLATION_MAPPING_JP)
    file_util.remove_file_if_exists(file_path=file_path)

    add_doc_translation_mapping_blank_data.add_mapping_blank_data(
        lang=Lang.JP)
    assert os.path.isfile(file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__append_body_text_keys_to_list() -> None:
    keys: List[str] = []
    add_doc_translation_mapping_blank_data._append_body_text_keys_to_list(
        key='Lorem ipsum', keys=keys)
    assert keys == ['Lorem ipsum']

    keys = []
    add_doc_translation_mapping_blank_data._append_body_text_keys_to_list(
        key='Lorem ipsum\\n\\ndolor sit', keys=keys)
    assert keys == ['Lorem ipsum', 'dolor sit']


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__remove_skipping_pattern_keys_from_list() -> None:
    result_keys: List[str] = add_doc_translation_mapping_blank_data.\
        _remove_skipping_pattern_keys_from_list(
            keys=[
                'Lorem ipsum',

                '<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->',

                '**[Interface signature]** `__init__(self, *, '
                'variable_name:Union[str, NoneType]=None) -> None`<hr>',

                '<hr>',

                'Dolor sit amet, consectetur adipiscing.',

                '<iframe src="static/sprite_move_instances_simultaneously'
                '/index.html" width="250" height="250"></iframe>',

                '<span class="inconspicuous-txt">Note: the '
                'document build script generates and updates this '
                'API document section automatically. Maybe this '
                'section is duplicated compared with previous '
                'sections.</span>',
            ])
    assert result_keys == [
        'Lorem ipsum',
        'Dolor sit amet, consectetur adipiscing.',
    ]


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__set_fixed_translation_value_if_exists() -> None:
    fixed_value: str = add_doc_translation_mapping_blank_data.\
        _set_fixed_translation_value_if_exists(
            key='**[Parameters]**', value='Lorem ipsum.')
    assert fixed_value == '**[引数]**'

    fixed_value = add_doc_translation_mapping_blank_data.\
        _set_fixed_translation_value_if_exists(
            key='Not existing key', value='Lorem ipsum.')
    assert fixed_value == 'Lorem ipsum.'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__set_same_value_if_code_block_mapping_is_blank() -> None:
    value: str = add_doc_translation_mapping_blank_data.\
        _set_same_value_if_code_block_mapping_is_blank(
            key='```py\nprint(10)\n```',
            value='Lorem ipsum.')
    assert value == 'Lorem ipsum.'

    value = add_doc_translation_mapping_blank_data.\
        _set_same_value_if_code_block_mapping_is_blank(
            key='Lorem ipsum.',
            value='')
    assert value == ''

    value = add_doc_translation_mapping_blank_data.\
        _set_same_value_if_code_block_mapping_is_blank(
            key='```py\nprint(10)\n```',
            value='')
    assert value == '```py\nprint(10)\n```'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__convert_link_list_by_lang() -> None:
    value: str = add_doc_translation_mapping_blank_data.\
        _convert_link_list_by_lang(
            key='Lorem ipsum.',
            value='Dolor sit.',
            lang=Lang.JP)
    assert value == 'Dolor sit.'

    value = add_doc_translation_mapping_blank_data.\
        _convert_link_list_by_lang(
            key='- Lorem ipsum.\n- Dolor sit.',
            value='Dolor sit.',
            lang=Lang.JP)
    assert value == 'Dolor sit.'

    value = add_doc_translation_mapping_blank_data.\
        _convert_link_list_by_lang(
            key=(
                '- [Lorem ipsum](any/path_1.md)'
                '\n- [Dolor sit](any/path_2.md)'
            ),
            value='',
            lang=Lang.JP)
    assert value == (
        '- [Lorem ipsum](any/jp_path_1.md)'
        '\\n- [Dolor sit](any/jp_path_2.md)'
    )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__escape_key_or_value() -> None:
    key_or_val: str = add_doc_translation_mapping_blank_data.\
        _escape_key_or_value(
            key_or_val=(
                "- [Lorem's\\+ ipsum](any/path_1.md)"
                '\n- [Dolor sit](any/path_2.md)'
            ))
    assert key_or_val == (
        "- [Lorem\\'s\\\\+ ipsum](any/path_1.md)"
        '\\n- [Dolor sit](any/path_2.md)'
    )
