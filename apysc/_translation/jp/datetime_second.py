"""This module is for the translation mapping data of the
following document:

Document file: datetime_second.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# DateTime class second property": "# DateTime クラスの second 属性",
    ##################################################
    "This page explains the `DateTime` class's `second` property interface.": "このページでは`DateTime`クラスの`second`属性のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `second` property gets or sets a second value.": "`second`属性では秒の値の取得もしくは設定を行うことができます。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "A `DateTime` instance has its property interface.": "`DateTime`クラスのインスタンスがその属性のインターフェイスを持っています。",  # noqa
    ##################################################
    "Its getter interface returns a second's `Int` value.": "そのインターフェイスのgetterでは`Int`型の秒の値を返却します。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, second=30)\nsecond: ap.Int = datetime_.second\nassert second == 30\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, second=30)\nsecond: ap.Int = datetime_.second\nassert second == 30\n```",  # noqa
    ##################################################
    "Also, its setter interface accepts a second's `Int` value.": "また、setterのインターフェイスでは同様に`Int`型の秒の値を受け付けます。",  # noqa
    ##################################################
    "0-59 integer is acceptable.": "0～59の整数を受け付けることができます。",
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, second=30)\ndatetime_.second = ap.Int(50)\nassert datetime_.second == 50\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ndatetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, second=30)\ndatetime_.second = ap.Int(50)\nassert datetime_.second == 50\n```",  # noqa
    ##################################################
    "## second property API": "## second 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a current second's value.<hr>": "現在の秒の値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `second`: Int": "- `second`: Int",
    ##################################################
    "  - A current second value.": "  - 現在の秒の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1, second=30)\n>>> datetime_.second\nInt(30)\n\n>>> datetime_.second = ap.Int(50)\n>>> datetime_.second\nInt(50)\n```": "```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1, second=30)\n>>> datetime_.second\nInt(30)\n\n>>> datetime_.second = ap.Int(50)\n>>> datetime_.second\nInt(50)\n```",  # noqa
}
