<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/set_debug_mode.html)の確認をお願いします。</span>

# set_debug_mode インターフェイス

このページでは`set_debug_mode`関数のインターフェイスについて説明します。

## インターフェイス概要

`set_debug_mode`関数のインターフェイスはデバッグモードの設定を有効化します。この設定はデバッグ用の情報（Python上の関数やメソッドの呼び出しと引数情報など）を出力されるHTML上に追加します。

## 特記事項

デバッグモードの設定は多くの情報をHTML上に追加します。結果として出力時間は長くなり、ファイルサイズも大きくなります。

また、この設定は`minify`（HTML最小化）の設定も無視します。

## 基本的な使い方

ステージのインスタンス後であれば`set_debug_mode`関数を使ってデバッグモードを設定ずることができます。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
ap.set_debug_mode()
sprite: ap.Sprite = ap.Sprite()
int_1: ap.Int = ap.Int(10)

ap.save_overall_html(
    dest_dir_path='set_debug_mode_basic_usage/')
```

この設定は以下の例の用に出力されたHTML内にPythonの関数やメソッドの呼び出しやそのモジュールやクラス名、引数情報などのJavaScriptのコメントを追加します:

```js
...
  //////////////////////////////////////////////////////////////////////
  // [__init__ 1] started.
  // module name: apysc._display.sprite
  // class: Sprite
  // arguments and variables:
  //    variable_name = None
  //    self = Sprite('')()
    //////////////////////////////////////////////////////////////////////
    // [__init__ 2] started.
    // module name: apysc._type.array
    // class: Array
    // arguments and variables:
    //    value = []
    //    self = []()
      //////////////////////////////////////////////////////////////////////
      // [_append_constructor_expression 2] started.
      // module name: apysc._type.array
      // class: Array
      // arguments and variables:
      //    self = [](arr_2)
        var arr_2 = [];
      // [_append_constructor_expression 2] ended.
      // module name: apysc._type.array
      // class: Array
      //////////////////////////////////////////////////////////////////////
    // [__init__ 2] ended.
    // module name: apysc._type.array
    // class: Array
    //////////////////////////////////////////////////////////////////////
    //////////////////////////////////////////////////////////////////////
    // [__init__ 1] started.
    // module name: apysc._display.display_object
    // class: DisplayObject
    // arguments and variables:
    //    variable_name = 'sp_1'
    //    self = Sprite('')()
    // [__init__ 1] ended.
    // module name: apysc._display.display_object
    // class: DisplayObject
    //////////////////////////////////////////////////////////////////////
    //////////////////////////////////////////////////////////////////////
    // [_append_constructor_expression 1] started.
    // module name: apysc._display.sprite
    // class: Sprite
    // arguments and variables:
    //    self = Sprite('sp_1')(sp_1)
      var sp_1 = stage.nested();
    // [_append_constructor_expression 1] ended.
    // module name: apysc._display.sprite
    // class: Sprite
    //////////////////////////////////////////////////////////////////////
...
```

## 関連資料

- [unset_debug_mode インターフェイス](jp_unset_debug_mode.md)

## set_debug_mode API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `set_debug_mode() -> None`<hr>

**[インターフェイス概要]** HTMLとJavaScriptのデバッグ用にデバッグモードの設定を行います。もしこの関数を呼び出した場合、のインターフェイスは以下の設定を追加します: <br> ・HTMLの最小化（minify）設定を無効化します。 <br> ・各インターフェイスごとのJavaScript上での区切りのための文字列を追加します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> ap.set_debug_mode()
>>> int_val: ap.Int = ap.Int(10)
```