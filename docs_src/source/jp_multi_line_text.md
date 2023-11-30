<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/multi_line_text.html)の確認をお願いします。</span>

# MultiLineText クラス

このページでは`MultiLineText`クラスについて説明します。

## クラス概要

`MultiLineText`クラスは複数行のテキストのインスタンスを生成します。

このテキストのインスタンスは一定の幅で折り返します。

## 基本的な使い方

`MultiLineText`クラスは`text`引数を必要とします。

コンストラクタでは`width`、`fill_color`、`bold`、`text_align`などのスタイル設定も同様に受け付けます。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=300,
    stage_height=200,
    stage_elem_id="stage",
)

multi_line_text: ap.MultiLineText = ap.MultiLineText(
    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam",
    width=250,
    font_size=16,
    fill_color=ap.Colors.CYAN_00AAFF,
    x=25,
    y=25,
)
ap.save_overall_html(dest_dir_path="multi_line_text_basic_usage/")
```

<iframe src="static/multi_line_text_basic_usage/index.html" width="300" height="200"></iframe>

## MultiLineText クラスのコンストラクタのAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, *, text: Union[str, apysc._type.string.String], x: Union[float, apysc._type.number.Number] = 0, y: Union[float, apysc._type.number.Number] = 0, width: Union[int, apysc._type.int.Int] = 200, font_size: Union[int, apysc._type.int.Int] = 16, fill_color: apysc._color.color.Color = Color("#666666"), fill_alpha: Union[float, apysc._type.number.Number] = 1.0, bold: Union[bool, apysc._type.boolean.Boolean] = False, italic: Union[bool, apysc._type.boolean.Boolean] = False, text_align: apysc._display.css_text_align.CssTextAlign = <CssTextAlign.LEFT: 'left'>, text_align_last: apysc._display.css_text_align_last.CssTextAlignLast = <CssTextAlignLast.AUTO: 'auto'>, underline: Union[bool, apysc._type.boolean.Boolean] = False, parent: Union[apysc._display.child_mixin.ChildMixIn, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

複数行のテキスト要素のクラスの実装。<hr>

**[引数]**

- `text`: Union[str, String]
  - 表示対象のテキスト。HTMLタグが利用可能です。

- `x`: Union[float, Number], default 0
  - X座標。

- `y`: Union[float, Number], default 0
  - Y座標。

- `width`: Union[int, Int], default 200
  - 折り返し位置となるテキストの幅。

- `font_size`: Union[int, Int], default 16
  - フォントサイズ。

- `fill_color`: Color, default Colors.GRAY_666666
  - テキストの色。

- `fill_alpha`: Union[float, Number], default 1.0
  - テキストの透明度。最小値は0.0（透明）、最大値は1.0（不透明）になります。

- `bold`: Union[bool, Boolean], default False
  - テキストを太字で表示するか否か。

- `italic`: Union[bool, Boolean], default False
  - テキストを斜体で表示するか否か。

- `text_align`: CssTextAlign, default `CssTextAlign.LEFT`
  - テキストの行揃えの設定。

- `text_align_last`: CssTextAlignLast, default `CssTextAlignLast.AUTO`
  - 最終行の行揃えの設定。

- `underline`: Union[bool, Boolean], default False
  - テキストの下線を表示するか否か。

- `parent`: ChildMixIn or None, default None
  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。

- `variable_name_suffix`: str, default ""
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color=ap.Color("#333"),
...     stage_width=300,
...     stage_height=100,
...     stage_elem_id="stage",
... )
>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(
...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
...     "Ut enim ad minim veniam",
...     width=300,
...     font_size=16,
...     fill_color=ap.Color("#00aaff"),
...     x=20,
...     y=20,
... )
>>> multi_line_text.fill_color
Color("#00aaff")
```

<hr>

**[関連資料]**

- [テキストの fill_color 属性](https://simon-ritchie.github.io/apysc/jp/jp_text_fill_color.html)
- [テキストの fill_alpha 属性](https://simon-ritchie.github.io/apysc/jp/jp_text_fill_alpha.html)

- [テキストの bold 属性](https://simon-ritchie.github.io/apysc/jp/jp_text_bold.html)
- [テキストの italic 属性](https://simon-ritchie.github.io/apysc/jp/jp_text_italic.html)

- [text_align 属性](https://simon-ritchie.github.io/apysc/jp/jp_text_align.html)
- [text_align_last 属性](https://simon-ritchie.github.io/apysc/jp/jp_text_align_last.html)

- [テキストの font_size 属性](https://simon-ritchie.github.io/apysc/jp/jp_text_font_size.html)