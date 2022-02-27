from random import randint
from typing import List
import os

from retrying import retry

from apysc._lint_and_doc.fixed_translation_mapping.data_model import Mapping, Mappings
from apysc._lint_and_doc.fixed_translation_mapping import data_model
from tests.testing_helper import assert_attrs
from apysc._lint_and_doc.add_doc_translation_mapping_blank_data import Lang


class TestMapping:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        base: Mapping = Mapping(key='Lorem', value='ipsum')
        assert_attrs(
            expected_attrs={
                '_key': 'Lorem',
                '_value': 'ipsum',
            },
            any_obj=base)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_key(self) -> None:
        base: Mapping = Mapping(key='Lorem', value='ipsum')
        assert base.key == 'Lorem'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_value(self) -> None:
        base: Mapping = Mapping(key='Lorem', value='ipsum')
        assert base.value == 'ipsum'


class TestMappings:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__init__(self) -> None:
        mappings_list: List[Mapping] = [
            Mapping(key='Lorem', value='ipsum'),
        ]
        mappings: Mappings = Mappings(
            mappings=mappings_list)
        assert_attrs(
            expected_attrs={
                'mappings': mappings_list,
            },
            any_obj=mappings,
        )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_mappings_module_path_from_lang() -> None:
    module_path: str = data_model._get_mappings_module_path_from_lang(
        lang=Lang.JP)
    assert module_path.endswith('jp.py')
    assert os.path.isfile(module_path)
