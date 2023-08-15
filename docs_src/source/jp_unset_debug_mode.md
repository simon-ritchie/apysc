<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/unset_debug_mode.html)の確認をお願いします。</span>

# unset_debug_mode インターフェイス

このページでは`unset_debug_mode`関数のインターフェイスについて説明します。

## インターフェイス概要

`unset_debug_mode`関数のインターフェイスはデバッグモードの設定を解除します。この関数はデバッグ情報の追加を停止します。

デバッグモードの設定は大量の情報を出力します。時折これは煩雑な（情報が多すぎる）状態になることがあります。そのような場合にデバッグモードが不要になったタイミングで設定を解除すると役に立つことがあります。

## 特記事項

もしも出力のインターフェイス（例 : `ap.save_overall_html`など）の`minify`のオプションが有効になっていると、デバッグモードの情報なども削除されてしまいます。そのため`unset_debug_mode`インターフェイスでデバッグモードを解除した場合には`minify=False`の引数設定が必要になります。

## 基本的な使い方

`unset_debug_mode`インターフェイスは引数の指定を必要としません。

以下のコード例では`int_1`の変数のインスタンス化と10の加算処理の箇所のみデバッグ情報の追加を有効化しています。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
ap.set_debug_mode()
int_1: ap.Int = ap.Int(10)
int_1 += 10
ap.unset_debug_mode()
int_2: ap.Int = ap.Int(20)
int_2 += 20

ap.save_overall_html(minify=False, dest_dir_path="unset_debug_mode_basic_usage/")
```

出力されたHTMLでは最初の整数部分のデバッグ情報を以下のように含んでいます。その後のスプライトや2つ目の整数関係の位置のものは含まれないようになっています:

```js
...
  var sp_1 = stage.nested();
  var g_1 = stage.nested();
  arr_2.push(g_1);
  var i_12 = -1;
  i_12 = arr_2.indexOf(g_1);
  var b_3 = false;
  var i_13 = -1;
...
  //////////////////////////////////////////////////////////////////////
  // [__init__ 12] started.
  // module name: apysc._type.int
  // class: Int
  // arguments and variables:
  //    value = 10
  //    self = 0()
    //////////////////////////////////////////////////////////////////////
    // [__init__ 14] started.
    // module name: apysc._type.number_value_mixin
    // class: NumberValueMixIn
    // arguments and variables:
    //    type_name = 'i'
    //    value = 10
    //    self = 0(i_16)
    // [__init__ 14] ended.
    // module name: apysc._type.number_value_mixin
    // class: NumberValueMixIn
    //////////////////////////////////////////////////////////////////////
    //////////////////////////////////////////////////////////////////////
    // [to_int_from_float 14] started.
    // module name: apysc._converter.cast
    // arguments and variables:
    //    int_or_float = 10
    // [to_int_from_float 14] ended.
    // module name: apysc._converter.cast
    //////////////////////////////////////////////////////////////////////
    //////////////////////////////////////////////////////////////////////
    // [append_constructor_expression 14] started.
    // module name: apysc._type.number_value_mixin
    // class: NumberValueMixIn
    // arguments and variables:
    //    self = 10(i_16)
      var i_16 = 10;
    // [append_constructor_expression 14] ended.
    // module name: apysc._type.number_value_mixin
    // class: NumberValueMixIn
    //////////////////////////////////////////////////////////////////////
...
  var i_18 = 20;
  var i_19 = cpy(i_18);
  var i_19 = i_18 + 20;
  i_18 = i_19;
...
```

## 関連資料

- [set_debug_mode インターフェイス](jp_set_debug_mode.md)

## unset_debug_mode API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `unset_debug_mode() -> None`<hr>

**[インターフェイス概要]**

HTMLとJavaScriptのデバッグ用のデバッグモードの設定を解除します。<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> ap.set_debug_mode()
>>> int_val: ap.Int = ap.Int(10)
>>> ap.unset_debug_mode()
```