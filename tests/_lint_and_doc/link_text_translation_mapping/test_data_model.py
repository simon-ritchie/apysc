from random import randint

from retrying import retry

from apysc._lint_and_doc.link_text_translation_mapping import data_model
from apysc._lint_and_doc.link_text_translation_mapping.data_model import \
    Mapping
from tests.testing_helper import assert_attrs


class TestMapping:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        mapping: Mapping = Mapping(
            link_text='Lorem ipsum', mapping_text='テストテキスト')
        assert_attrs(
            expected_attrs={
                '_link_text': 'Lorem ipsum',
                '_mapping_text': 'テストテキスト',
            },
            any_obj=mapping)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_link_text(self) -> None:
        mapping: Mapping = Mapping(
            link_text='Lorem ipsum', mapping_text='テストテキスト')
        assert mapping.link_text == 'Lorem ipsum'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_mapping_text(self) -> None:
        mapping: Mapping = Mapping(
            link_text='Lorem ipsum', mapping_text='テストテキスト')
        assert mapping.mapping_text == 'テストテキスト'
