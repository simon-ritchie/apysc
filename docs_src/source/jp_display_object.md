<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](display_object.md)の確認をお願いします。</span>

# DisplayObject クラス

このページでは`DisplayObject`クラスについて説明します。

## DisplayObject クラスの概要

`DisplayObject`クラスは`Sprite`や`Rectangle`などのapyscの表示オブジェクトの基底クラスとなります。

各インスタンスが`DisplayObject`を継承していることを`isinstance`関数を使って確認することができます。

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=200,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)

# Verify each instance type.
assert isinstance(sprite, ap.DisplayObject)
assert isinstance(circle, ap.DisplayObject)
```

apyscはこのクラスを基本的な共通のインターフェイスで使用したり、もしくは別の`DisplayObject`を継承したインスタンスの作成処理などで使用しています。

`DisplayObject`クラスは`x`や`y`、`visible`属性、各マウスイベントの設定などの基本的なインターフェイスを持っています。以下のページではそれぞれのインターフェイスについて1つ1つ詳しく触れています。

## 関連資料

- [DisplayObject クラスの x と y インターフェイス](jp_display_object_x_and_y.md)
- [DisplayObjectクラス parent （親要素属性）のインターフェイス](jp_display_object_parent.md)

- [DisplayObject クラスの visible (表示・非表示) のインターフェイス](jp_display_object_visible.md)
- [DisplayObject クラスのマウスイベント設定の各インターフェイス](jp_display_object_mouse_event.md)