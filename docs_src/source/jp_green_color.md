<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/green_color.html)の確認をお願いします。</span>

# Color クラスの green_color プロパティ

このページでは`Color`クラスの`green_color`プロパティについて説明します。

## 属性の概要

`green_color`プロパティは緑色の色の`ap.Int`型の値を返却します。

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

color: ap.Color = ap.Color("#aa00ff")
green_color: ap.Int = color.green_color
ap.assert_equal(green_color, 0)

color = ap.Color("#00ffaa")
green_color = color.green_color
ap.assert_equal(green_color, 255)

ap.save_overall_html(dest_dir_path="./green_color_basic_usage/")
```

<iframe src="static/green_color_basic_usage/index.html" width="0" height="0"></iframe>

## green_color 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]**

緑色の整数値（0～255）を取得します。<hr>

**[返却値]**

- `green_color`: Int
  - 緑色の整数値（0～255）。