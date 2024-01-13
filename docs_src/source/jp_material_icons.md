<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/material_icons.html)の確認をお願いします。</span>

# マテリアルデザインアイコン

このページではapyscでのマテリアルデザインのアイコンに関係した実装について説明します。

## 実装の概要

各マテリアルデザインのアイコンのクラス名は例えば`MaterialSearchIcon`や`MaterialAccountCircleIcon`といったように`Material<アイコン名>Icon`という形式になります。

これらのアイコンのクラスは`Rectangle`や`Circle`などの他のグラフィックス用の各クラスと同様に使用することができます。

## 基本的な使い方

```py
# runnable
import apysc as ap

MARGIN: int = 20
ICON_SIZE: int = 24
ICON_NUM: int = 3
stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=MARGIN * 2 + ICON_SIZE * ICON_NUM + MARGIN * 2,
    stage_height=MARGIN + ICON_SIZE + MARGIN,
    stage_elem_id="stage",
)

search_icon: ap.MaterialSearchIcon = ap.MaterialSearchIcon(
    fill_color=ap.Colors.GRAY_AAAAAA,
    x=MARGIN,
    y=MARGIN,
    width=ICON_SIZE,
    height=ICON_SIZE,
)
info_icon: ap.MaterialInfoIcon = ap.MaterialInfoIcon(
    fill_color=ap.Colors.CYAN_00FFFF,
    x=MARGIN + ICON_SIZE + MARGIN,
    y=MARGIN,
    width=ICON_SIZE,
    height=ICON_SIZE,
)
home_icon: ap.MaterialHomeIcon = ap.MaterialHomeIcon(
    fill_color=ap.Colors.MAGENTA_FF00FF,
    x=MARGIN + (ICON_SIZE + MARGIN) * 2,
    y=MARGIN,
    width=ICON_SIZE,
    height=ICON_SIZE,
)

ap.save_overall_html(dest_dir_path="./material_icons_basic_usage/")
```

<iframe src="static/material_icons_basic_usage/index.html" width="152" height="64"></iframe>

## 各マテリアルアイコンのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, *, fill_color: apysc._color.color.Color, fill_alpha: Union[float, apysc._type.number.Number] = 1.0, x: Union[float, apysc._type.number.Number] = 0, y: Union[float, apysc._type.number.Number] = 0, width: Union[int, apysc._type.int.Int] = 24, height: Union[int, apysc._type.int.Int] = 24, parent: Union[apysc._display.child_mixin.ChildMixIn, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

マテリアルデザインのアイコンを作成します。<hr>

**[引数]**

- `fill_color`: Color
  - アイコンの塗りの色。

- `fill_alpha`: Union[float, Number], optional
  - アイコンの塗りの透明度。

- `x`: Union[float, Number], optional
  - アイコンのX座標。

- `y`: Union[float, Number], optional
  - アイコンのY座標。

- `width`: Union[int, Int], optional
  - アイコンの幅。

- `height`: Union[int, Int], optional
  - アイコンの高さ。

- `parent`: ChildMixIn or None, default None
  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。

- `variable_name_suffix`: str, optional
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[関連資料]**

- [Material icons](https://fonts.google.com/icons?selected=Material+Icons:search:)
- [APACHE LICENSE, VERSION 2.0](https://www.apache.org/licenses/jp_LICENSE-2.0.html)