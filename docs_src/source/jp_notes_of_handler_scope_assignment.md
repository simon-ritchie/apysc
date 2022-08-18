<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/notes_of_handler_scope_assignment.html)の確認をお願いします。</span>

# ハンドラスコープ内での変数割り当てに関する特記事項

このページでのハンドラスコープ内での変数割り当てに関する各特記事項について説明します。

## 変数割り当ての現在の制限

現在apyscライブラリではハンドラのスコープ内での基本的な型（例 : `ap.Int`や`ap.String`、`ap.Boolean`など）の値の変数割り当て（インスタンス化）をサポートしていません。

例えば以下のように、ハンドラスコープ内での`x: ap.Int = ap.Int(50)`といったようなコードは例外を発生させます:

```py
import apysc as ap


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    x: ap.Int = ap.Int(50)
    ap.trace("x:", x)


ap.Timer(handler=on_timer, delay=1000, repeat_count=1).start()
```

```
...
apysc._validation.handler_validation.InvalidAssignmentInHandler: Assigning values of basic types such as the ap.Int or ap.String to variables is not supported in a handler.

Instead, consider passing a predefined value to a second argument dictionary of a handler, or updating it via the `value` property.

E.g.,
x = options["x"]
x.value = ap.Int(...)
...
```

ハンドラのスコープ内で変数割り当てなどの制御を行いたい場合には以下のようにハンドラのスコープ外でその変数を作成し、その値をハンドラの`options`引数へ渡す対応等を検討してください:

```py
# runnable
import apysc as ap

from typing_extensions import TypedDict


class XOptions(TypedDict):
    x: ap.Int


def on_timer(e: ap.TimerEvent, options: XOptions) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : XOptions
        Optional arguments dictionary.
    """
    ap.trace("x:", options["x"])


options: XOptions = {"x": ap.Int(50)}
ap.Timer(handler=on_timer, delay=1000, repeat_count=1, options=options).start()
```

この制限はインスタンス化と変数割り当てが同時に実行される場合のみ対象となります。

そのため以下のコード（`x: ap.Int = options["x"]`）のような変数のインスタンス化を伴わない変数の割り当てなどは例外を発生させません:

```py
# runnable
import apysc as ap

from typing_extensions import TypedDict


class XOptions(TypedDict):
    x: ap.Int


def on_timer(e: ap.TimerEvent, options: XOptions) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : XOptions
        Optional arguments dictionary.
    """
    x: ap.Int = options["x"]
    ap.trace("x:", x)


options: XOptions = {"x": ap.Int(50)}
ap.Timer(handler=on_timer, delay=1000, repeat_count=1, options=options).start()
```

Pythonのビルトインの型など、apyscの基本的な値の型以外でも同様に例外を発生させません（例 : `x: int = 50`）:

```py
# runnable
import apysc as ap


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    x: int = 50
    ap.trace("x:", x)


ap.Timer(handler=on_timer, delay=1000, repeat_count=1).start()
```

ハンドラのスコープ内での変数の値の更新（例 : `x.value = ap.Int(100)`）も同様にエラーを発生させずに使用することができます:

```py
# runnable
import apysc as ap

from typing_extensions import TypedDict


class XOptions(TypedDict):
    x: ap.Int


def on_timer(e: ap.TimerEvent, options: XOptions) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : XOptions
        Optional arguments dictionary.
    """
    x: ap.Int = options["x"]
    x.value = ap.Int(100)
    ap.trace("x:", x)


options: XOptions = {"x": ap.Int(50)}
ap.Timer(handler=on_timer, delay=1000, repeat_count=1, options=options).start()
```