<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/variable_name_suffix.html)の確認をお願いします。</span>

# variable_name_suffix の引数設定

このページでは`variable_name_suffix`の引数設定について説明します。

## 引数の概要

`variable_name_suffix`引数は出力されるJavaScriptの変数名のサフィックスを変更します。

この設定は出力されたJavaScriptに対してデバッグを行う際などに便利なことがあります。

## 基本的な使い方

apyscの各クラスは`variable_name_suffix`引数を持っており、その引数を使ってサフィックスを設定することができます。

以下のコード例では`my_int`というサフィックスを`ap.Int`クラスのインスタンスへと設定しています:

```py
import apysc as ap

ap.Stage(stage_width=150, stage_height=150, stage_elem_id="stage")
int_val: ap.Int = ap.Int(10, variable_name_suffix="my_int")
ap.trace(int_val)

ap.save_overall_html(
    dest_dir_path="./variable_name_suffix_basic_usage_1/", minify=False
)
```

出力されたJavaScriptコード内で、`ap.Int`クラスが変換されて作成された変数が以下のように指定された`_my_int`というサフィックスを持っていることを確認できます:

```js
  // ...
  var i_9__my_int = 10;
  console.log(i_9__my_int, "Called from: tmp.py, line number: 5");
  // ...
```

クラスの属性の値はそのクラスへ指定されたサフィックスの値を引き継ぎます。

例えば`variable_name_suffix`引数に`my_rectangle`というサフィックスを指定した場合、そのクラスの属性（例 : `x`や`fill_color`など）は同様に`my_rectangle`というサフィックスを持つようになります:

```py
import apysc as ap

ap.Stage(stage_width=150, stage_height=150, stage_elem_id="stage")
rectangle: ap.Rectangle = ap.Rectangle(
    x=50,
    y=50,
    width=50,
    height=50,
    fill_color=ap.Color("#0af"),
    variable_name_suffix="my_rectangle",
)

ap.save_overall_html(
    dest_dir_path="./variable_name_suffix_basic_usage_2/", minify=False
)
```

このようなケースでは`x`や`width`などの属性の識別用のサフィックスも同様に設定されます:

```js
  var i_9__my_rectangle__x = 50;
  var i_10__my_rectangle__y = 50;
  var i_12__my_rectangle__width = 50;
  // ...
  var rect_1__my_rectangle = stage
    .rect(i_16__my_rectangle__width, i_17__my_rectangle__height)
    .attr({
      fill: s_1__my_rectangle__fill_color,
      "fill-opacity": n_2__my_rectangle__fill_alpha,
      "stroke-width": i_15__my_rectangle__line_thickness,
      "stroke-opacity": n_3__my_rectangle__line_alpha,
      x: i_9__my_rectangle__x,
      y: i_10__my_rectangle__y,
    });
  // ...
```