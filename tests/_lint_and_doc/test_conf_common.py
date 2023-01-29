import os
from typing import Any

from sphinx.application import Sphinx

from apysc._lint_and_doc import conf_common
from apysc._testing.testing_helper import apply_test_settings


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
        if filename != "keyword_link_mapping.js":
            assert os.path.exists(f"./docs_src/source/_static/{filename}")


@apply_test_settings()
def test_setup() -> None:
    sphinx: _MockSphinx = _MockSphinx()
    conf_common.setup(sphinx=sphinx)
