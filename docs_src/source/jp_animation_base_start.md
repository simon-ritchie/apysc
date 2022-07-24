<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/animation_base_start.html)の確認をお願いします。</span>

# AnimationBaseクラス start インターフェイス

このページでの`AnimationBase`クラスの`start`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`start`メソッドは対象のアニメーションを開始します。各アニメーションのインターフェイスは`AnimationBase`クラスのサブクラスのインスタンスを返却します。例えば`animation_move`や`animation_x`などが該当し、それらのインスタンスはこの`start`メソッドを持っています。

## 基本的な使い方

特記事項: 以下のコードのようにアニメーションを開始するには`animation_x`などの各アニメーションのインターフェイスを呼び出した後に`start`メソッドを呼ぶ必要があります。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

animation_x: ap.AnimationX = rectangle.animation_x(x=100, duration=3000, delay=3000)
animation_x.start()

ap.save_overall_html(dest_dir_path="./animation_base_start_basic_usage_1/")
```

<iframe src="static/animation_base_start_basic_usage_1/index.html" width="200" height="150"></iframe>

シンプルに書くためにメソッドチェーンを使う形でも書くことができます:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

rectangle.animation_x(x=100, duration=3000, delay=3000).start()

ap.save_overall_html(dest_dir_path="./animation_base_start_basic_usage_2/")
```

<iframe src="static/animation_base_start_basic_usage_2/index.html" width="200" height="150"></iframe>

## start API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `start(self) -> 'AnimationBase'`<hr>

**[インターフェイス概要]** 現在の設定値でアニメーションを開始します。<hr>

**[返却値]**

- `self`: AnimatonBase
  - このインスタンス。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.animation_x(x=100).start()
```