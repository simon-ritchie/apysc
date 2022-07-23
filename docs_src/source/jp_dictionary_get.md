<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/dictionary_get.html)の確認をお願いします。</span>

# Dictionary クラスの get インターフェイス

このページでは`Dictionary`クラスの`get`メソッドのインターフェイスについて説明します。

## インターフェイス概要

`get`メソッドは引数に指定されたキーの値を返却します。もし指定されたキーが辞書内に存在しなければデフォルトの値を返却します（キーが無くともエラーにはなりません）。

## 基本的な使い方

`get`メソッドは`key`（辞書のキー）の第一引数を必要とします。第二引数の`default`引数は省略可で、もし指定されなければ`None`がデフォルト値となります。

```py
# runnable
from typing import Any, Optional

import apysc as ap

dict_val: ap.Dictionary = ap.Dictionary({"a": 10})
got_val_1: int = dict_val.get(key="a", default=0)
assert got_val_1 == 10

got_val_2: int = dict_val.get(key="b", default=0)
assert got_val_2 == 0

got_val_3: Optional[Any] = dict_val.get(key="b")
assert got_val_3 is None
```

## get API

<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>

**[インターフェイスの構造]** `get(self, key: Union[~_K, apysc._type.expression_string.ExpressionString], *, default: ~DefaultType = None) -> ~DefaultType`<hr>

**[インターフェイス概要]** 指定されたキーの辞書の値を取得します。もし辞書が指定されたキーを持っていない場合はデフォルト値を返却します。<hr>

**[引数]**

- `key`: _K
  - 対象のキー。

- `default`: DefaultType or None, optional
  - 任意のデフォルト値の値。

<hr>

**[返却値]**

- `result_value`: Any
  - 抽出された値もしくはデフォルト値。

<hr>

**[コードサンプル]**

```py
>>> from typing import Optional
>>> import apysc as ap
>>> dictionary: ap.Dictionary = ap.Dictionary({'a': 10})
>>> value_1: Optional[int] = dictionary.get('a')
>>> value_1
10

>>> value_2: Optional[int] = dictionary.get('b')
>>> print(value_2)
None

>>> value_3: int = dictionary.get('c', default=0)
>>> value_3
0
```