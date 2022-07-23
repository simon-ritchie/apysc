"""This module is for the translation mapping data of the
following document:

Document file: import_conventions.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# import conventions": "# import の慣習",
    ##################################################
    "The apysc library recommends using the `import apysc as ap` to import the package, like the `import numpy as np`\\, `import pandas as pd`\\, `import tkinter as tk`\\, or something like that.": "apyscのライブラリでは他のPythonパッケージの`import numpy as np`、`import pandas as pd`、`import tkinter as tk`などと同じように`import apysc as ap`というimportの指定を推奨しています。",  # noqa
    ##################################################
    "The root package module packages all interfaces you need (for instance, `Sprite`\\, `Int`\\, `Stage`).": "モジュールのルートのパッケージパスにapyscで利用が必要な各インターフェイスが設定されています（例 : `Sprite`、`Int`、`Stage`など）。",  # noqa
    ##################################################
    "Also, it packages internal logic modules with the underscore prefix like the `_file`\\. These packages are not necessary for you.": "また、パッケージの内部で使用するロジックの各モジュールは`_file`のようにアンダースコアのプレフィックスが設定されています。基本的にこれらのプレフィックスの付いたパッケージの利用は不要です。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nnumber_1: ap.Number = int_1 + ap.Number(10.5)\n```": "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nnumber_1: ap.Number = int_1 + ap.Number(10.5)\n```",  # noqa
}
