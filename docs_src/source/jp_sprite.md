<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/sprite.html)の確認をお願いします。</span>

# Spriteクラス

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
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

ap.save_overall_html(dest_dir_path="sprite_graphics_attribute/")
```

<iframe src="static/sprite_graphics_attribute/index.html" width="150" height="150"></iframe>

詳細は以下の`Graphics`クラスの関連ドキュメントをご覧ください。

- [Graphics クラス](jp_graphics.md)
- [Graphics クラス begin_fill （塗り設定）のインターフェイス](jp_graphics_begin_fill.md)

- [Graphics クラス line_style （線設定）のインターフェイス](jp_graphics_line_style.md)
- [Graphics クラス draw_rect （四角描画）のインターフェイス](jp_graphics_draw_rect.md)

- [Graphics クラス draw_circle （円描画）のインターフェイス](jp_graphics_draw_circle.md)

## DisplayObjectの複数のインスタンスの移動について

`Sprite`クラスはコンテナであり、その座標を移動させると同時に子のインスタンスの座標も変更されます。例えば以下のコードでは四角をクリックするとSpriteのy座標が変化します（子の各四角形が一通り移動します）。

```py
# runnable
import apysc as ap


def on_sprite_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:
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
    background_color=ap.Color("#333"),
    stage_width=250,
    stage_height=250,
    stage_elem_id="stage",
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)
sprite.click(on_sprite_click)

ap.save_overall_html(dest_dir_path="sprite_move_instances_simultaneously/")
```

<iframe src="static/sprite_move_instances_simultaneously/index.html" width="250" height="250"></iframe>

以降のページでは`add_child`のインターフェースなど、Spriteクラスの他のインターフェースについて説明していきます。

## 関連資料

- [add_child （子の追加）と remove_child （子の削除）のインターフェイス](jp_add_child_and_remove_child.md)
- [contains インターフェイス](jp_contains.md)

- [num_children （子の件数属性）のインターフェイス](jp_num_children.md)
- [get_child_at （特定位置の子の取得処理）のインターフェイス](jp_get_child_at.md)

## SpriteクラスのコンストラクタAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, *, variable_name: str = '', variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

親になることの出来る基本的な表示用のオブジェクトを作成します。<hr>

**[引数]**

- `variable_name`: str, default '
  - このインスタンスの（JavaScript上などで使われる）変数名の設定値。apyscの内部実装で`Sprite`クラスのサブクラスをインスタンス化する時以外は設定は不要です。

- `variable_name_suffix`: str, default ""
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite_1: ap.Sprite = ap.Sprite()
>>> # Create the sprite child rectangle
>>> sprite_1.graphics.begin_fill(color=ap.Color("#0af"))
>>> rect: ap.Rectangle = sprite_1.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
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
>>> sprite_2.x = ap.Number(50)
>>> sprite_2.x
Number(50.0)
```