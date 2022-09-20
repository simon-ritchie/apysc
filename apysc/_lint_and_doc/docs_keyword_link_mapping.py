"""The module to define keyword link mappings.
"""

from typing import Dict


_Keyword = str
_DocFileName = str

MAPPINGS: Dict[_Keyword, _DocFileName] = {
    "Stage": "stage",
    "Sprite": "sprite",
    "save_overall_html": "save_overall_html",
}
