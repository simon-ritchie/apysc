<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/text_fill_color.html)の確認をお願いします。</span>

# Text クラスの fill_color 属性

このページではテキスト関係の`fill_color`属性について説明します。

## 属性の概要

`fill_color`属性のインターフェイスでは塗りの色の値を更新したり取得したりすることができます。

## 基本的な使い方

getterのインターフェイスは`Color`型の値になります。setterのインターフェイスも`Color`型の値の指定が必要になります。

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
    x=25,
    y=25,
)
multi_line_text.fill_color = ap.Colors.CYAN_00AAFF
ap.assert_equal(multi_line_text.fill_color, ap.Colors.CYAN_00AAFF)
ap.save_overall_html(dest_dir_path="text_fill_color_basic_usage/")
```

<iframe src="static/text_fill_color_basic_usage/index.html" width="300" height="200"></iframe>

## fill_color 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

テキストの塗りの色を取得します。<hr>

**[返却値]**

- `color`: Color
  - テキストの色。