"""This module is for the translation conversion
of the documents.
"""

from typing import List
from typing import Union

from apysc._lint_and_doc.docs_lang import Lang


def apply_translation_to_doc(
        *, md_file_path: str, lang: Lang) -> None:
    """
    Apply a translation mapping to a specified markdown
    document. This interface saves a translated file
    with a file name with a language suffix (e.g.,
    jp_your_doc.md).

    Parameters
    ----------
    md_file_path : str
        A source markdown file path.
    """
    from apysc._file import file_util
    from apysc._lint_and_doc.document_text_split_util import BodyText
    from apysc._lint_and_doc.document_text_split_util import CodeBlock
    from apysc._lint_and_doc.document_text_split_util import Heading
    from apysc._lint_and_doc.document_text_split_util import \
        split_markdown_document
    markdown: str = file_util.read_txt(file_path=md_file_path)
    splitted_values: List[Union[Heading, BodyText, CodeBlock]] = \
        split_markdown_document(markdown_txt=markdown)
    for splitted_value in splitted_values:
        pass
