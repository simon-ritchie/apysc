<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/display_object_x_and_y.html)の確認をお願いします。</span>

# DisplayObject クラスの x と y のインターフェイス

このページでは`DisplayObject`クラスのxとy属性のインターフェイスについて説明します。

## 各インターフェイスの概要

xとy属性は`DisplayObject`のインスタンスの2次元の座標位置を変更します。

## 基本的な使い方

`DisplayObject`の各インスタンスはxとy属性を持っており、それを参照して座標値の取得と更新を行うことができます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=0, y=0, width=50, height=50)

# Update the x and y coordinates from 0 to 50.
rectangle.x = ap.Int(50)
rectangle.y = ap.Int(50)

ap.save_overall_html(dest_dir_path="display_object_x_and_y_basic_usage/")
```

<iframe src="static/display_object_x_and_y_basic_usage/index.html" width="150" height="150"></iframe>

## 累算代入演算

xとy属性は`+=`や`-=`、`/=`、`*=`の累算代入演算をサポートしています。

以下のコード例では四角をクリックする度に10pxずつY座標を加算しています。

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.y += 10


ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(dest_dir_path="display_object_x_and_y_augmented_assignment/")
```

<iframe src="static/display_object_x_and_y_augmented_assignment/index.html" width="150" height="150"></iframe>

## x属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

X座標を取得します。<hr>

**[返却値]**

- `x`: Int
  - X座標。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> rectangle.x = ap.Int(100)
>>> rectangle.x
Int(100)
```

## y属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

Y座標を取得します。<hr>

**[返却値]**

- `y`: Int
  - Y座標。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> rectangle.y = ap.Int(100)
>>> rectangle.y
Int(100)
```