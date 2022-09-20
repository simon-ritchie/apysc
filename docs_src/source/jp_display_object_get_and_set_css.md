<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/display_object_get_and_set_css.html)の確認をお願いします。</span>

# DisplayObject クラスの get_css と set_css メソッドのインターフェイス

このページでは`DisplayObject`クラスの`get_css`と`set_css`の各インターフェイスについて説明します。

## 各インターフェイスの概要

`get_css`メソッドは`DisplayObject`のインスタンスに設定されている特定のCSSの文字列を返却し、`set_css`メソッドは特定のCSSの値を設定します。

## 基本的な使い方

各インターフェイスはCSS名としての`name`引数の指定を必要とします。加えて、`set_css`メソッドではCSSの値の文字列としての`value`引数が必要になります。

以下のコード例では1秒ごとのタイマーでCSSの`display`の値がもしデフォルトの空文字になっていれば`none`の値を設定しています。デフォルト値以外の値になっていればデフォルトの値へと戻しています。

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _SpriteOptions(TypedDict):
    sprite: ap.Sprite


def on_timer(e: ap.TimerEvent, options: _SpriteOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    sprite: ap.Sprite = options["sprite"]
    display_css_val: ap.String = sprite.get_css(name="display")
    condition: ap.Boolean = display_css_val == "none"
    with ap.If(condition):
        sprite.set_css(name="display", value="")
    with ap.Else():
        sprite.set_css(name="display", value="none")


ap.Stage(
    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
options: _SpriteOptions = {"sprite": sprite}
timer: ap.Timer = ap.Timer(handler=on_timer, delay=1000, options=options)
timer.start()

ap.save_overall_html(dest_dir_path="display_object_get_and_set_css_basic_usage/")
```

<iframe src="static/display_object_get_and_set_css_basic_usage/index.html" width="150" height="150"></iframe>

## get_css API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `get_css(self, *, name: Union[str, apysc._type.string.String]) -> apysc._type.string.String`<hr>

**[インターフェイス概要]**

CSSの設定値の文字列を取得します。<hr>

**[引数]**

- `name`: str or String
  - CSS名（例 : 'display'）。

<hr>

**[返却値]**

- `css`: ap.String
  - CSSの値。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)
>>> sprite.set_css(name="display", value="none")
>>> sprite.get_css(name="display")
String('none')
```

## set_css API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `set_css(self, *, name: Union[str, apysc._type.string.String], value: Union[str, apysc._type.string.String]) -> None`<hr>

**[インターフェイス概要]**

CSSに指定された文字列の値を設定します。<hr>

**[引数]**

- `name`: str or String
  - CSS名（例 : 'display'）。

- `value`: str or String
  - CSSの値の文字列（例 : 'none'）

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)
>>> sprite.set_css(name="display", value="none")
>>> sprite.get_css(name="display")
String('none')
```