<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_draw_ellipse.html)の確認をお願いします。</span>

# Graphics クラスの draw_ellipse インターフェイス

このページでは`Graphics`クラスの`draw_ellipse`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`draw_ellipse`インターフェイスは楕円のベクターグラフィックスを描画します。

## 基本的な使い方

`draw_ellipse`インターフェイスは`x`、`y`、`width`、`height`の各インターフェイスを持っています。`x`と`y`の引数は楕円の中央座標となります。`width`と`height`は楕円の幅と高さを決定します。これらのサイズは半径の倍の値（直径）で指定する必要があります。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=325, stage_height=200, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()

# Set the cyan fill color and draw the ellipse.
sprite.graphics.begin_fill(color="#0af")
sprite.graphics.draw_ellipse(x=125, y=100, width=150, height=100)

# Set the only dotted-line style and draw the ellipse.
sprite.graphics.begin_fill(color="")
sprite.graphics.line_style(
    color="#fff", thickness=3, dot_setting=ap.LineDotSetting(dot_size=3)
)
sprite.graphics.draw_ellipse(x=200, y=100, width=150, height=100)

ap.save_overall_html(dest_dir_path="graphics_draw_ellipse_basic_usage/")
```

<iframe src="static/graphics_draw_ellipse_basic_usage/index.html" width="325" height="200"></iframe>

## 返却値

`draw_ellipse`インターフェイスの返却値は`Ellipse`クラスのインスタンスとなります。

このクラスのインスタンスは他のグラフィックス系のクラスと同様に`x`や`y`、`width`などの基本的なインターフェイスを持っています。

以下のコード例ではクリックのイベントハンドラを設定しており、楕円をクリックするたびに幅と高さが大きくなるようにしています。

```py
# runnable
import apysc as ap


def on_ellipse_click(e: ap.MouseEvent[ap.Ellipse], options: dict) -> None:
    """
    The handler that the ellipse calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ellipse: ap.Ellipse = e.this
    ellipse.width += 15
    ellipse.height += 10


ap.Stage(
    background_color="#333", stage_width=250, stage_height=200, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color="#0af")
ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(x=125, y=100, width=150, height=100)
ellipse.click(on_ellipse_click)

ap.save_overall_html(dest_dir_path="graphics_draw_ellipse_return_value/")
```

<iframe src="static/graphics_draw_ellipse_return_value/index.html" width="250" height="200"></iframe>

## draw_ellipse API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `draw_ellipse(self, *, x: Union[int, apysc._type.int.Int], y: Union[int, apysc._type.int.Int], width: Union[int, apysc._type.int.Int], height: Union[int, apysc._type.int.Int], variable_name_suffix: str = '') -> '_ellipse.Ellipse'`<hr>

**[インターフェイス概要]** 楕円のベクターグラフィックスを描画します。<hr>

**[引数]**

- `x`: Int or int
  - 楕円の中央のX座標。

- `y`: Int or int
  - 楕円の中央のY座標。

- `width`: Int or int
  - 楕円の幅。

- `height`: Int or int
  - 楕円の高さ。

- `variable_name_suffix`: str, default ''
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[返却値]**

- `ellipse`: Ellipse
  - 作成された楕円のグラフィックスのインスタンス。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
...     x=100, y=100, width=100, height=50)
>>> ellipse.x
Int(100)

>>> ellipse.y
Int(100)

>>> ellipse.width
Int(100)

>>> ellipse.height
Int(50)

>>> ellipse.fill_color
String('#00aaff')
```