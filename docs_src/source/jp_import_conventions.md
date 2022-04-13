<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](import_conventions.md)の確認をお願いします。</span>

# import の慣習

apyscのライブラリでは他のPythonパッケージの`import numpy as np`、`import pandas as pd`、`import tkinter as tk`などと同じように`import apysc as ap`というimportの指定を推奨しています。

モジュールのルートのパッケージパスにapyscで利用が必要な各インターフェイスが設定されています（例 : `Sprite`、`Int`、`Stage`など）。

また、パッケージの内部で使用するロジックの各モジュールは`_file`のようにアンダースコアのプレフィックスが設定されています。基本的にこれらのプレフィックスの付いたパッケージの利用は不要です。

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
number_1: ap.Number = int_1 + ap.Number(10.5)
```