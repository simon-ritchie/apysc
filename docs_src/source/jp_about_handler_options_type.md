<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](about_handler_options_type.md)の確認をお願いします。</span>

# ハンドラのoptions引数の型について

このページではイベントハンドラの`options`引数の型について説明します。

## options引数には辞書の型を受け付けることができます

以下のコードサンプルのように`options`引数は辞書の型の値を受け付けることができます。

```py
# runnable
from typing import Dict

import apysc as ap


def on_timer(e: ap.TimerEvent, options: Dict[str, str]) -> None:
    """
    The handler that a timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace(options['msg'])


timer: ap.Timer = ap.Timer(on_timer, delay=1000, options={'msg': 'Hello!'})
timer.start()
```

## TypedDictを使った型アノテーションについて

通常の辞書の代わりに`TypedDict`を使った型アノテーションは可読性の向上に役立つことがあります。apyscではoptions引数にTypedDictによる型アノテーションをサポートしており、実際に渡したoptionsの辞書の型とハンドラのTypedDictによるアノテーション間で型チェックを行うことができます。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _MsgOptions(TypedDict):
    msg: str


def on_timer(e: ap.TimerEvent, options: _MsgOptions) -> None:
    """
    The handler that a timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace(options['msg'])


options: _MsgOptions = {'msg': 'Hello!'}
timer: ap.Timer = ap.Timer(on_timer, delay=1000, options=options)
timer.start()
```

特記事項: もしPython3.8もしくはそれ以降のPythonバージョンをお使いの場合には`typing_extensions`パッケージの代わりに`typing`パッケージから`TypedDict`をimportすることができます（例 : `from typing import TypedDict`）。