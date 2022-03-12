<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](add_child_and_remove_child.md)の確認をお願いします。</span>

# add_child と remove_child インターフェイス

このページではGraphicsクラスやSprite、Stageクラスなどのコンテナーとして扱えるクラスが持つ`add_child`と`remove_child`のインターフェイスについて説明します。

## 各インターフェイス概要

`add_child`インターフェイスではコンテナーのインスタンスへ子となる各`DisplayObject`を継承したインスタンスを追加し、逆に`remove_child`インターフェイスでは子のインスタンスをコンテナーから取り除きます。apyscでは取り除かれた子のインスタンスは表示されなくなります。

## 子のインスタンスの自動追加について

apyscでは各`DisplayObject`のインスタンスはコンストラクタの時点で親のインスタンスへと自動で追加されます。例えば`Sprite`クラスであれば`Stage`クラスのインスタンスを親として追加され、`Sprite`クラスを親として内部で作成される`graphics`プロパティのインスタンスは`Sprite`クラスのインスタンスへと自動で追加されます。

もし親のインスタンスを調整したい場合には手動で`add_child`や`remove_child`などのインターフェイスを呼ぶ必要があります。例えば親としてのとある`Sprite`クラスのインスタンスから別の`Sprite`クラスのインスタンスに子を移したい場合などが該当します。

## remove_child インターフェイスの基本的な使い方

`remove_child`インターフェイスでは子を親のコンテナー要素から取り除きます。apyscは取り除かれた`DisplayObject`の子のインスタンスを表示しません。

例えば以下のコードでは四角をクリックした際のハンドラ内で`remove_child`インターフェイスを呼び出しており、クリック時に四角が画面から取り除かれます。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_sprite_click(
        e: ap.MouseEvent[ap.Sprite], options: _RectOptions) -> None:
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
    rectangle: ap.Rectangle = options['rectangle']
    sprite.remove_child(child=rectangle)


ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
options: _RectOptions = {'rectangle': rectangle}
sprite.click(on_sprite_click, options=options)

ap.save_overall_html(
    dest_dir_path='sprite_basic_usage_of_remove_child/')
```

<iframe src="static/sprite_basic_usage_of_remove_child/index.html" width="150" height="150"></iframe>

## add_child インターフェイスの基本的な使い方

`add_child`インターフェイスは取り除かれた子のインスタンスをもう一度他の親のコンテナーのインスタンスへと追加します。

以下のコードでは四角をクリックした際に1つ目の左に配置されている`Sprite`の親のコンテナーからその四角を取り除き、そして2つ目の右側に配置してある`Sprite`のインスタンスへと子を追加しています。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _SpriteAndRectOptions(TypedDict):
    rectangle: ap.Rectangle
    sprite: ap.Sprite


def on_sprite_click(
        e: ap.MouseEvent[ap.Sprite],
        options: _SpriteAndRectOptions) -> None:
    """
    The handler that the sprite calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    first_sprite: ap.Sprite = e.this
    rectangle: ap.Rectangle = options['rectangle']
    second_sprite: ap.Sprite = options['sprite']
    first_sprite.remove_child(child=rectangle)
    second_sprite.add_child(child=rectangle)


ap.Stage(
    background_color='#333',
    stage_width=250,
    stage_height=150,
    stage_elem_id='stage')

first_sprite: ap.Sprite = ap.Sprite()
first_sprite.graphics.begin_fill(color='#0af')
first_sprite.x = ap.Int(50)
first_sprite.y = ap.Int(50)
rectangle: ap.Rectangle = first_sprite.graphics.draw_rect(
    x=0, y=0, width=50, height=50)

second_sprite: ap.Sprite = ap.Sprite()
second_sprite.x = ap.Int(150)
second_sprite.y = ap.Int(50)

options: _SpriteAndRectOptions = {
    'rectangle': rectangle, 'sprite': second_sprite}
first_sprite.click(on_sprite_click, options=options)

ap.save_overall_html(
    dest_dir_path='sprite_basic_usage_of_add_child/')
```

<iframe src="static/sprite_basic_usage_of_add_child/index.html" width="250" height="150"></iframe>

## 関連資料

- [DisplayObjectクラス parent インターフェイス](jp_display_object_parent.md)
- [contains インターフェイス](jp_contains.md)

## add_child API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `add_child(self, child:apysc._display.display_object.DisplayObject) -> None`<hr>

**[Interface 概要]** 子の表示用のインスタンスをこのインスタンスへと追加します。<hr>

**[引数]**

- `child`: DisplayObject
  - 追加する子のインスタンス。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite_1: ap.Sprite = ap.Sprite()
>>> sprite_1.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> sprite_2: ap.Sprite = ap.Sprite()
>>> sprite_2.add_child(rectangle)
```

## remove_child API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `remove_child(self, child:apysc._display.display_object.DisplayObject) -> None`<hr>

**[Interface 概要]** 表示用の子のインスタンスをこのインスタンスから取り除きます。<hr>

**[引数]**

- `child`: DisplayObject
  - 取り除く子のインスタンス。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> sprite.graphics.remove_child(rectangle)
>>> print(rectangle.parent)
None
```