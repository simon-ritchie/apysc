<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/for_dict_keys_and_values.html)の確認をお願いします。</span>

# ForDictKeysAndValues クラス

このページでは`ForDictKeysAndValues`クラスについて説明します。

事前に以下のページを読んでおくと役立つかもしれません（apyscライブラリではこのクラスを各データ型と同じように扱っています）。

- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)

## クラス概要

`ForDictKeysAndValues`クラスはfor文のループのためのクラスです。

このインターフェイスはループの中で`Dictionary`のキーと値を返却します。

## 基本的な使い方

このクラスは`with`ステートメントと共に使う必要があります。

`as`キーワード部分の値は`Dictionary`のキーと値になります。

また、このクラスは`Dictionary`のキーと値の型を指定するための`dict_key_type`と`dict_value_type`引数の指定を必要とします。

`dict_key_type`は`String`、`Int`、`Number`、`Boolean`などのハッシュ化可能なapyscの型のみを受け付けます。

同様に`dict_value_type`引数は`String`や`Int`、`Rectangle`などのapyscの型を受け付けます。

```py
# runnable
import apysc as ap

ap.Stage(background_color="#333", stage_width=250, stage_height=300)

dict_: ap.Dictionary[ap.Number, ap.Number] = ap.Dictionary(
    {
        ap.Number(50): ap.Number(50),
        ap.Number(100): ap.Number(125),
        ap.Number(150): ap.Number(200),
    }
)
with ap.ForDictKeysAndValues(
    dict_=dict_,
    dict_key_type=ap.Number,
    dict_value_type=ap.Number,
) as (key, value):
    ap.Rectangle(x=key, y=value, width=50, height=50, fill_color="#0af")

ap.save_overall_html(dest_dir_path="for_dict_keys_and_values_basic_usage_1/")
```

<iframe src="static/for_dict_keys_and_values_basic_usage_1/index.html" width="250" height="300"></iframe>

## 関連資料

- [分岐条件の各クラスのスコープ内変数の復元設定](jp_branch_instruction_variables_reverting_setting.md)
  - 特記事項 : このクラスは同じ引数を持ち同様の振る舞いをします。

## ForDictKeysAndValues API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, dict_: apysc._type.dictionary.Dictionary[~_DictKey, ~_DictValue], dict_key_type: Type[~_DictKey], dict_value_type: Type[~_DictValue], *, locals_: Union[Dict[str, Any], NoneType] = None, globals_: Union[Dict[str, Any], NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

`ap.Dictionary`のキーと値のためのループのクラスの実装です。<hr>

**[引数]**

- `dict_`: Dictionary[_DictKey, _DictValue]
  - イテレーションで扱うための辞書。

- `dict_key_type`: Type[_DictKey]
  - 辞書のキーの型。このインターフェイスは`String`、`Int`、`Number`、`Boolean`といったハッシュ化可能な型を受け付けます。

- `dict_value_type`: Type[_DictValue]
  - 辞書の値の型。ごのインターフェイスは`Int`、`String`、`Rectangle`などの`InitializeForLoopKeyOrValueInterface`のサブクラスの型のみ受け付けます。

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
>>> _ = ap.Stage(background_color="#333", stage_width=250, stage_height=300)
>>> dict_: ap.Dictionary[ap.Number, ap.Number] = ap.Dictionary(
...     {
...         ap.Number(50): ap.Number(50),
...         ap.Number(100): ap.Number(125),
...         ap.Number(150): ap.Number(200),
...     }
... )
>>> with ap.ForDictKeysAndValues(
...     dict_=dict_,
...     dict_key_type=ap.Number,
...     dict_value_type=ap.Number,
... ) as (key, value):
...     _ = ap.Rectangle(x=key, y=value, width=50, height=50, fill_color="#0af")
```