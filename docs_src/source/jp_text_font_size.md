<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/text_font_size.html)の確認をお願いします。</span>

# テキストの font_size 属性

このページではテキスト関係の`font_size`属性について説明します。

## 属性の概要

`font_size`属性ではフォントサイズ（テキストサイズ）の更新もしくは取得を行うことができます。

## 基本的な使い方

getterとsetterの各インターフェイスの値の型は`ap.Int`になります。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=350,
    stage_height=400,
    stage_elem_id="stage",
)
font_size_16_text: ap.MultiLineText = ap.MultiLineText(
    text="Example of font-size = 16. Lorem ipsum dolor sit amet, "
    "consectetur adipiscing elit, sed do eiusmod tempor incididunt "
    "ut labore et dolore magna aliqua. Ut enim ad minim veniam.",
    width=300,
    fill_color=ap.Color("#00aaff"),
    x=25,
    y=25,
)
font_size_16_text.font_size = ap.Int(16)

font_size_32_text: ap.MultiLineText = ap.MultiLineText(
    text="Example of font-size = 32. Lorem ipsum dolor sit amet, consectetur.",
    width=300,
    fill_color=ap.Color("#00aaff"),
    x=25,
    y=190,
)
font_size_32_text.font_size = ap.Int(32)

ap.save_overall_html(dest_dir_path="./text_font_size_basic_usage/")
```

<iframe src="static/text_font_size_basic_usage/index.html" width="350" height="400"></iframe>

## font_size 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

テキストのフォントサイズを取得します。<hr>

**[返却値]**

- `font_size`: Int
  - テキストのフォントサイズ。