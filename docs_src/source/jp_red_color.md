<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/red_color.html)の確認をお願いします。</span>

# Color クラスの red_color プロパティ

このページでは`Color`クラスの`red_color`属性について説明します。

## 属性の概要

`red_color`属性は赤色の`ap.Int`型の値を返します。

この値は0～255の範囲を取ります。

## 基本的な使い方

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

color: ap.Color = ap.Color("#00aaff")
red_color: ap.Int = color.red_color
ap.assert_equal(red_color, 0)

color = ap.Color("#ff00aa")
red_color = color.red_color
ap.assert_equal(red_color, 255)

ap.save_overall_html(dest_dir_path="./red_color_basic_usage/")
```

<iframe src="static/red_color_basic_usage/index.html" width="0" height="0"></iframe>

## red_color 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

赤色の整数値（0～255）を取得します。<hr>

**[返却値]**

- `red_color`: Int
  - 赤色の整数値（0～255）。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> color: ap.Color = ap.Color("#00aaff")
>>> red_color: ap.Int = color.red_color
>>> red_color
Int(0)

>>> color = ap.Color("#ff00aa")
>>> red_color = color.red_color
>>> red_color
Int(255)
```