<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](graphics_line_dash_setting.md)の確認をお願いします。</span>

# Graphics クラスの line_dash_setting インターフェイス

このページでは`Graphics`クラスの`line_dash_setting`属性のインターフェイスについて説明します。

## インターフェイス概要

`line_dash_setting`

## 基本的な使い方

getterとsetterのインターフェイスの値は`LineDashSetting`インスタンスの値となります。

以下のコード例では線に対して10pxの破線と3pxの破線間の空白のスペースを設定しています。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=250, stage_height=100, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color='#0af', thickness=5)

line: ap.Line = sprite.graphics.draw_line(
    x_start=50, y_start=50, x_end=200, y_end=50)
line.line_dash_setting = ap.LineDashSetting(dash_size=10, space_size=3)

ap.save_overall_html(
    dest_dir_path='./graphics_line_dash_setting_basic_usage/')
```

<iframe src="static/graphics_line_dash_setting_basic_usage/index.html" width="250" height="100"></iframe>

## line_dash_setting 属性のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** 現在の線の破線のスタイル設定を取得します。<hr>

**[返却値]**

- `line_dash_setting`: LineDashSetting or None
  - 線の破線のスタイル設定。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=10)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50)
>>> line.line_dash_setting = ap.LineDashSetting(
...     dash_size=5, space_size=2)
>>> line.line_dash_setting.dash_size
Int(5)

>>> line.line_dash_setting.space_size
Int(2)
```