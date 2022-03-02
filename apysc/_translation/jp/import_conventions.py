"""This module is for the translation mapping data of the
following document:

Document file: import_conventions.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Import conventions':
    '',

    'The apysc library recommends using the `import apysc as ap` to import the package, like the `import numpy as np`\\, `import pandas as pd`\\, `import tkinter as tk`\\, or something like that.\n\nThe root package module packages all interfaces you need (for instance, `Sprite`\\, `Int`\\, `Stage`).\n\nAlso, it packages internal logic modules with the underscore prefix like the `_file`\\. These packages are not necessary for you.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nnumber_1: ap.Number = int_1 + ap.Number(10.5)\n```':  # noqa
    '',

}
