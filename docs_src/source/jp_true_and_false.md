<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/true_and_false.html)の確認をお願いします。</span>

# True_ と False_ の各定数

このページでは`ap.True_`と`ap.False_`の各定数について説明します。

## 各定数の概要

`ap.True_`は`Boolean`の`True`の値を示すたの定数値です（これは`ap.Boolean(True)`とほぼ同じ値となります）。

反対に、`ap.False_`は`Boolean`の`False`の値を示すための定数となります。

## 基本的な使い方

`True_`と`False_`の各定数は`ap.Boolean(True)`や`ap.Boolean(False)`などと同じように振る舞います。

`Boolean`の引数を取る関数やメソッドなどではこれらの定数を指定することができます。

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=100,
    stage_height=50,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
text: ap.SvgText = ap.SvgText(
    text="Hello!",
    x=10,
    y=31,
    fill_color=ap.Color("#aaa"),
    bold=ap.True_,
    italic=ap.False_,
)

ap.save_overall_html(dest_dir_path="true_and_false_basic_usage/")
```

<iframe src="static/true_and_false_basic_usage/index.html" width="100" height="50"></iframe>