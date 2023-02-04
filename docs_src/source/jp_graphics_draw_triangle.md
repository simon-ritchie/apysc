<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_draw_triangle.html)の確認をお願いします。</span>

# Graphics クラスの draw_triangle インターフェイス

このページでは`Graphics`クラスの`draw_triangle`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`draw_triangle`インターフェイスは三角形のベクターグラフィックスを描画します。

## 基本的な使い方

`draw_triangle`インターフェイスは`x1`, `y1`, `x2`, `y2`, `x3`, `y3`の各引数の指定を必要とします。

`x1`と`y1`の引数は三角形の1つ目の頂点の座標となります。

`x2`と`y2`は2つ目の頂点の座標となり、`x3`と`y3`は3つ目の頂点の座標となりま。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
triangle: ap.Triangle = sprite.graphics.draw_triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
)

ap.save_overall_html(dest_dir_path="./graphics_draw_triangle_basic_usage/")
```

<iframe src="static/graphics_draw_triangle_basic_usage/index.html" width="150" height="150"></iframe>

## Triangle インスタンス

`draw_triangle`インターフェイスは`Triangle`クラスのインスタンスを返却します。

そのインスタンスを使って各種設定を更新したりイベントの設定などを行うことができます。

例えば、以下の例では`Triangle`のインスタンスにマウスイベントを設定し、`on_click`のハンドラ内でX座標の更新を行っています:

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent[ap.Triangle], options: dict) -> None:
    """
    The handler for the click event.

    Parameters
    ----------
    e : ap.MouseEvent[ap.Rectangle]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    triangle: ap.Triangle = e.this
    triangle.x += 2


ap.Stage(
    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
triangle: ap.Triangle = sprite.graphics.draw_triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
)
triangle.click(handler=on_click)

ap.save_overall_html(dest_dir_path="./graphics_draw_triangle_triangle_instance/")
```

<iframe src="static/graphics_draw_triangle_triangle_instance/index.html" width="150" height="150"></iframe>

## draw_triangle のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `draw_triangle(self, *, x1: Union[int, apysc._type.int.Int], y1: Union[int, apysc._type.int.Int], x2: Union[int, apysc._type.int.Int], y2: Union[int, apysc._type.int.Int], x3: Union[int, apysc._type.int.Int], y3: Union[int, apysc._type.int.Int], variable_name_suffix: str = '') -> apysc._display.triangle.Triangle`<hr>

**[インターフェイス概要]**

三角形のベクターグラフィックスを描画します。<hr>

**[引数]**

- `x1`: Union[int, Int]
  - 1つ目の頂点のX座標。

- `y1`: Union[int, Int]
  - 1つ目の頂点のY座標。

- `x2`: Union[int, Int]
  - 2つ目の頂点のX座標。

- `y2`: Union[int, Int]
  - 2つ目の頂点のY座標。

- `x3`: Union[int, Int]
  - 3つ目の頂点のX座標。

- `y3`: Union[int, Int]
  - 3つ目の頂点のY座標。

- `variable_name_suffix`: str, optional
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `triangle`: Triangle
  - 生成された三角形のグラフィックスのインスタンス。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af", alpha=0.7)
>>> sprite.graphics.line_style(color="#fff", thickness=5, alpha=0.5)
>>> triangle: ap.Triangle = sprite.graphics.draw_triangle(
...     x1=75,
...     y1=50,
...     x2=25,
...     y2=100,
...     x3=100,
...     y3=100,
... )
>>> triangle.x1
Int(75)

>>> triangle.y1 = ap.Int(30)
>>> triangle.y1
Int(30)

>>> triangle.fill_color
String('#00aaff')
```

<hr>

**[関連資料]**

- [Triangle クラス](https://simon-ritchie.github.io/apysc/jp/jp_triangle.html)