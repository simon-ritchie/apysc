<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](../en/display_object_visible.html)の確認をお願いします。</span>

# DisplayObject クラスの visible インターフェイス

このページでは`DisplayObject`クラスの`visible`属性のインターフェイスについて説明します。

## インターフェイス概要

`visible`属性は`DisplayObject`の表示・非表示の状態を切り替えます。

## 基本的な使い方

`visible`属性は`Boolean`の値を受け付けます。Trueを設定した場合その`DisplayObject`のインスタンスは表示状態になります（デフォルトの状態になります）。Falseを設定するとその`DisplayObject`のインスタンスは非表示になります。

以下のコード例では四角をクリックした時にvisibleの設定を切り替えています。左側の四角をクリックした際には左側の四角は非表示となり、右側に別の四角が表示されます。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_rectangle_1_click(
        e: ap.MouseEvent[ap.Rectangle], options: _RectOptions) -> None:
    """
    The handler that the first rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle_1: ap.Rectangle = e.this
    rectangle_2: ap.Rectangle = options['rectangle']
    rectangle_1.visible = ap.Boolean(False)
    rectangle_2.visible = ap.Boolean(True)


def on_rectangle_2_click(
        e: ap.MouseEvent[ap.Rectangle], options: _RectOptions) -> None:
    """
    The handler that the second rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle_1: ap.Rectangle = options['rectangle']
    rectangle_2: ap.Rectangle = e.this
    rectangle_1.visible = ap.Boolean(True)
    rectangle_2.visible = ap.Boolean(False)


ap.Stage(
    background_color='#333',
    stage_width=250,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color='#0af')
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

sprite.graphics.begin_fill(color='#f0a')
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
rectangle_2.visible = ap.Boolean(False)

options: _RectOptions = {'rectangle': rectangle_2}
rectangle_1.click(
    on_rectangle_1_click, options=options)
options = {'rectangle': rectangle_1}
rectangle_2.click(
    on_rectangle_2_click, options=options)

ap.save_overall_html(
    dest_dir_path='display_object_visible_basic_usage/')
```

<iframe src="static/display_object_visible_basic_usage/index.html" width="250" height="150"></iframe>

## visible 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** このインスタンスの表示・非表示の状態の値を取得します。<hr>

**[返却値]**

- `result`: Boolean
  - もしこのインスタンスが表示状態であればTrueとなります。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.visible = ap.Boolean(False)
>>> rectangle.visible
Boolean(False)
```