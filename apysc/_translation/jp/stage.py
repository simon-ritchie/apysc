"""This module is for the translation mapping data of the
following document:

Document file: stage.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Stage class": "# Stage クラス",
    ##################################################
    "This page explains the `Stage` class.": "このページでは`Stage`クラスについて説明します。",
    ##################################################
    "## What is the Stage?": "## Stage クラスの概要",
    ##################################################
    "The `Stage` is the apysc overall drawing area (like a viewport) and contains all elements.": "`Stage`クラスはapyscにおける描画エリア全体を扱うインスタンスを作成し、各要素を格納します。",  # noqa
    ##################################################
    "You must create the `Stage` at the first of the apysc project (this runs cleaning up internal data and files).": "apyscのプロジェクトの最初で`Stage`のインスタンスを作成する必要があります（この時点で内部でデータやファイルの古いものの削除などが実行されます）。",  # noqa
    ##################################################
    "## Create stage": "## ステージの作成",
    ##################################################
    "Creating a stage is simple, like this:": "ステージの作成は以下のコード例のようにシンプルです:",
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage()\n```": "```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage()\n```",  # noqa
    ##################################################
    "## Stage background color setting": "## ステージの背景色設定",
    ##################################################
    "`Stage` class has a `background_color` option, which changes the stage's background color.": "`Stage`クラスは`background_color`のオプションの引数を持っており、この引数でステージの背景色を変更することができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(background_color="#333", stage_elem_id="stage")\n\nap.save_overall_html(dest_dir_path="stage_background_color/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(background_color="#333", stage_elem_id="stage")\n\nap.save_overall_html(dest_dir_path="stage_background_color/")\n```',  # noqa
    ##################################################
    "This will create HTML with black background stage, as follows:": "このコードは以下のように黒背景のステージのHTMLを生成します:",  # noqa
    ##################################################
    "## Stage size setting": "## ステージのサイズ設定",
    ##################################################
    "`Stage` class has options to set stage width and stage height (arguments of `stage_width` and `stage_height`). These settings change stage sizes.": "`Stage`クラスはステージの幅を設定する`stage_width`引数とステージの高さを設定する`stage_height`引数を持っています。これらの設定はステージのサイズを変更します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=500, stage_height=50, background_color="#333", stage_elem_id="stage"\n)\n\nap.save_overall_html(dest_dir_path="stage_size/")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=500, stage_height=50, background_color="#333", stage_elem_id="stage"\n)\n\nap.save_overall_html(dest_dir_path="stage_size/")\n```',  # noqa
    ##################################################
    "The Previous script will create a horizontal stage, as follows:": "上記のコードは以下のように横長のステージを作成します:",  # noqa
    ##################################################
    "## Stage element id setting": "## ステージの要素のID設定",
    ##################################################
    "Stage element id (HTML id) can be set by `stage_elem_id` argument. If you don't specify this, the apysc sets any unique id (based on created timestamp, like `stage_12345...`).": "ステージの要素のID（HTMLのID）は`stage_elem_id`引数で設定することができます。もしもこの設定を指定しない場合、apyscはステージ生成時のタイムスタンプや乱数などをベースとした一意なIDを生成します（例 : `stage_12345...`）。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(background_color="#333", stage_elem_id="line_chart_1")\n```': '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(background_color="#333", stage_elem_id="line_chart_1")\n```',  # noqa
    ##################################################
    "This option is useful when using the apysc project multiple times (for an easily identifiable ID) or version control.": "このオプションはapyscの各プロジェクトで複数回出力などを行う際のIDの識別やバージョン管理などの面で便利です。",  # noqa
    ##################################################
    "## get_stage function interface": "## get_stage 関数のインターフェイス",
    ##################################################
    "The `get_stage` function returns the current stage instance.": "`get_stage`関数は現在生成済みのステージのインスタンスを返却します。",  # noqa
    ##################################################
    "This interface is sometimes useful to get a stage instance in the other function's scope.": "このインターフェイスは他の関数のスコープ内などでステージのインスタンスを参照したい場合などに便利なことがあります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\n\ndef _main() -> None:\n    """\n    Entry point of this project.\n    """\n    _: ap.Stage = ap.Stage(\n        stage_width=150,\n        stage_height=150,\n        background_color="#333",\n        stage_elem_id="my_stage",\n    )\n    ...\n    _other_function()\n\n\ndef _other_function() -> None:\n    """\n    The other function to do something.\n    """\n    stage: ap.Stage = ap.get_stage()\n    assert stage.stage_elem_id == "my_stage"\n\n\n_main()\n```': '```py\n# runnable\nimport apysc as ap\n\n\ndef _main() -> None:\n    """\n    Entry point of this project.\n    """\n    _: ap.Stage = ap.Stage(\n        stage_width=150,\n        stage_height=150,\n        background_color="#333",\n        stage_elem_id="my_stage",\n    )\n    ...\n    _other_function()\n\n\ndef _other_function() -> None:\n    """\n    The other function to do something.\n    """\n    stage: ap.Stage = ap.get_stage()\n    assert stage.stage_elem_id == "my_stage"\n\n\n_main()\n```',  # noqa
    ##################################################
    "## Stage class constructor API": "## Stage クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Create Stage (overall viewport) instance.<hr>": "ステージ（描画領域全体）のインスタンスを生成します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `stage_width`: int, default 300": "- `stage_width`: int, default 300",
    ##################################################
    "  - Stage width.": "  - ステージの幅。",
    ##################################################
    "- `stage_height`: int, default 185": "- `stage_height`: int, default 185",
    ##################################################
    "  - Stage height": "  - ステージの高さ。",
    ##################################################
    "- `background_color`: str, default '#ffffff'": "- `background_color`: str, default '#ffffff'",  # noqa
    ##################################################
    "  - Hexadecimal background color string.": "  - 16進数の背景色の文字列。",
    ##################################################
    "- `add_to`: str, default 'body'": "- `add_to`: str, default 'body'",
    ##################################################
    "  - Specification of element to add stage. Unique tag (e.g., 'body') or ID selector (e.g., '#any-unique-elem') is acceptable.": "  - ステージの要素を追加先となる要素の指定。一意のタグ（例 : 'body'）やIDのセレクタ（例 : '#any-unique-elem'）を受け付けることができます。",  # noqa
    ##################################################
    "- `stage_elem_id`: str or None, optional": "- `stage_elem_id`: str or None, optional",  # noqa
    ##################################################
    "  - ID attribute set to stage HTML element (e.g., 'line-graph'). If None is set, a random integer will be applied.": "  - ステージのHTML要素に設定されるIDの属性（例 : 'line-graph'）。もしNoneが設定されている場合、乱数などを使った数値を使った値が設定されます。",  # noqa
    ##################################################
    "- `variable_name_suffix`: str, default ''": "- `variable_name_suffix`: str, default ''",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     stage_width=500,\n...     stage_height=300,\n...     background_color="#333",\n...     stage_elem_id="sales_chart",\n... )\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     stage_width=500,\n...     stage_height=300,\n...     background_color="#333",\n...     stage_elem_id="sales_chart",\n... )\n```',  # noqa
    ##################################################
    "## stage_elem_id property API": "## stage_elem_id 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get stage's html element id.<hr>": "ステージのHTML要素のIDを取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `stage_elem_id`: str": "- `stage_elem_id`: str",
    ##################################################
    "  - Stage's html element id (not including class or id symbol). e.g., 'line-graph'": "  - ステージのHTML要素のID（ID用の#の記号などは含まれません。例 : 'line-graph'）。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     stage_width=500,\n...     stage_height=300,\n...     background_color="#333",\n...     stage_elem_id="sales_chart",\n... )\n>>> stage.stage_elem_id\n\'sales_chart\'\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     stage_width=500,\n...     stage_height=300,\n...     background_color="#333",\n...     stage_elem_id="sales_chart",\n... )\n>>> stage.stage_elem_id\n\'sales_chart\'\n```',  # noqa
    ##################################################
    "## add_child API": "## add_child API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Add display object child to this instance.<hr>": "表示オブジェクトの子をこのインスタンスへと追加します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `child`: DisplayObject": "- `child`: DisplayObject",
    ##################################################
    "  - Child instance to add.": "  - 追加する子のインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite_1: ap.Sprite = ap.Sprite()\n>>> sprite_1.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> sprite_2: ap.Sprite = ap.Sprite()\n>>> sprite_2.add_child(rectangle)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite_1: ap.Sprite = ap.Sprite()\n>>> sprite_1.graphics.begin_fill(color="#0af")\n>>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> sprite_2: ap.Sprite = ap.Sprite()\n>>> sprite_2.add_child(rectangle)\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [add_child and remove_child interfaces](https://simon-ritchie.github.io/apysc/en/add_child_and_remove_child.html)": "- [add_child （子の追加）と remove_child （子の削除）のインターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_add_child_and_remove_child.html)",  # noqa
    ##################################################
    "## remove_child API": "## remove_child API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Remove display object child from this instance.<hr>": "このインスタンスから指定された表示オブジェクトの子を取り除きます。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `child`: DisplayObject": "- `child`: DisplayObject",
    ##################################################
    "  - Child instance to remove.": "  - 取り除く対象の子のインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> sprite.graphics.remove_child(rectangle)\n>>> print(rectangle.parent)\nNone\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> sprite.graphics.remove_child(rectangle)\n>>> print(rectangle.parent)\nNone\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [add_child and remove_child interfaces](https://simon-ritchie.github.io/apysc/en/add_child_and_remove_child.html)": "- [add_child （子の追加）と remove_child （子の削除）のインターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_add_child_and_remove_child.html)",  # noqa
    ##################################################
    "## contains API": "## contains API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a boolean whether this instance contains a specified child.<hr>": "指定された子のインスタンスを持っているかどうかの真偽値を取得します。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `child`: DisplayObject": "- `child`: DisplayObject",
    ##################################################
    "  - Child instance to check.": "  - チェック対象の子のインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `result`: Boolean": "- `result`: Boolean",
    ##################################################
    "  - If this instance contains a specified child, this method returns True.": "  - このインスタンスが指定された子を持つ場合Trueが設定されます。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> sprite.graphics.contains(rectangle)\nBoolean(True)\n\n>>> rectangle.remove_from_parent()\n>>> sprite.graphics.contains(rectangle)\nBoolean(False)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> sprite.graphics.contains(rectangle)\nBoolean(True)\n\n>>> rectangle.remove_from_parent()\n>>> sprite.graphics.contains(rectangle)\nBoolean(False)\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [contains interface](https://simon-ritchie.github.io/apysc/en/contains.html)": "- [contains インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_contains.html)",  # noqa
    ##################################################
    "## num_children property API": "## num_children property API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a current children's number.<hr>": "現在の子の数を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `num_children`: int": "- `num_children`: int",
    ##################################################
    "  - Current children number.": "  - 現在の子の数。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)\n>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=150, y=50, width=50, height=50\n... )\n>>> sprite.graphics.num_children\nInt(2)\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)\n>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=150, y=50, width=50, height=50\n... )\n>>> sprite.graphics.num_children\nInt(2)\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [num_children interface](https://simon-ritchie.github.io/apysc/en/num_children.html)": "- [num_children （子の件数属性）のインターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_num_children.html)",  # noqa
    ##################################################
    "## get_child_at API": "## get_child_at API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a child at a specified index.<hr>": "指定されたインデックスの子を取得します。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `index`: int or Int": "- `index`: int or Int",
    ##################################################
    "  - Child's index (start from 0).": "  - 対象の子のインデックス（0からスタートします）。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `child`: DisplayObject": "- `child`: DisplayObject",
    ##################################################
    "  - Target index child instance.": "  - 対象の子のインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)\n>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=150, y=50, width=50, height=50\n... )\n>>> child_at_index_1: ap.DisplayObject = sprite.graphics.get_child_at(1)\n>>> child_at_index_1 == rectangle_2\nTrue\n```': '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)\n>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50\n... )\n>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=150, y=50, width=50, height=50\n... )\n>>> child_at_index_1: ap.DisplayObject = sprite.graphics.get_child_at(1)\n>>> child_at_index_1 == rectangle_2\nTrue\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [get_child_at interface](https://simon-ritchie.github.io/apysc/en/get_child_at.html)": "- [get_child_at （特定位置の子の取得処理）のインターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_get_child_at.html)",  # noqa
    ##################################################
    "## get_stage API": "## get_stage のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get an already instantiated stage instance.<hr>": "既に生成済みのステージのインスタンスを取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `stage`: Stage": "- `stage`: Stage",
    ##################################################
    "  - Target stage instance.": "  - 対象のステージのインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Raises]**": "**[エラー発生条件]**",
    ##################################################
    "- _StageNotCreatedError: If there is no instantiated stage yet.": "- _StageNotCreatedError: もしもまだ生成済みのステージのインスタンスが存在しない場合。",  # noqa
}
