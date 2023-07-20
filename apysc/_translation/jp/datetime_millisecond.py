"""This module is for the translation mapping data of the
following document:

Document file: datetime_millisecond.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# DateTime class millisecond property": "# DateTime クラスの millisecond 属性",
    ##################################################
    "This page explains the `DateTime` class's `millisecond` property interface.": "このページでは`DateTime`クラスの`millisecond`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `millisecond` property gets or sets a millisecond value.": "`millisecond`属性ではミリ秒の値の取得もしくは設定を行うことができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "A `DateTime` instance has its property interface.": "`DateTime`クラスのインスタンスがその属性のインターフェイスを持っています。",  # noqa
    ##################################################
    "Its getter interface returns a millisecond's `Int` value.": "そのインタ費フェイスのgetterでは`Int`型のミリ秒の値を返却します。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, millisecond=500)\nmillisecond: ap.Int = datetime_.millisecond\nassert millisecond == 500\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, millisecond=500)\nmillisecond: ap.Int = datetime_.millisecond\nassert millisecond == 500\n```",  # noqa
    ##################################################
    "Also, its setter interface accepts a millisecond's `Int` value.": "また、setter側のインターフェイスでは同様に`Int`型の値を受け付けます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, millisecond=500)\ndatetime_.millisecond = ap.Int(300)\nassert datetime_.millisecond == 300\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, millisecond=500)\ndatetime_.millisecond = ap.Int(300)\nassert datetime_.millisecond == 300\n```",  # noqa
    ##################################################
    "## millisecond property API": "## millisecond 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a current millisecond value.<hr>": "現在のミリ秒の値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `millisecond`: Int": "- `millisecond`: Int",
    ##################################################
    "  - A current millisecond value.": "  - 現在のミリ秒の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> datetime_: ap.DateTime = ap.DateTime(\n...     year=2022, month=12, day=1, millisecond=500\n... )\n>>> datetime_.millisecond\nInt(500)\n\n>>> datetime_.millisecond = ap.Int(300)\n>>> datetime_.millisecond\nInt(300)\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> datetime_: ap.DateTime = ap.DateTime(\n...     year=2022, month=12, day=1, millisecond=500\n... )\n>>> datetime_.millisecond\nInt(500)\n\n>>> datetime_.millisecond = ap.Int(300)\n>>> datetime_.millisecond\nInt(300)\n```",  # noqa
}
