<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/for_array_indices_and_values.html)の確認をお願いします。</span>

# ForArrayIndicesAndValues クラス

このページでは`ForArrayIndicesAndValues`クラスについて説明します。

事前に以下のページを読んでおくと役立つかもしれません（apyscライブラリではこのクラスを各データ型と同じように扱っています）。

- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)

## クラス概要

`ForArrayIndicesAndValues`クラスはループ制御のためのクラスです。

このインターフェイスはループ内で`Array`クラスのインデックスと値を返却します。

## 基本的な使い方

このクラスは`with`ステートメントと共に使う必要があります。

`as`キーワードの値は`Array`クラスのインデックスと値になります。

また、このクラスは`Array`の配列内の値の型の指定用に`arr_value_type`引数の指定が必要になります。

この型の指定は`Int`や`Number`、`String`や`Rectangle`などのapyscの型（クラス）のみ受け付けます。

```py
# runnable
import apysc as ap

ap.Stage(stage_width=350, stage_height=225, background_color="#333")

x_arr: ap.Array[ap.Number] = ap.Array([ap.Number(75), ap.Number(175), ap.Number(275)])
with ap.ForArrayIndicesAndValues(arr=x_arr, arr_value_type=ap.Number) as (i, x):
    circle: ap.Circle = ap.Circle(
        x=x,
        y=(i + 1) * 50,
        radius=25,
        fill_color="#0af",
    )

ap.save_overall_html(dest_dir_path="for_array_indices_and_values_basic_usage_1/")
```

<iframe src="static/for_array_indices_and_values_basic_usage_1/index.html" width="350" height="225"></iframe>

## 関連資料

- [分岐条件の各クラスのスコープ内変数の復元設定](jp_branch_instruction_variables_reverting_setting.md)
  - 特記事項 : このクラスは同じ引数を持ち同様の振る舞いをします。

## ForArrayIndicesAndValues API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, arr: apysc._type.array.Array[~_ArrayValue], arr_value_type: Type[~_ArrayValue], *, locals_: Union[Dict[str, Any], NoneType] = None, globals_: Union[Dict[str, Any], NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

`ap.Array`の各インデックスと値に対するループ制御の実装となるクラスです。<hr>

**[引数]**

- `arr`: Array[_ArrayValue]
  - イテレーションのための配列。

- `arr_value_type`: Type[_ArrayValue]
  - 配列の値の型。このインターフェイスは`Int`、`String`、`Rectangle`などのapyscの型を受け付けます。

- `locals_`: Optional[Dict[str, Any]], optional
  - 現在のスコープの各ローカル変数。この引数にはlocals()関数の返却値を設定してください。もしこの引数が指定された場合、このインターフェイスはローカルスコープのVariableNameMixInの各変数（例 : IntやSpriteなど）の値をwithステートメントの最後で復元します。この設定は各変数を更新したくない場合等に役立ちます。

- `globals_`: Optional[Dict[str, Any]], optional
  - 現在のスコープの各グローバル変数。設定する場合にはglobal()関数の値をこの引数に指定してください。この設定はlocals_引数と同じように動作します。

- `variable_name_suffix`: str, optional
  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> _ = ap.Stage(
...     stage_width=350, stage_height=225, background_color="#333"
... )
>>> x_arr: ap.Array[ap.Number] = ap.Array(
...     [ap.Number(75), ap.Number(175), ap.Number(275)]
... )
>>> with ap.ForArrayIndicesAndValues(
...     arr=x_arr, arr_value_type=ap.Number
... ) as (i, x):
...     circle: ap.Circle = ap.Circle(
...         x=x,
...         y=(i + 1) * 50,
...         radius=25,
...         fill_color="#0af",
...     )
```