<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](num_children.md)の確認をお願いします。</span>

# num_children インターフェイス

このページでは`Graphics`や`Sprite`、`Stage`などのコンテナのクラスの`num_children`属性のインターフェイスについて説明します。

## インターフェイス概要

`num_children`属性のインターフェイスは子の数の`Int`型の整数の値を返却します。

## 特記事項

`Sprite`インスタンスの初期値は`graphics`インスタンスの子を持つため0ではなく1になっています。

## 基本的な使い方

`num_children`属性は`Int`型の整数の子の数を返却します。その値を使って座標の計算などを行うことができます。

以下のコード例では四角をクリックした際に新しい四角を追加しています。`num_children`属性の値は新しい四角のX座標を決めるのに使われています。また、このコードではクリックされた際に現在の`num_children`属性の値をブラウザのコンソールに表示しています（F12キーを押してコンソールを開いて確認してください）。

```py
# runnable
import apysc as ap


def on_sprite_click(
        e: ap.MouseEvent[ap.Sprite], options: dict) -> None:
    """
    The handler that the sprite calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    sprite: ap.Sprite = e.this
    rectangle_x: ap.Int = (sprite.num_children - 1) * 100 + 50
    new_rect: ap.Rectangle = sprite.graphics.draw_rect(
        x=rectangle_x,
        y=50, width=50, height=50)
    sprite.add_child(new_rect)
    ap.trace(
        'Current sprite children number:', sprite.num_children,
        'rectangle x:', rectangle_x)


ap.Stage(
    background_color='#333',
    stage_width=450,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
sprite.add_child(rectangle_1)
sprite.click(on_sprite_click)

ap.save_overall_html(
    dest_dir_path='num_children_basic_usage/')
```

<iframe src="static/num_children_basic_usage/index.html" width="450" height="150"></iframe>

## num_children API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** 現在の子の数を取得します。<hr>

**[返却値]**

- `num_children`: int
  - 現在の子の数。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
...     x=150, y=50, width=50, height=50)
>>> sprite.graphics.num_children
Int(2)
```