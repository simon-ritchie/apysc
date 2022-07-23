<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics.html)の確認をお願いします。</span>

# Graphics クラス

このページでは`Graphics`クラスについて説明します。

## Graphics クラスの概要

`Graphics`クラスは各ベクターグラフィックスの描画のインターフェイスを扱うクラスです。このインターフェイスには四角の描画や線の描画など様々なインターフェイスが存在します。

`Sprite`クラスなどのインスタンスはこの`Graphics`クラスのインスタンスを内部で生成します。

## Sprite のインスタンスを経由した各インターフェイスの呼び出し

Sprite のインスタンスは`graphics`属性を持っており、その属性を使用して各描画のインターフェイスを呼び出すことができます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=250, stage_height=180, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()

# Draw the white border and cyan color rectangle.
sprite.graphics.line_style(color="#fff", thickness=5)
sprite.graphics.begin_fill(color="#0af")
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

# Draw the magenta color polyline.
sprite.graphics.begin_fill(color="")
sprite.graphics.line_style(color="#f0a", thickness=5)
sprite.graphics.move_to(x=150, y=50)
sprite.graphics.line_to(x=200, y=50)
sprite.graphics.line_to(x=150, y=100)
sprite.graphics.line_to(x=200, y=100)

# Draw the dashed line.
sprite.graphics.draw_dashed_line(
    x_start=50, y_start=130, x_end=200, y_end=130, dash_size=10, space_size=5
)

ap.save_overall_html(dest_dir_path="graphics_call_interfaces_from_sprite_instance/")
```

<iframe src="static/graphics_call_interfaces_from_sprite_instance/index.html" width="250" height="180"></iframe>

## 各返却値について

各インターフェイスは`Rectangle`や`Polyline`クラスなどの生成されたグラフィックスのインスタンスを返却します。これらのインスタンスはxやy、fill_alpha、visibleなどの基本的な`DisplayObject`クラスの各属性やメソッドなどを持っています。

例えば以下のコード例のようにこれらのインスタンスに対してイベントを設定して座標の更新処理などを設定することができます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=200, stage_elem_id="stage"
)

sprite: ap.Sprite = ap.Sprite()


def on_rectangle_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
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

    # Update the coordinates, fill alpha, and fill color.
    rectangle.x = ap.Int(100)
    rectangle.y = ap.Int(100)
    rectangle.fill_alpha = ap.Number(0.5)
    rectangle.fill_color = ap.String("#f0a")


# drew_rect interface will return Rectangle instance.
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

# Bind click event to the rectangle.
rectangle.click(on_rectangle_click)

ap.save_overall_html(dest_dir_path="graphics_return_values/")
```

もし以下の四角をクリックすると座標値や塗りの色、透明度などの値が更新されます。

<iframe src="static/graphics_return_values/index.html" width="200" height="200"></iframe>

## 関連資料

- [Graphics クラスの begin_fill (塗りの設定)のインターフェイス](jp_graphics_begin_fill.md)
- [Graphics クラスの line_style (線のスタイル設定)のインターフェイス](jp_graphics_line_style.md)

- [Graphics クラスの draw_rect (四角の描画)のインターフェイス](jp_graphics_draw_rect.md)
- [Graphics クラスの draw_round_rect (角丸の四角の描画)のインターフェイス](jp_graphics_draw_round_rect.md)

- [Graphics クラスの draw_circle (円の描画)のインターフェイス](jp_graphics_draw_circle.md)
- [Graphics クラスの draw_ellipse (楕円描画) のインターフェイス](jp_graphics_draw_ellipse.md)

- [Graphics クラスの move_to (線の描画位置の変更)と line_to (指定座標への線の描画)のインターフェイス](jp_graphics_move_to_and_line_to.md)
- [Graphics クラスの draw_line (線の描画)のインターフェイス](jp_graphics_draw_line.md)

- [Graphics クラスの draw_dotted_line (点線の描画)のインターフェイス](jp_graphics_draw_dotted_line.md)
- [Graphics クラスの draw_dashed_line (破線の描画)のインターフェイス](jp_graphics_draw_dashed_line.md)

- [Graphics クラスの draw_round_dotted_line (点線(丸)の描画)のインターフェイス](jp_graphics_draw_round_dotted_line.md)
- [Graphics クラスの draw_dash_dotted_line (一点鎖線の描画)のインターフェイス](jp_graphics_draw_dash_dotted_line.md)

- [Graphics クラスの draw_polygon (多角形描画)のインターフェイス](jp_graphics_draw_polygon.md)