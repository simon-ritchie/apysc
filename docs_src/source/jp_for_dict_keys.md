<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/for_dict_keys.html)の確認をお願いします。</span>

# ForDictKeys クラス

このページでは`ForDictKeys`クラスについて説明します。

事前に以下のページを読んでおくと役立つかもしれません（apyscライブラリではこのクラスを各データ型と同じように扱っています）。

- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)

## クラス概要

`ForDictKeys`クラスはfor文でのループのためのクラスです。

このインターフェイスはループ内で`Dictionary`のキーを返却します。

## 基本的な使い方

このクラスは`with`ステートメントと共に使う必要があります。

`as`キーワードの値は`Dictionary`のキーとなります。

また、このクラスは`Dictionary`のキーの型を指定するための`dict_key_type`引数の指定が必要になります。

この型の指定は`String`や`Int`、`Number`、`Boolean`といったapyscの型のみ受け付けます。

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")

dict_: ap.Dictionary[ap.String, int] = ap.Dictionary(
    {
        ap.String("apple"): 120,
        ap.String("orange"): 200,
    }
)
keys: ap.Array[ap.String] = ap.Array([])
with ap.ForDictKeys(dict_=dict_, dict_key_type=ap.String) as key:
    keys.append(key)
ap.assert_arrays_equal(
    keys,
    ["apple", "orange"],
)

ap.save_overall_html(dest_dir_path="for_dict_keys_basic_usage_1/")
```

<iframe src="static/for_dict_keys_basic_usage_1/index.html" width="0" height="0"></iframe>

## 関連資料

- [分岐条件の各クラスのスコープ内変数の復元設定](jp_branch_instruction_variables_reverting_setting.md)
  - 特記事項 : このクラスは同じ引数を持ち同様の振る舞いをします。

## ForDictKeys API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, dict_: apysc._type.dictionary.Dictionary[~_DictKey, typing.Any], dict_key_type: Type[~_DictKey], *, locals_: Union[Dict[str, Any], NoneType] = None, globals_: Union[Dict[str, Any], NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[インターフェイス概要]**

`ap.Dictionary`の各キーのためのループ用のクラスです。<hr>

**[引数]**

- `dict_`: Dictionary[_DictKey, Any]
  - イテレーションで扱うための辞書。

- `dict_key_type`: Type[_DictKey]
  - 辞書のキーの型。このインターフェイスは`String`、`Int`、`Number`、`Boolean`といったハッシュ化可能な型を受け付けます。

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
>>> dict_: ap.Dictionary[ap.String, ap.Boolean] = ap.Dictionary(
...     {
...         ap.String("apple"): ap.Boolean(True),
...         ap.String("orange"): ap.Boolean(False),
...     }
... )
>>> keys: ap.Array[ap.String] = ap.Array([])
>>> with ap.ForDictKeys(dict_=dict_, dict_key_type=ap.String) as key:
...     keys.append(key)
...
>>> ap.assert_arrays_equal(
...     keys,
...     ["apple", "orange"],
... )
```