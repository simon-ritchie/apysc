<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/assertion_basic_behavior.html)の確認をお願いします。</span>

# JavaScript 上のアサーションのインターフェイスの基本的な挙動

このページではJavaScript上でのアサーション（テストなどのチェック処理）の各インターフェイスの基本的な挙動について説明します。

## 各インターフェイス名について

JavaScript上の各アサーションのインターフェイスは`assert_`のプレフィックスを持っています（例 : `assert_equal`や`assert_true`など）。

これらのインターフェイスはapyscのルートのパッケージに配置されているため、たとえば`ap.assert_equal(...)`といった記述で使うことができます。

## アサーションの結果について

これらのインターフェイスのチェック結果は以下の例のようにブラウザのコンソール上に表示されます:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
int_1: ap.Int = ap.Int(10)
ap.assert_equal(left=10, right=int_1)
ap.save_overall_html(dest_dir_path="assertion_basic_behavior_results/")
```

上記のコード例ではブラウザのコンソール上に以下のような結果の情報が表示されます（ブラウザ上でF12キーを押して確認してください）:

```
[assert_equal]
Right-side variable name: i_11
Left value: 10 right value: 10
```

<iframe src="static/assertion_basic_behavior_results/index.html" width="0" height="0"></iframe>

もしチェック処理に失敗した場合も同様にブラウザのコンソール上にエラーメッセージが表示されます:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
int_1: ap.Int = ap.Int(10)
ap.assert_equal(left=11, right=int_1)
ap.save_overall_html(dest_dir_path="assertion_basic_behavior_results_failed/")
```

```
[assert_equal]
Right-side variable name: i_11
Left value: 11 right value: 10
...
Assertion failed:
...
```

<iframe src="static/assertion_basic_behavior_results_failed/index.html" width="0" height="0"></iframe>

## 省略可能なmsg引数について

各インターフェイスは共通して`msg`という省略可能な引数のとオプションを持っています。もしこの引数に値を指定した場合、チェック処理に失敗した場合にエラーの詳細のメッセージとしてブラウザのコンソール上に表示されます。

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
int_1: ap.Int = ap.Int(10)
ap.assert_equal(left=11, right=int_1, msg="Values are not equal!")
ap.save_overall_html(dest_dir_path="assertion_basic_behavior_msg/")
```

```
[assert_equal]
Right-side variable name: i_11
Left value: 11 right value: 10
...
Assertion failed: Values are not equal!
```

<iframe src="static/assertion_basic_behavior_msg/index.html" width="0" height="0"></iframe>