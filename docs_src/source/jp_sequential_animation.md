<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](../en/sequential_animation.html)の確認をお願いします。</span>

# 連続したアニメーション設定

このページではアニメーションを連続させて再生する方法について説明します。

## 同じインスタンス上でアニメーションのインターフェイスを連続して呼び出す

アニメーションのインターフェイスを連続して呼び出した場合、各アニメーションは順番にスタートします（例えば、最初のアニメーションが終わったら次のアニメーションの再生がスタートじます）。

以下のコード例では4つの座標のアニメーションを設定しています。これらのアニメーションは同時にはスタートしません:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=200, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
easing: ap.Easing = ap.Easing.EASE_OUT_QUINT
rectangle.animation_x(x=100, duration=1000, delay=1000, easing=easing).start()
rectangle.animation_y(y=100, duration=1000, delay=1000, easing=easing).start()
rectangle.animation_x(x=50, duration=1000, delay=1000, easing=easing).start()
rectangle.animation_y(y=50, duration=1000, delay=1000, easing=easing).start()

ap.save_overall_html(
    dest_dir_path='sequential_animation_example_1/')
```

<iframe src="static/sequential_animation_example_1/index.html" width="200" height="200"></iframe>

## animation_complete のハンドラ設定

また、`animation_complete`インターフェイスを使ってアニメーション終了時のハンドラを設定して連続したアニメーションを設定することもできます。詳細は以下をご確認ください:

- [animation_complete インターフェイス](jp_animation_complete.md)

## 関連資料

もしも複数のアニメーションを同時に再生したい場合、以下のインターフェイスをお使いください。

- [animation_parallel インターフェイス](jp_animation_parallel.md)