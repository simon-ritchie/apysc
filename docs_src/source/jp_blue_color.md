<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/blue_color.html)の確認をお願いします。</span>

# Color クラスの blue_color プロパティ

このページでは`Color`クラスの`blue_color`属性について説明します。

## 属性の概要

`blue_color`属性は青色の`ap.Int`型の値の返却もしくは設定を行います。

この値は0～255の範囲を取ります。

## 基本的な使い方

以下の例では`blue_color`のgetterとsetterの各インターフェイスの使い方を示します:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

color: ap.Color = ap.Color("#ffaa00")
blue_color: ap.Int = color.blue_color
ap.assert_equal(blue_color, 0)

color = ap.Color("#00aaff")
blue_color = color.blue_color
ap.assert_equal(blue_color, 255)

color.blue_color = ap.Int(0)
blue_color = color.blue_color
ap.assert_equal(blue_color, 0)

color.blue_color = ap.Int(255)
blue_color = color.blue_color
ap.assert_equal(blue_color, 255)

ap.save_overall_html(dest_dir_path="./blue_color_basic_usage/")
```

<iframe src="static/blue_color_basic_usage/index.html" width="0" height="0"></iframe>

## blue_color 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

青色の整数の値（0～255）を取得します。<hr>

**[返却値]**

- `blue_color`: Int
  - 青色の整数値（0～255）。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color=ap.Color("#333"),
...     stage_elem_id="stage",
... )
>>> color: ap.Color = ap.Color("#aaff00")
>>> blue_color: ap.Int = color.blue_color
>>> blue_color
Int(0)

>>> color = ap.Color("#00aaff")
>>> blue_color = color.blue_color
>>> blue_color
Int(255)

>>> color.blue_color = ap.Int(0)
>>> blue_color = color.blue_color
>>> blue_color
Int(0)

>>> color.blue_color = ap.Int(255)
>>> blue_color = color.blue_color
>>> blue_color
Int(255)
```