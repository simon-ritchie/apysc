<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/unbind_enter_frame_and_unbind_enter_frame_all.html)の確認をお願いします。</span>

# unbind_enter_frame と unbind_enter_frame_all の各インターフェイス

このページでは`unbind_enter_frame`と`unbind_enter_frame_all`メソッドの各インターフェイスについて説明します。

## 各インターフェイスの概要

`unbind_enter_frame`と`unbind_enter_frame_all`メソッドの各インターフェイスはenter frameイベントのハンドラ設定を取り除きます。

`unbind_enter_frame`インターフェイスは指定された一つのハンドラを無効化し、`unbind_enter_frame_all`インターフェイスはすべてのハンドラ設定を無効化します。

## 基本的な使い方

`unbind_enter_frame`インターフェイスは`handler`引数の指定を必要とします。

加えて、このインターフェイスはもし指定されたハンドラがまだ未設定だった場合にはエラーとなります。

以下の例では、四角をクリックした際にenter frameのイベントを無効化しています。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color="#333",
    stage_elem_id="stage",
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, fill_color="#0af"
)


def on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:
    """
    The handler to handle an enter frame event.

    Parameters
    ----------
    e : ap.EnterFrameEvent
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    rectangle.rotation_around_center += 1


def on_rectangle_click(
    e: ap.MouseEvent[ap.Rectangle],
    options: dict,
) -> None:
    """
    The handler to handle a rectangle click event.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    stage.unbind_enter_frame(handler=on_enter_frame)


stage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)
rectangle.click(handler=on_rectangle_click)
ap.save_overall_html(dest_dir_path="unbind_enter_frame_basic_usage/")
```

<iframe src="static/unbind_enter_frame_basic_usage/index.html" width="150" height="150"></iframe>

`unbind_enter_frame_all`インターフェイスは引数の指定を必要としません。

以下の例では四角をクリックした際にすべてのenter frameのイベントを無効化しています。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=250,
    stage_height=150,
    background_color="#333",
    stage_elem_id="stage",
)
left_rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, fill_color="#0af"
)
right_rectangle: ap.Rectangle = ap.Rectangle(
    x=150, y=50, width=50, height=50, fill_color="#f0a"
)


def on_enter_frame_1(e: ap.EnterFrameEvent, options: dict) -> None:
    """
    The handler to handle an enter frame event.

    Parameters
    ----------
    e : ap.EnterFrameEvent
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    left_rectangle.rotation_around_center += 1


def on_enter_frame_2(e: ap.EnterFrameEvent, options: dict) -> None:
    """
    The handler to handle an enter frame event.

    Parameters
    ----------
    e : ap.EnterFrameEvent
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    right_rectangle.rotation_around_center -= 1


def on_rectangle_click(e: ap.MouseEvent, options: dict) -> None:
    """
    The handler to handle a rectangle click event.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    stage.unbind_enter_frame_all()


stage.enter_frame(handler=on_enter_frame_1, fps=ap.FPS.FPS_30)
stage.enter_frame(handler=on_enter_frame_2, fps=ap.FPS.FPS_30)
left_rectangle.click(handler=on_rectangle_click)
right_rectangle.click(handler=on_rectangle_click)

ap.save_overall_html(dest_dir_path="unbind_enter_frame_all_basic_usage/")
```

<iframe src="static/unbind_enter_frame_all_basic_usage/index.html" width="250" height="150"></iframe>

## 関連資料

- [enter_frame インターフェイス](jp_enter_frame.md)

## unbind_enter_frame のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unbind_enter_frame(self, handler: Callable[[apysc._event.enter_frame_event.EnterFrameEvent, ~_Options], NoneType]) -> None`<hr>

**[インターフェイス概要]**

指定されたハンドラのenter-frameイベントの設定を解除します。<hr>

**[引数]**

- `handler`: Callable[[EnterFrameEvent, _Options], None]
  - 設定を取り除く対象のcallableオブジェクト。

<hr>

**[エラー発生条件]**

- _EnterFrameEventNotRegistered: もし指定されたハンドラの設定削除対象が存在しない場合。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=50, y=50, width=50, height=50, fill_color="#0af"
... )
>>> def on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:
...     rectangle.x += 1
>>> stage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)
>>> # Any implementations here...
>>> stage.unbind_enter_frame(handler=on_enter_frame)
```

## unbind_enter_frame_all のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unbind_enter_frame_all(self) -> None`<hr>

**[インターフェイス概要]**

すべてのenter-frameイベントの設定を解除します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=50, y=50, width=50, height=50, fill_color="#0af"
... )
>>> def on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:
...     rectangle.x += 1
>>> stage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)
>>> # Any implementations here...
>>> stage.unbind_enter_frame_all()
```