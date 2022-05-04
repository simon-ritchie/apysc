from random import randint

from retrying import retry

from tests import e2e_tests_helper
from apysc._lint_and_doc.docs_lang import Lang


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_docs_local_file_path() -> None:
    file_path: str = e2e_tests_helper.get_docs_local_file_path(
        lang=Lang.EN, file_name='index')
    assert file_path.startswith('file://')
    assert file_path.endswith('/docs/en/index.html')
