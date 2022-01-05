# JavaScript assertion interface basic behaviors

This page explains the JavaScript assertion interface basic behavior.

## Interface names

Each JavaScript assertion interface has the prefix of the `assert_` (e.g., `assert_equal`, `assert_true`, and so on).

These interfaces are positioned in the root package so you can use them, for example, `ap.assert_equal(...)`.

## Assertion results

These interfaces display the results on the browser console, as follows:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')
int_1: ap.Int = ap.Int(10)
ap.assert_equal(left=10, right=int_1)
ap.save_overall_html(
    dest_dir_path='assertion_common_behavior_results/')
```

This code displays the information message on the browser console, like this (please press the F12 key to see):

```
[assert_equal]
Right-side variable name: i_11
Left value: 10 right value: 10
```

<iframe src="static/assertion_common_behavior_results/index.html" width="0" height="0"></iframe>

If the assertion fails, then an error message also is displayed on the browser console:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')
int_1: ap.Int = ap.Int(10)
ap.assert_equal(left=11, right=int_1)
ap.save_overall_html(
    dest_dir_path='assertion_common_behavior_results_failed/')
```

```
[assert_equal]
Right-side variable name: i_11
Left value: 11 right value: 10
...
Assertion failed:
...
```

<iframe src="static/assertion_common_behavior_results_failed/index.html" width="0" height="0"></iframe>

## Optional msg argument

Each assertion interface has the `msg` optional argument. If you provide this argument, the error message is displayed on the browser console when an assertion fails.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0, stage_height=0, background_color='#333',
    stage_elem_id='stage')
int_1: ap.Int = ap.Int(10)
ap.assert_equal(left=11, right=int_1, msg='Values are not equal!')
ap.save_overall_html(
    dest_dir_path='assertion_common_behavior_msg/')
```

```
[assert_equal]
Right-side variable name: i_11
Left value: 11 right value: 10
...
Assertion failed: Values are not equal!
```

<iframe src="static/assertion_common_behavior_msg/index.html" width="0" height="0"></iframe>
