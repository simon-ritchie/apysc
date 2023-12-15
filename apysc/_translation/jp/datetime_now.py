"""This module is for the translation mapping data of the
following document:

Document file: datetime_now.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# DateTime class now interface": "# DateTime クラスの now インターフェイス",
    ##################################################
    "This page explains the `DateTime` class `now` method interface.": "このページでは`DateTime`クラスの`now`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `DateTime`'s `now` class method returns a current time `DateTime` instance.": "`DateTime`クラスの`now`のクラスメソッドは現在の時間での`DateTime`のインスタンスを返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `DateTime` class has the `now` method defined as a class method.": "`DateTime`クラスはクラスメソッドとして定義された`now`メソッドを持っています。",  # noqa
    ##################################################
    "It returns a `DateTime` instance, and its values become a current time.": "そのインターフェイスでは各値に現在時刻が設定された`DateTime`クラスのインスタンスを返却します。",  # noqa
    ##################################################
    "In the following example, if you click the rectangle, the click handler displays a current year, month, and day on the browser console.": "以下のコード例では、四角をクリックするとブラウザのコンソール上に現在の年月日を表示します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent, options: dict) -> None:\n    """\n    The handler to handle a rectangle\'s click event.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        An event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    now_datetime: ap.DateTime = ap.DateTime.now()\n    ap.trace("Current year:", now_datetime.year)\n    ap.trace("Current month:", now_datetime.month)\n    ap.trace("Current day:", now_datetime.day)\n\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=ap.Color("#0af"),\n)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="datetime_now_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(e: ap.MouseEvent, options: dict) -> None:\n    """\n    The handler to handle a rectangle\'s click event.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        An event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    now_datetime: ap.DateTime = ap.DateTime.now()\n    ap.trace("Current year:", now_datetime.year)\n    ap.trace("Current month:", now_datetime.month)\n    ap.trace("Current day:", now_datetime.day)\n\n\nap.Stage(\n    background_color=ap.Color("#333"),\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id="stage",\n)\nrectangle: ap.Rectangle = ap.Rectangle(\n    x=50,\n    y=50,\n    width=50,\n    height=50,\n    fill_color=ap.Color("#0af"),\n)\nrectangle.click(on_click)\n\nap.save_overall_html(dest_dir_path="datetime_now_basic_usage/")\n```',  # noqa
    ##################################################
    "## now class method API": "## now のクラスメソッドのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a `DateTime` instance of the current time.<hr>": "現在時刻が設定された`DateTime`クラスのインスタンスを取得します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    '- `variable_name_suffix`: str, default ""': '- `variable_name_suffix`: str, default ""',  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `dt`: DateTime": "- `dt`: DateTime",
    ##################################################
    "  - A created `DateTime` instance.": "  - 生成された`DateTime`クラスのインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> from datetime import datetime\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> py_now: datetime = datetime.now()\n>>> ap_now: ap.DateTime = ap.DateTime.now()\n>>> ap_now.year == py_now.year\nBoolean(True)\n\n>>> ap_now.month == py_now.month\nBoolean(True)\n\n>>> ap_now.day == py_now.day\nBoolean(True)\n```": "```py\n>>> from datetime import datetime\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> py_now: datetime = datetime.now()\n>>> ap_now: ap.DateTime = ap.DateTime.now()\n>>> ap_now.year == py_now.year\nBoolean(True)\n\n>>> ap_now.month == py_now.month\nBoolean(True)\n\n>>> ap_now.day == py_now.day\nBoolean(True)\n```",  # noqa
}
