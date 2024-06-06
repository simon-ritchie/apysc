<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/svg_mask.html)の確認をお願いします。</span>

# SvgMask クラスと関連インターフェース

このページでは`SvgMask`クラスとそれに関連した`add_svg_masking_object`メソッドや`svg_mask`属性などのインターフェイスについて説明します。

## クラス概要

`SvgMask`クラスはSVGグラフィックのマスク設定を扱います。

重なりあった領域のみを表示する形でSVGの`DisplayObject`（例 : `Rectangle`）に別のSVGの`DisplayObject`を設定することができます。

## 基本的な使い方

以下のステップでマスク設定を適用することができます。

1. `SvgMask`インスタンスを作成します。

2. `add_svg_masking_object`メソッドを使って作成した`SvgMask`のインスタンスに`DisplayObject`を追加します。

3. マスクのインスタンスを対象の`DisplayObject`の`svg_mask`属性に設定します。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)

# 1. Create an `SvgMask` instance.
mask: ap.SvgMask = ap.SvgMask()
circle: ap.Circle = ap.Circle(x=100, y=100, radius=50)

# 2. Add a `DisplayObject` to the created `SvgMask` instance.
mask.add_svg_masking_object(masking_object=circle)
rectangle: ap.Rectangle = ap.Rectangle(
    x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF
)

# 3. Set a mask instance to the target `DisplayObject`'s `svg_mask` property.
rectangle.svg_mask = mask

ap.save_overall_html(dest_dir_path="svg_mask_basic_usage/")
```

<iframe src="static/svg_mask_basic_usage/index.html" width="150" height="150"></iframe>

## DisplayObjectとマスクの座標を同期させたい場合のケース

マスクを設定する対象の`DisplayObject`とマスク用の`DisplayObject`はそれぞれ分離された座標値を持っています。

もし両方の`DisplayObject`の座標を同じ量だけ変更したい場合には`Sprite`のコンテナーを使用すると便利です。

`Sprite`のコンテナーの座標のみを変更することで、マスクの座標を維持したまま`DisplayObject`の座標を変更することができます。

特記事項 : マスク処理用の`DisplayObject`は`Sprite`のコンテナーへと追加する必要はありません。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=400,
    stage_height=300,
    stage_elem_id="stage",
)
mask: ap.SvgMask = ap.SvgMask()
circle: ap.Circle = ap.Circle(x=150, y=100, radius=100)
mask.add_svg_masking_object(masking_object=circle)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF
)
rectangle.svg_mask = mask

sprite: ap.Sprite = ap.Sprite()
# Notes: You do not need to add the circle for masking.
sprite.add_child(rectangle)
sprite.x = ap.Number(100)
sprite.y = ap.Number(50)

ap.save_overall_html(dest_dir_path="svg_mask_sprite_container_example/")
```

<iframe src="static/svg_mask_sprite_container_example/index.html" width="400" height="300"></iframe>

## SvgMask クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, *, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

SVGのマスク処理のためのクラスです。<hr>

**[引数]**

- `variable_name_suffix`: str, default ""
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> mask: ap.SvgMask = ap.SvgMask()
>>> circle: ap.Circle = ap.Circle(
...     x=50, y=50, radius=50, fill_color=ap.Colors.CYAN_00AAFF
... )
>>> mask.add_svg_masking_object(masking_object=circle)
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF
... )
>>> rectangle.svg_mask = mask
```

## SvgMask クラスの add_svg_masking_object メソッドのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `add_svg_masking_object(self, *, masking_object: apysc._display.graphics_base.GraphicsBase) -> None`<hr>

**[インターフェイス概要]**

このマスクにマスク処理用のSVGのオブジェクトを追加します。このインスタンスは他のSVGのグラフィックスオブジェクトをマスクするためにそのオブジェクトを使用します。マスクへ複数のマスク処理用のオブジェクトを追加することができます。<hr>

**[引数]**

- `masking_object`: GraphicsBase
  - 追加するマスク処理用のオブジェクト。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> mask: ap.SvgMask = ap.SvgMask()
>>> circle: ap.Circle = ap.Circle(
...     x=50, y=50, radius=50, fill_color=ap.Colors.CYAN_00AAFF
... )
>>> mask.add_svg_masking_object(masking_object=circle)
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF
... )
>>> rectangle.svg_mask = mask
```

## svg_mask 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

SVGのマスク設定を取得します。もしマスク設定がされていなければ、この属性の値はNoneとなります。<hr>

**[返却値]**

- `mask`: Optional[SvgMask]
  - マスク設定。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> mask: ap.SvgMask = ap.SvgMask()
>>> circle: ap.Circle = ap.Circle(
...     x=50, y=50, radius=50, fill_color=ap.Colors.CYAN_00AAFF
... )
>>> mask.add_svg_masking_object(masking_object=circle)
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF
... )
>>> rectangle.svg_mask = mask
>>> assert rectangle.svg_mask == mask
```