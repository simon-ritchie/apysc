<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](../en/dictionary_generic.html)の確認をお願いします。</span>

# Dictionary クラスのジェネリックの型アノテーション設定

このページでは`Dictionary`クラスのキーと値のジェネリックの型アノテーション設定について説明します。

## 基本的な使い方

以下のコードのように、`Dictionary`クラスではキーと値に対してジェネリックの型アノテーションを行うことができます:

```py
# runnable
import apysc as ap

dict_value: ap.Dictionary[str, int] = ap.Dictionary({'a': 10})
a_value: int = dict_value['a']
```

これらのジェネリックの型アノテーションはmypyやPylanceなどのライブラリによるチェックや安全面で役に立つことがあります。

例えば、以下のコード例では辞書の値の型に対するPylanceがエラーが発生します:

```py
# runnable
import apysc as ap

dict_value: ap.Dictionary[str, int] = ap.Dictionary({'a': 10})
a_value: str = dict_value['a']
```

```
Expression of type "int" cannot be assigned to declared type "str"
  "int" is incompatible with "str"
```

同じように、以下のコード例では辞書のキーの型でエラーが発生します（`str`が必要になっている一方で`int`が指定されています）。

```py
# runnable
import apysc as ap

dict_value: ap.Dictionary[str, int] = ap.Dictionary({'a': 10})
a_value: int = dict_value[10]
```

もし複数の型の指定が必要な場合、以下のコード例のように`Union`を使うこともできます。

特記事項: もしPython3.10以降をお使いの場合には`|`の記号などを代わりに使用することができます（もしくは`Any`の型を指定するなど）。

```py
# runnable
from typing import Union

import apysc as ap

# Accepting the str and int key types.
dict_value: ap.Dictionary[Union[int, str], int] = ap.Dictionary(
    {'a': 10, 2: 20})
a_value: int = dict_value['a']
b_value: int = dict_value[2]
```

```py
# runnable
from typing import Any

import apysc as ap

# Accepting all types by specifying the Any type.
dict_value: ap.Dictionary[Any, Any] = ap.Dictionary(
    {'a': 10, 2: 'b'})
a_value: int = dict_value['a']
b_value: str = dict_value[2]
```