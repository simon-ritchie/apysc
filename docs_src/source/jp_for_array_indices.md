<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/for_array_indices.html)の確認をお願いします。</span>

# ForArrayIndices クラス

このページでは`ForArrayIndices`クラスについて説明します。

事前に以下のページを読んでおくと役立つかもしれません（apyscライブラリではこのクラスを各データ型と同じように扱っています）。

- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)

## クラス概要

`ForArrayIndices`クラスはループ制御のためのクラスです。

このインターフェイスではループ中の`Array`クラスのインデックス（0からスタートします）を返却します。

## 基本的な使い方

このクラスは`with`ステートメントと共に使う必要があります。

`as`キーワードの値は`Int`型のインデックスとなります。

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")

arr: ap.Array[ap.Number] = ap.Array([ap.Number(50), ap.Number(150), ap.Number(250)])
indices: ap.Array[ap.Int] = ap.Array([])
with ap.ForArrayIndices(arr=arr) as i:
    indices.append(i)

ap.assert_arrays_equal(indices, [0, 1, 2])

ap.save_overall_html(dest_dir_path="for_array_indices_basic_usage_1/")
```

<iframe src="static/for_array_indices_basic_usage_1/index.html" width="0" height="0"></iframe>

以下の例ではインデックスを使って円の中心のX座標を設定しています。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=350, stage_height=150, background_color="#333", stage_elem_id="stage"
)

x_arr: ap.Array[ap.Number] = ap.Array([ap.Number(75), ap.Number(175), ap.Number(275)])
with ap.ForArrayIndices(arr=x_arr) as i:
    x: ap.Number = x_arr[i]
    circle: ap.Circle = ap.Circle(
        x=x,
        y=75,
        radius=25,
        fill_color="#0af",
    )

ap.save_overall_html(dest_dir_path="for_array_indices_basic_usage_2/")
```

<iframe src="static/for_array_indices_basic_usage_2/index.html" width="350" height="150"></iframe>

## 関連資料

- [分岐条件の各クラスのスコープ内変数の復元設定](jp_branch_instruction_variables_reverting_setting.md)
  - 特記事項 : このクラスは同じ引数を持ち同様の振る舞いをします。

## ForArrayIndices API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, arr: apysc._type.array.Array, *, locals_: Union[Dict[str, Any], NoneType] = None, globals_: Union[Dict[str, Any], NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

`ap.Array`のインデックス制御のためのループ制御用のクラスです。<hr>

**[引数]**

- `arr`: Array
  - イテレーションのための配列。

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
>>> arr: ap.Array[ap.Number] = ap.Array(
...     [ap.Number(50), ap.Number(150), ap.Number(250)]
... )
>>> indices: ap.Array[ap.Int] = ap.Array([])
>>> with ap.ForArrayIndices(arr=arr) as i:
...     indices.append(i)
...
>>> _ = ap.assert_arrays_equal(indices, [0, 1, 2])
```

<hr>

**[関連資料]**

- [なぜapyscライブラリではPythonビルトインのデータ型を使っていないのか](https://simon-ritchie.github.io/apysc/jp/jp_why_apysc_doesnt_use_python_builtin_data_type.html)
- [各分岐制御のクラスのスコープ内の変数値の復元設定](https://simon-ritchie.github.io/apysc/jp/jp_branch_instruction_variables_reverting_setting.html)