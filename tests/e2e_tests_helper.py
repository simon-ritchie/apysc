"""This module is for the E2E testing common utilities
and definitions.
"""

import os

from apysc._lint_and_doc.docs_lang import Lang

LOCAL_FILE_PATH_PREFIX: str = f'file://{os.path.abspath("./")}/'


def get_docs_local_file_path(
        *, lang: Lang, file_name: str) -> str:
    """
    Get a document's local file path for the E2E testing.

    Parameters
    ----------
    lang : Lang
        A target language.
    file_name : str
        A target file name (e.g., `index`).

    Returns
    -------
    file_path : str
        A target document's local file path.
    """
    file_path: str = os.path.join(
        LOCAL_FILE_PATH_PREFIX,
        f'docs/{lang.value}/{file_name}.html',
    )
    return file_path
