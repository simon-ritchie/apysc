"""This module is for the translation mapping data of the
following document:

Document file: datetime_hour.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# DateTime class hour property": "# DateTime クラスの hour 属性",
    ##################################################
    "This page explains the `DateTime` class's `hour` property interface.": "このページでは`DateTime`クラスの`hour`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `hour` property gets or sets an hour value.": "`hour`属性では時間の値の取得もしくは設定を行うことができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "A `DateTime` instance has its property interface.": "`DateTime`クラスのインスタンスがその属性のインターフェイスを持っています。",  # noqa
    ##################################################
    "Its getter interface returns an hour's `Int` value.": "そのインターフェイスのgetterでは`Int`型の時間の値を返却します。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, hour=10)\nhour: ap.Int = datetime_.hour\nassert hour == 10\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, hour=10)\nhour: ap.Int = datetime_.hour\nassert hour == 10\n```",  # noqa
    ##################################################
    "Also, its setter interface accepts an hour's `Int` value.": "また、setterのインターフェイスでは同様に`Int`型の値を受け付けます。",  # noqa
    ##################################################
    "0-23 integer is acceptable.": "0～23の整数を受け付けることができます。",
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, hour=10)\ndatetime_.hour = ap.Int(15)\nassert datetime_.hour == 15\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, hour=10)\ndatetime_.hour = ap.Int(15)\nassert datetime_.hour == 15\n```",  # noqa
    ##################################################
    "## hour property API": "## hour 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a current hour's value.<hr>": "現在の時間の値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `hour`: Int": "- `hour`: Int",
    ##################################################
    "  - A current hour value.": "  - 現在の時間の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1, hour=5)\n>>> datetime_.hour\nInt(5)\n\n>>> datetime_.hour = ap.Int(10)\n>>> datetime_.hour\nInt(10)\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1, hour=5)\n>>> datetime_.hour\nInt(5)\n\n>>> datetime_.hour = ap.Int(10)\n>>> datetime_.hour\nInt(10)\n```",  # noqa
}
