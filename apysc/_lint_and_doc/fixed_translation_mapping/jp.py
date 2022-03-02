"""This module is for the Japanese fixed-translation mappings
settings.
"""

from apysc._lint_and_doc.fixed_translation_mapping.data_model import Mapping
from apysc._lint_and_doc.fixed_translation_mapping.data_model import Mappings

MAPPINGS: Mappings = Mappings(
    mappings=[
        Mapping(
            key='## See also',
            value='## 関連資料'),
        Mapping(
            key='**[Parameters]**',
            value='**[引数]**'),
        Mapping(
            key='**[Returns]**',
            value='**[返却値]**'),
        Mapping(
            key='**[Parameters]**',
            value='**[引数]**'),
        Mapping(
            key='**[Examples]**',
            value='**[コードサンプル]**'),
        Mapping(
            key='**[References]**',
            value='**[関連資料]**'),
    ])
