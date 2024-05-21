<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/material_icon.html)の確認をお願いします。</span>

# マテリアルアイコン

このページではapyscにおけるマテリアルアイコンの実装について説明します。

## 基本的な使い方

各マテリアルアイコンは一番上のパッケージパスに存在します（例 : `ap.MaterialTimelineIcon`）。

また、各マテリアルアイコンの名前は`Material`というプレフィックスと`Icon`というサフィックスを共通で持ちます。

全てのマテリアルアイコンのコンストラクタは`x`や`y`、`size`、`fill_color`、`fill_alpha`などの座標やスタイルの設定の引数を持ちます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=168,
    stage_height=72,
    stage_elem_id="stage",
)
SIZE: int = 24

ap.MaterialHomeIcon(
    x=24,
    y=24,
    size=SIZE,
    fill_color=ap.Colors.CYAN_00AAFF,
)
ap.MaterialBuildIcon(
    x=24 * 3,
    y=24,
    size=SIZE,
    fill_color=ap.Colors.CYAN_00AAFF,
)
ap.MaterialCheckCircleIcon(
    x=24 * 5,
    y=24,
    size=SIZE,
    fill_color=ap.Colors.CYAN_00AAFF,
)

ap.save_overall_html(dest_dir_path="material_icon_basic_usage_1/")
```

<iframe src="static/material_icon_basic_usage_1/index.html" width="168" height="72"></iframe>

以下のようにインスタンスの属性を用いて座標やスタイルを設定することもできます:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=168,
    stage_height=72,
    stage_elem_id="stage",
)
SIZE: int = 24

home_icon: ap.MaterialHomeIcon = ap.MaterialHomeIcon(size=SIZE)
home_icon.x = ap.Number(24)
home_icon.y = ap.Number(24)
home_icon.fill_color = ap.Colors.CYAN_00AAFF

build_icon: ap.MaterialBuildIcon = ap.MaterialBuildIcon(size=SIZE)
build_icon.x = ap.Number(24 * 3)
build_icon.y = ap.Number(24)
build_icon.fill_color = ap.Colors.CYAN_00AAFF

check_circle_icon: ap.MaterialCheckCircleIcon = ap.MaterialCheckCircleIcon(
    size=SIZE,
)
check_circle_icon.x = ap.Number(24 * 5)
check_circle_icon.y = ap.Number(24)
check_circle_icon.fill_color = ap.Colors.CYAN_00AAFF

ap.save_overall_html(dest_dir_path="material_icon_basic_usage_2/")
```

<iframe src="static/material_icon_basic_usage_2/index.html" width="168" height="72"></iframe>

## マテリアルアイコンのライセンス

apyscライブラリはAPACHE LICENSE, VERSION 2.0のライセンスのマテリアルアイコンを使用しています。

- [Material Symbols & Icons](https://fonts.google.com/icons?icon.size=24&icon.color=%23e8eaed)
- [material-design-icons (GitHub)](https://github.com/google/material-design-icons)

- [APACHE LICENSE, VERSION 2.0](https://www.apache.org/licenses/jp_LICENSE-2.0.html)

## 各マテリアルアイコンのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, x: Union[float, apysc._type.number.Number] = 0.0, y: Union[float, apysc._type.number.Number] = 0.0, size: Union[int, apysc._type.int.Int] = 24, fill_color: apysc._color.color.Color = Color("#666666"), fill_alpha: Union[float, apysc._type.number.Number] = 1.0, parent: Union[apysc._display.child_mixin.ChildMixIn, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

SVGアイコンのためのクラスの実装。<hr>

**[引数]**

- `x`: Union[float, Number], optional
  - アイコンのX座標。

- `y`: Union[float, Number], optional
  - アイコンのY座標。

- `size`: Union[int, Int], optional
  - アイコンのY座標。

- `fill_color`: Color, optional
  - アイコンの塗りの色。

- `fill_alpha`: Union[float, Number], optional
  - アイコンの塗りの透明度。

- `parent`: Optional[ChildMixIn], optional
  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。

- `variable_name_suffix`: str, optional
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。