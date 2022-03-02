from random import randint
from typing import Dict

from retrying import retry

from apysc._file import file_util
from apysc._lint_and_doc import translation_mapping_utils
from apysc._lint_and_doc.docs_lang import Lang
from apysc._lint_and_doc.translation_mapping_utils import MAPPING_CONST_NAME


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
