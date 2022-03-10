<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](./docs_src/source/sprite.md)の確認をお願いします。</span>

# Sprite

このページでは、`Sprite`クラスについて説明します。

## Spriteとは？

`Sprite`クラスは、各`DisplayObject`インスタンスのコンテナです。また、`Graphics`クラスのインタフェースを持ち、各ベクターグラフィックを描画することができます。

## インスタンスの自動追加に関する注意点

`Sprite`のインスタンスは自動的にステージに追加されます（`add_child`などの関連インタフェースを呼び出す必要はありません）。一方で、もし他のインスタンスに`Sprite`のインスタンスを追加したいと場合、手動で `add_child` メソッドを呼び出す必要があります。

## graphics属性のインタフェース

`Sprite`クラスのインスタンスは`graphics`属性を持っており、それを使って各ベクターグラフィックを描画することができます。例えば以下のコードでは水色の四角を描画します。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='sprite_graphics_attribute/')
```

<iframe src="static/sprite_graphics_attribute/index.html" width="150" height="150"></iframe>

詳細は以下の`Graphics`クラスの関連ドキュメントをご覧ください。

- [Graphicsクラス](jp_graphics.md)

- [Graphicsクラス begin_fill インターフェイス](jp_graphics_begin_fill.md)

- [Graphicsクラス line_style インターフェイス](jp_graphics_line_style.md)

- [Graphicsクラス draw_rect インターフェイス](jp_graphics_draw_rect.md)

- [Graphicsクラス draw_circle インターフェイス](jp_graphics_draw_circle.md)

## DisplayObjectの複数のインスタンスの移動について

`Sprite`クラスはコンテナであり、その座標を移動させると同時に子のインスタンスの座標も変更されます。例えば以下のコードでは四角をクリックするとSpriteのy座標が変化します（子の各四角形が一通り移動します）。

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
    sprite.y += 50


ap.Stage(
    background_color='#333',
    stage_width=250,
    stage_height=250,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)
sprite.click(on_sprite_click)

ap.save_overall_html(
    dest_dir_path='sprite_move_instances_simultaneously/')
```

<iframe src="static/sprite_move_instances_simultaneously/index.html" width="250" height="250"></iframe>

以降のページでは`add_child`のインターフェースなど、Spriteクラスの他のインターフェースについて説明していきます。

## 関連資料

- [add_child と remove_child インターフェイス](jp_add_child_and_remove_child.md)

- [contains インターフェイス](jp_contains.md)

- [num_children インターフェイス](jp_num_children.md)

- [get_child_at インターフェイス](jp_get_child_at.md)

## SpriteクラスのコンストラクタAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, *, variable_name:Union[str, NoneType]=None) -> None`<hr>

**[インターフェイス概要]** 子を持つことのできる基本的な表示要素用のオブジェクトを生成します。

**[引数]**

- `variable_name`: str or None, default None
  - このインスタンスのJavaScriptで使用するための変数名です。Spriteクラスのサブクラスを使う場合を除いてこの引数の指定は不要です。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite_1: ap.Sprite = ap.Sprite()
>>> # Create the sprite child rectangle
>>> sprite_1.graphics.begin_fill(color='#0af')
>>> rect: ap.Rectangle = sprite_1.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> sprite_1.graphics.contains(rect)
Boolean(True)

>>> # Move the created rectangle to the other sprite
>>> sprite_2: ap.Sprite = ap.Sprite()
>>> sprite_2.add_child(rect)
>>> sprite_1.graphics.contains(rect)
Boolean(False)

>>> sprite_2.contains(rect)
Boolean(True)

>>> # Move the sprite container
>>> sprite_2.x = ap.Int(50)
>>> sprite_2.x
Int(50)
```