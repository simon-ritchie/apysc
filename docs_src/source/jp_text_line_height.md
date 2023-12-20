<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/text_line_height.html)の確認をお願いします。</span>

# テキストの line_height 属性

このページではテキスト関係の`line_height`属性について説明します。

## 属性の概要

`line_height`属性ではインスタンスの行間の設定の更新もしくは取得を行うことができます。

## 基本的な使い方

getterとsetterの各インターフェイスの型は`ap.Number`の値になります。

もしこの属性に1.5を指定した場合、行間はフォントサイズの1.5倍の大きさになります。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=300,
    stage_height=250,
    stage_elem_id="stage",
)

multi_line_text: ap.MultiLineText = ap.MultiLineText(
    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam",
    width=250,
    fill_color=ap.Colors.GRAY_AAAAAA,
    x=25,
    y=25,
)
multi_line_text.line_height = ap.Number(2.0)

ap.save_overall_html(dest_dir_path="./text_line_height_basic_usage/")
```

<iframe src="static/text_line_height_basic_usage/index.html" width="300" height="250"></iframe>

## line_height 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

行間の値を取得します。<hr>

**[返却値]**

- `line_height`: Number
  - 行間の値。