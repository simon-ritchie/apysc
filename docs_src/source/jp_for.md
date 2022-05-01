<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/for.html)の確認をお願いします。</span>

# For クラス

このページでは`For`クラスについて説明します。

このページを読み進める前に以下のページを事前に確認しておくと役に立つかもしれません（apyscでは`For`クラスを各データ型のクラスと同じ理由で使用しています）。

- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)

## For クラスの概要

`For`クラスはapyscのループ制御用のクラスです。このクラスはPythonのビルトインの`for`のキーワードのように動作します。

## 基本的な使い方

`For`クラスは`with`ステートメントと一緒に使用する必要があります。`as`のキーワードの値は`Int`型のインデックス（`i`の変数）もしくは`String`型のキーになります。

以下のコード例では3つの四角を`with For`のブロック内で描画しています:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=350, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

arr: ap.Array[int] = ap.Array(range(3))
i: ap.Int
with ap.For(arr) as i:
    sprite.graphics.draw_rect(
        x=i * 100 + 50, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='for_basic_usage/')
```

<iframe src="static/for_basic_usage/index.html" width="350" height="150"></iframe>

`For`クラスの第一引数は`Array`もしくは`Dictionary`クラスの値を受け付けます。もしも`Dictionary`の値を指定した場合、`as`のキーワードの値は`Int`の代わりに`String`の値になります。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=250, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

dict_val: ap.Dictionary = ap.Dictionary(
    {'magenta': ap.String('#f0a'), 'cyan': ap.String('#0af')})
key: ap.String
with ap.For(dict_val) as key:
    color: ap.String = dict_val[key]
    sprite.graphics.begin_fill(color=color)
    condition_1: ap.Boolean = key == 'magenta'
    condition_2: ap.Boolean = key == 'cyan'
    with ap.If(condition_1):
        sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
    with ap.Elif(condition_2):
        sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='for_basic_usage_with_dict/')
```

<iframe src="static/for_basic_usage_with_dict/index.html" width="250" height="150"></iframe>

## 関連資料

- [分岐条件の各クラスのスコープ内変数の復元設定](jp_branch_instruction_variables_reverting_setting.md)
  - 特記事項: `For`クラスは同じ各引数を持っており、同じように動作します。

## For API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `__init__(self, arr_or_dict:Union[apysc._type.array.Array, apysc._type.dictionary.Dictionary], *, locals_:Union[Dict[str, Any], NoneType]=None, globals_:Union[Dict[str, Any], NoneType]=None) -> None`<hr>

**[インターフェイス概要]** forのループのコード表現を追加するためのクラスです。<hr>

**[引数]**

- `arr_or_dict`: Array or Dictionary
  - ループで使用するためのArray もしくは Dictionary クラスのインスタンス。

- `locals_`: dict or None, default None
  - 現在のスコープのローカル変数。設定する場合にはlocals()関数の値をこの引数に指定してください。もし設定された場合にはこのいんたーふぇいろは`For`クラスによるスコープの終わりにVariableNameInterfaceを継承した各変数（IntやSpriteなど）の値を元の状態に復元します。この設定はもしも変数の値を`For`のスコープ内で更新したくない場合などに便利な時があります。

- `globals_`: dict or None, default None
  - 現在のスコープの各グローバル変数。設定する場合にはglobal()関数の値をこの引数に指定してください。この設定はlocals_引数と同じように動作します。

<hr>

**[コードサンプル]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array(range(3))
>>> with ap.For(arr) as i:
...     ap.trace('Loop index is:', i)
```