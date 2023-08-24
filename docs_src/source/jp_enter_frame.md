<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/enter_frame.html)の確認をお願いします。</span>

# enter_frame インターフェイス

このページでは`enter_frame`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`enter_frame`インターフェイスはアニメーションのためのハンドラを設定します。

このインターフェイスでは指定されたハンドラを各フレームごとに呼び出します。

## Timer クラスと enter_frame のインターフェイスのどちらを使うべきか

`Timer`クラスでも同様にアニメーションを扱うことができます。

そのため、アニメーション用途の場合`Timer`クラスと`enter_frame`のインターフェイスのどちらを使うべきなのでしょうか？

回答としては基本的には`enter_frame`側となります。

`enter_frame`のインターフェイスはハンドラの呼び出しの間隔が`Timer`クラスよりもずれにくくなっています。

一方で、`Timer`クラス側はCPU負荷が高い場合などに呼び出しタイミングがずれるケースが発生します。

## 基本的な使い方

`enter_frame`インターフェイスは`Stage`や`Sprite`などのクラスに存在します。

`enter_frame`インターフェイスは`handler`引数（関数やメソッドなどのcallableオブジェクト）の指定を必要とします。

`fps`引数は省略可で、この引数はフレームレートを決定します（`FPS`のenumの指定が可能です）。

また、`options`引数も省略可であり、この指定はハンドラへと追加のパラメーターを渡すことができます。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50,
    y=50,
    width=50,
    height=50,
    fill_color=ap.Color("#0af"),
)


def on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:
    """
    The handler to handle an enter frame event.

    Parameters
    ----------
    e : ap.EnterFrameEvent
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    rectangle.rotation_around_center += 1


stage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)
ap.save_overall_html(dest_dir_path="enter_frame_basic_usage/")
```

<iframe src="static/enter_frame_basic_usage/index.html" width="150" height="150"></iframe>

## 関連資料

- [Timer クラス](jp_timer.md)
- [FPS の enum](jp_fps.md)

## enter_frame のAPI

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `enter_frame(self, handler: Callable[[apysc._event.enter_frame_event.EnterFrameEvent, ~_Options], NoneType], *, fps: apysc._time.fps.FPS = <FPS.FPS_60: <apysc._time.fps.FPSDefinition object at 0x7f80576dc3a0>>, options: Union[~_Options, NoneType] = None) -> None`<hr>

**[インターフェイス概要]**

enter frameのイベントのリスナー設定を追加します。<hr>

**[引数]**

- `handler`: Callable[[EnterFrameEvent, _Options], None]
  - enter frameイベントを扱うためのハンドラの関数。

- `fps`: FPS, default FPS.FPS_60
  - 設定する1秒辺りのフレーム数（frame per second）。

- `options`: Optional[_Options], optional
  - ハンドラの関数へと渡される追加のパラメーターの引数値。

<hr>

**[特記事項]**

もしこのインターフェイスの呼び出しが2回目且つ指定されたハンドラの引数の値が同一の場合、このインターフェイスは`options`引数の指定を無視します（実行中かどうかのステータスと`fps`の設定のみ更新します）。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=50, y=50, width=50, height=50, fill_color=ap.Color("#0af")
... )
>>> def on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:
...     rectangle.x += 1
>>> stage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)
```