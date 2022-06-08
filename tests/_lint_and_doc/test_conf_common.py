import os
from typing import Type, Union
from random import randint
from typing import Any

from retrying import retry
from sphinx.application import Sphinx
from docutils.transforms import Transform
from recommonmark.transform import AutoStructify

from apysc._lint_and_doc import conf_common


class _MockSphinx(Sphinx):

    def __init__(self) -> None:
        """The mock class for the `Sphinx` class.
        """

    def add_config_value(
            self, name: str, default: Any, rebuild: Union[bool, str],
            types: Any = ()) -> None:
        """
        Register a configuration value.

        Parameters
        ----------
        name : str
            The name of configuration value.
        default : Any
            The default value of the configuration.
        rebuild : Union[bool, str]
            The condition of rebuild.
        types : Any, optional
            The type of configuration value.
        """
        assert name == 'recommonmark_config'
        assert default == {
            'auto_toc_tree_section': 'Table of contents',
        }
        assert rebuild

    def add_transform(self, transform: Type[Transform]) -> None:
        """
        Register a Docutils transform to be applied after parsing.

        Parameters
        ----------
        transform : Type[Transform]
            A transform class.
        """
        assert transform == AutoStructify

    def add_js_file(
            self, filename: str, priority: int = 500,
            **kwargs: Any) -> None:
        """
        Register a JavaScript file to include in the HTML output.

        Parameters
        ----------
        filename : str
            A target JavaScript file name.
        priority : int, optional
            A priority for the file ordering.
        """
        assert filename.endswith('.js')
        assert os.path.exists(
            f'./docs_src/source/_static/{filename}'
        )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_setup() -> None:
    sphinx: _MockSphinx = _MockSphinx()
    conf_common.setup(sphinx=sphinx)
