"""This module is for the translation mapping data of the
following document:

Document file: datetime_year.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# DateTime class year property": "# DateTime クラスの year 属性",
    ##################################################
    "This page explains the `DateTime` class's `year` property interface.": "このページでは`DateTime`クラスの`year`属性について説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `year` property gets or sets a year value.": "`year`属性は年の値の取得もしくは設定を行うことができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "A `DateTime` instance has its property interface.": "`DateTime`クラスのインスタンスがその属性のインターフェイスを持っています。",  # noqa
    ##################################################
    "Its getter interface returns a year's `Int` value.": "そのgetterインターフェイスは`Int`型の年の値を返却します。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)\nyear: ap.Int = datetime_.year\nassert year == 2022\n```": "```py\n# runnable\nimport apysc as ap\n\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)\nyear: ap.Int = datetime_.year\nassert year == 2022\n```",  # noqa
    ##################################################
    "Also, its setter interface accepts a year's `Int` value.": "また、`year`属性のsetterインターフェイスも同様に`Int`型の年の値を受け付けます。",  # noqa
    ##################################################
    "A for-digits number is acceptable (e.g., 2023).": "4桁の数字を受け付けることができます（例 : 2023）。",
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)\ndatetime_.year = ap.Int(2023)\nassert datetime_.year == 2023\n```": "```py\n# runnable\nimport apysc as ap\n\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)\ndatetime_.year = ap.Int(2023)\nassert datetime_.year == 2023\n```",  # noqa
    ##################################################
    "## year property API": "## year 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a current year's value.<hr>": "現在の年の値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `year`: Int": "- `year`: Int",
    ##################################################
    "  - A current year value.": "  - 現在の年の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)\n>>> datetime_.year\nInt(2022)\n\n>>> datetime_.year = ap.Int(2023)\n>>> datetime_.year\nInt(2023)\n```": "```py\n>>> import apysc as ap\n>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)\n>>> datetime_.year\nInt(2022)\n\n>>> datetime_.year = ap.Int(2023)\n>>> datetime_.year\nInt(2023)\n```",  # noqa
}
