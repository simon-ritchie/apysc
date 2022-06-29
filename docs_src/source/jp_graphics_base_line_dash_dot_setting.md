<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/graphics_line_dash_dot_setting.html)の確認をお願いします。</span>

# GraphicsBase クラスの line_dash_dot_setting インターフェイス

このページでは`GraphicsBase`クラスの`line_dash_dot_setting`属性のインターフェイスについて説明します。

## インターフェイス概要

`line_dash_dot_setting`属性のインターフェイスでは現在の一点鎖線のスタイル設定の更新もしくは取得を行えます。

## 基本的な使い方

getterやsetterのインターフェイスの値は`LineDashDotSetting`インスタンスの値となります。

以下のコード例では10pxの破線と3pxの点線の一点鎖線を設定しています。

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
line.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=10, dash_size=3, space_size=3)

ap.save_overall_html(
    dest_dir_path='./graphics_line_dash_dot_setting_basic_usage/')
```

<iframe src="static/graphics_line_dash_dot_setting_basic_usage/index.html" width="250" height=100></iframe>

## line_dash_dot_setting API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイス概要]** 現在の一点鎖線のスタイル設定を取得します。<hr>

**[返却値]**

- `line_dash_dot_setting`: LineDashDotSetting or None
  - 一点鎖線の設定。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=10)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50)
>>> line.line_dash_dot_setting = ap.LineDashDotSetting(
...     dot_size=2, dash_size=5, space_size=3)
>>> line.line_dash_dot_setting.dot_size
Int(2)

>>> line.line_dash_dot_setting.dash_size
Int(5)

>>> line.line_dash_dot_setting.space_size
Int(3)
```