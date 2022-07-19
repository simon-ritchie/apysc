import os
from random import randint
from typing import Any

from retrying import retry
from sphinx.application import Sphinx

from apysc._lint_and_doc import conf_common


class _MockSphinx(Sphinx):
    def __init__(self) -> None:
        """The mock class for the `Sphinx` class."""

    def add_js_file(self, filename: str, priority: int = 500, **kwargs: Any) -> None:
        """
        Register a JavaScript file to include in the HTML output.

        Parameters
        ----------
        filename : str
            A target JavaScript file name.
        priority : int, optional
            A priority for the file ordering.
        """
        assert filename.endswith(".js")
        assert os.path.exists(f"./docs_src/source/_static/{filename}")


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_setup() -> None:
    sphinx: _MockSphinx = _MockSphinx()
    conf_common.setup(sphinx=sphinx)
