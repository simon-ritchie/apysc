# For

This page will explain the `For` class.

Before reading on, maybe it is useful to read the following page (the `For` class will be used for the same reason of each apysc data type):

- [Why not using the Python built-in data type in the apysc library?](why_not_using_python_builtin_data_type.md)

## What is the For class?

The `For` class is the apysc for loop class. It will behave like the Python built-in `for` keyword.

## Basic usage

The `For` class will be used at the `with` statement. The `as` keyword value will be the `Int` type index (`i` variable).

The following example will draw the three rectangles in the `with For` block:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=350, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
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

The `For` class constructor's first argument will accept an `Array` or `Dictionary` value. If a `Dictionary` value is passed then the `as` keyword value will be a `String` value, not `Int`.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=250, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)

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

## See also

- [Each branch instruction class scope variables reverting setting](branch_instruction_variables_reverting_setting.md)
  - Notes: the `For` class also has the same arguments and behaves as the same way.
