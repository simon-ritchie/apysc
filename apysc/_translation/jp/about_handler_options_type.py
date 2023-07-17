"""This module is for the translation mapping data of the
following document:

Document file: about_handler_options_type.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# About the handler options' type": "# ハンドラのoptions引数の型について",
    ##################################################
    "This page explains the event handler `options` argument's type.": "このページではイベントハンドラの`options`引数の型について説明します。",  # noqa
    ##################################################
    "## The dictionary type is acceptable": "## options引数には辞書の型を受け付けることができます",
    ##################################################
    "Each handler's `options` argument can accept a dictionary type value, like the following:": "以下のコードサンプルのように`options`引数は辞書の型の値を受け付けることができます。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing import Dict\n\nimport apysc as ap\n\n\ndef on_timer(e: ap.TimerEvent, options: Dict[str, str]) -> None:\n    """\n    The handler that a timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace(options["msg"])\n\n\ntimer: ap.Timer = ap.Timer(on_timer, delay=1000, options={"msg": "Hello!"})\ntimer.start()\n```': '```py\n# runnable\nfrom typing import Dict\n\nimport apysc as ap\n\n\ndef on_timer(e: ap.TimerEvent, options: Dict[str, str]) -> None:\n    """\n    The handler that a timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace(options["msg"])\n\n\ntimer: ap.Timer = ap.Timer(on_timer, delay=1000, options={"msg": "Hello!"})\ntimer.start()\n```',  # noqa
    ##################################################
    "## About the TypedDict annotation": "## TypedDictを使った型アノテーションについて",
    ##################################################
    "Sometimes using the `TypedDict` type annotation instead of the `dict` type annotation is helpful and makes it easy to read the code. The apysc check a handler options annotation and the actual options value type when you use the `TypedDict`\\.": "通常の辞書の代わりに`TypedDict`を使った型アノテーションは可読性の向上に役立つことがあります。apyscではoptions引数にTypedDictによる型アノテーションをサポートしており、実際に渡したoptionsの辞書の型とハンドラのTypedDictによるアノテーション間で型チェックを行うことができます。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _MsgOptions(TypedDict):\n    msg: str\n\n\ndef on_timer(e: ap.TimerEvent, options: _MsgOptions) -> None:\n    """\n    The handler that a timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace(options["msg"])\n\n\noptions: _MsgOptions = {"msg": "Hello!"}\ntimer: ap.Timer = ap.Timer(on_timer, delay=1000, options=options)\ntimer.start()\n```': '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\n\nclass _MsgOptions(TypedDict):\n    msg: str\n\n\ndef on_timer(e: ap.TimerEvent, options: _MsgOptions) -> None:\n    """\n    The handler that a timer calls.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace(options["msg"])\n\n\noptions: _MsgOptions = {"msg": "Hello!"}\ntimer: ap.Timer = ap.Timer(on_timer, delay=1000, options=options)\ntimer.start()\n```',  # noqa
    ##################################################
    "Notes: if you are using a Python 3.8 or later version, then importing the `TypedDict` from the `typing` package instead of the `typing_extensions` is available (e.g., `from typing import TypedDict`).": "特記事項: もしPython3.8もしくはそれ以降のPythonバージョンをお使いの場合には`typing_extensions`パッケージの代わりに`typing`パッケージから`TypedDict`をimportすることができます（例 : `from typing import TypedDict`）。",  # noqa
}
