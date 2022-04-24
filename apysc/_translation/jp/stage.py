"""This module is for the translation mapping data of the
following document:

Document file: stage.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Stage class':
    '# Stage クラス',

    'This page explains the `Stage` class.':
    'このページでは`Stage`クラスについて説明します。',

    '## What is the Stage?':
    '## Stage クラスの概要',

    'The `Stage` is the apysc overall drawing area (like a viewport) and contains all elements.':  # noqa
    '`Stage`クラスはapyscにおける描画エリア全体を扱うインスタンスを作成し、各要素を格納します。',

    'You must create the `Stage` at the first of the apysc project (this runs cleaning up internal data and files).':  # noqa
    'apyscのプロジェクトの最初で`Stage`のインスタンスを作成する必要があります（この時点で内部でデータやファイルの古いものの削除などが実行されます）。',  # noqa

    '## Create stage':
    '## ステージの作成',

    'Creating a stage is simple, like this:':
    'ステージの作成は以下のコード例のようにシンプルです:',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage()\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage()\n```',  # noqa

    '## Stage background color setting':
    '## ステージの背景色設定',

    '`Stage` class has a `background_color` option, which changes the stage\'s background color.':  # noqa
    '`Stage`クラスは`background_color`のオプションの引数を持っており、この引数でステージの背景色を変更することができます。',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nap.save_overall_html(\n    dest_dir_path=\'stage_background_color/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nap.save_overall_html(\n    dest_dir_path=\'stage_background_color/\')\n```',  # noqa

    'This will create HTML with black background stage, as follows:':
    'このコードは以下のように黒背景のステージのHTMLを生成します:',

    '## Stage size setting':
    '## ステージのサイズ設定',

    '`Stage` class has options to set stage width and stage height (arguments of `stage_width` and `stage_height`). These settings change stage sizes.':  # noqa
    '`Stage`クラスはステージの幅を設定する`stage_width`引数とステージの高さを設定する`stage_height`引数を持っています。これらの設定はステージのサイズを変更します。',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=500, stage_height=50,\n    background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nap.save_overall_html(\n    dest_dir_path=\'stage_size/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=500, stage_height=50,\n    background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nap.save_overall_html(\n    dest_dir_path=\'stage_size/\')\n```',  # noqa

    'The Previous script will create a horizontal stage, as follows:':
    '上記のコードは以下のように横長のステージを作成します:',

    '## Stage element id setting':
    '## ステージの要素のID設定',

    'Stage element id (HTML id) can be set by `stage_elem_id` argument. If you don\'t specify this, the apysc sets any unique id (based on created timestamp, like `stage_12345...`).':  # noqa
    'ステージの要素のID（HTMLのID）は`stage_elem_id`引数で設定することができます。もしもこの設定を指定しない場合、apyscはステージ生成時のタイムスタンプや乱数などをベースとした一意なIDを生成します（例 : `stage_12345...`）。',  # noqa

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=\'#333\',\n    stage_elem_id=\'line_chart_1\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=\'#333\',\n    stage_elem_id=\'line_chart_1\')\n```',  # noqa

    'This option is useful when using the apysc project multiple times (for an easily identifiable ID) or version control.':  # noqa
    'このオプションはapyscの各プロジェクトで複数回出力などを行う際のIDの識別やバージョン管理などの面で便利です。',

    '## Stage class constructor API':
    '## Stage クラスのコンストラクタのAPI',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Create Stage (overall viewport) instance.<hr>':
    '**[インターフェイス概要]** ステージ（描画領域全体）のインスタンスを生成します。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `stage_width`: int, default 300':
    '- `stage_width`: int, default 300',

    '  - Stage width.':
    '  - ステージの幅。',

    '- `stage_height`: int, default 185':
    '- `stage_height`: int, default 185',

    '  - Stage height':
    '  - ステージの高さ。',

    '- `background_color`: str, default \'#ffffff\'':
    '- `background_color`: str, default \'#ffffff\'',

    '  - Hexadecimal background color string.':
    '  - 16進数の背景色の文字列。',

    '- `add_to`: str, default \'body\'':
    '- `add_to`: str, default \'body\'',

    '  - Specification of element to add stage. Unique tag (e.g., \'body\') or ID selector (e.g., \'#any-unique-elem\') is acceptable.':  # noqa
    '  - ステージの要素を追加先となる要素の指定。一意のタグ（例 : \'body\'）やIDのセレクタ（例 : \'#any-unique-elem\'）を受け付けることができます。',  # noqa

    '- `stage_elem_id`: str or None, optional':
    '- `stage_elem_id`: str or None, optional',

    '  - ID attribute set to stage html element (e.g., \'line-graph\'). If None is set, random integer will be applied.':  # noqa
    '  - ステージのHTML要素に設定されるIDの属性（例 : \'line-graph\'）。もしNoneが設定されている場合、乱数などを使った数値を使った値が設定されます。',  # noqa

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     stage_width=500, stage_height=300,\n...     background_color=\'#333\', stage_elem_id=\'sales_chart\')\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     stage_width=500, stage_height=300,\n...     background_color=\'#333\', stage_elem_id=\'sales_chart\')\n```',  # noqa

    '## stage_elem_id property API':
    '## stage_elem_id 属性のAPI',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Get stage\'s html element id.<hr>':
    '**[インターフェイス概要]** ステージのHTML要素のIDを取得します。<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `stage_elem_id`: str':
    '- `stage_elem_id`: str',

    '  - Stage\'s html element id (not including class or id symbol). e.g., \'line-graph\'':  # noqa
    '  - ステージのHTML要素のID（ID用の#の記号などは含まれません。例 : \'line-graph\'）。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     stage_width=500, stage_height=300,\n...     background_color=\'#333\', stage_elem_id=\'sales_chart\')\n>>> stage.stage_elem_id\n\'sales_chart\'\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     stage_width=500, stage_height=300,\n...     background_color=\'#333\', stage_elem_id=\'sales_chart\')\n>>> stage.stage_elem_id\n\'sales_chart\'\n```',  # noqa

    '## add_child API':
    '## add_child API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Add display object child to this instance.<hr>':  # noqa
    '**[インターフェイス概要]** 表示オブジェクトの子をこのインスタンスへと追加します。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `child`: DisplayObject':
    '- `child`: DisplayObject',

    '  - Child instance to add.':
    '  - 追加する子のインスタンス。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite_1: ap.Sprite = ap.Sprite()\n>>> sprite_1.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> sprite_2: ap.Sprite = ap.Sprite()\n>>> sprite_2.add_child(rectangle)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite_1: ap.Sprite = ap.Sprite()\n>>> sprite_1.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> sprite_2: ap.Sprite = ap.Sprite()\n>>> sprite_2.add_child(rectangle)\n```',  # noqa

    '<hr>':
    '<hr>',

    '**[References]**':
    '**[関連資料]**',

    '- [add_child and remove_child interfaces document](https://simon-ritchie.github.io/apysc/add_child_and_remove_child.html)':  # noqa
    '- [add_child （子の追加）と remove_child （子の削除）のインターフェイス](https://simon-ritchie.github.io/apysc/jp_add_child_and_remove_child.html)',  # noqa

    '## remove_child API':
    '## remove_child API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Remove display object child from this instance.<hr>':  # noqa
    '**[インターフェイス概要]** このインスタンスから指定された表示オブジェクトの子を取り除きます。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `child`: DisplayObject':
    '- `child`: DisplayObject',

    '  - Child instance to remove.':
    '  - 取り除く対象の子のインスタンス。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> sprite.graphics.remove_child(rectangle)\n>>> print(rectangle.parent)\nNone\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> sprite.graphics.remove_child(rectangle)\n>>> print(rectangle.parent)\nNone\n```',  # noqa

    '<hr>':
    '<hr>',

    '**[References]**':
    '**[関連資料]**',

    '- [add_child and remove_child interfaces document](https://simon-ritchie.github.io/apysc/add_child_and_remove_child.html)':  # noqa
    '- [add_child （子の追加）と remove_child （子の削除）のインターフェイス](https://simon-ritchie.github.io/apysc/jp_add_child_and_remove_child.html)',  # noqa

    '## contains API':
    '## contains API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Get a boolean whether this instance contains a specified child.<hr>':  # noqa
    '**[インターフェイス概要]** 指定された子のインスタンスを持っているかどうかの真偽値を取得します。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `child`: DisplayObject':
    '- `child`: DisplayObject',

    '  - Child instance to check.':
    '  - チェック対象の子のインスタンス。',

    '<hr>':
    '<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `result`: Boolean':
    '- `result`: Boolean',

    '  - If this instance contains a specified child, this method returns True.':  # noqa
    '  - このインスタンスが指定された子を持つ場合Trueが設定されます。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> sprite.graphics.contains(rectangle)\nBoolean(True)\n\n>>> rectangle.remove_from_parent()\n>>> sprite.graphics.contains(rectangle)\nBoolean(False)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> sprite.graphics.contains(rectangle)\nBoolean(True)\n\n>>> rectangle.remove_from_parent()\n>>> sprite.graphics.contains(rectangle)\nBoolean(False)\n```',  # noqa

    '<hr>':
    '<hr>',

    '**[References]**':
    '**[関連資料]**',

    '- [contains interface document](https://simon-ritchie.github.io/apysc/contains.html)':  # noqa
    '- [contains インターフェイス](https://simon-ritchie.github.io/apysc/jp_contains.html)',  # noqa

    '## num_children property API':
    '## num_children property API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Get a current children\'s number.<hr>':
    '**[インターフェイス概要]** 現在の子の数を取得します。<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `num_children`: int':
    '- `num_children`: int',

    '  - Current children number.':
    '  - 現在の子の数。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=150, y=50, width=50, height=50)\n>>> sprite.graphics.num_children\nInt(2)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=150, y=50, width=50, height=50)\n>>> sprite.graphics.num_children\nInt(2)\n```',  # noqa

    '<hr>':
    '<hr>',

    '**[References]**':
    '**[関連資料]**',

    '- [num_children interface document](https://simon-ritchie.github.io/apysc/num_children.html)':  # noqa
    '- [num_children （子の件数属性）のインターフェイス](https://simon-ritchie.github.io/apysc/jp_num_children.html)',  # noqa

    '## get_child_at API':
    '## get_child_at API',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Get child at a specified index.<hr>':
    '**[インターフェイス概要]** 指定されたインデックス位置の子を取得します。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `index`: int or Int':
    '- `index`: int or Int',

    '  - Child\'s index (start from 0).':
    '  - 対象の子のインデックス（0からスタートします）。',

    '<hr>':
    '<hr>',

    '**[Returns]**':
    '**[返却値]**',

    '- `child`: DisplayObject':
    '- `child`: DisplayObject',

    '  - Target index child instance.':
    '  - 対象の子のインスタンス。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=150, y=50, width=50, height=50)\n>>> child_at_index_1: ap.DisplayObject = (\n...     sprite.graphics.get_child_at(1))\n>>> child_at_index_1 == rectangle_2\nTrue\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=150, y=50, width=50, height=50)\n>>> child_at_index_1: ap.DisplayObject = (\n...     sprite.graphics.get_child_at(1))\n>>> child_at_index_1 == rectangle_2\nTrue\n```',  # noqa

    '<hr>':
    '<hr>',

    '**[References]**':
    '**[関連資料]**',

    '- [get_child_at interface document](https://simon-ritchie.github.io/apysc/get_child_at.html)':  # noqa
    '- [get_child_at （特定位置の子の取得処理）のインターフェイス](https://simon-ritchie.github.io/apysc/jp_get_child_at.html)',  # noqa

}
