# save_overall_html interface

This page explains the `save_overall_html` function interface.

## What interface is this?

The `save_overall_html` function interface will export the overall HTML and JavaScript files. At the end of the apysc project, this function's calling is necessary to export the HTML.

## Basic usage

The `save_overall_html` function need at least one argument, `dest_dir_path`. This argument determines a directory path to save HTML and JavaScript files.

The following code example exports the HTML and JavaScript files, and the exported HTML displays the blank stage (150 px width and height).

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

ap.save_overall_html(
    dest_dir_path='save_overall_html_interface_basic_usage/')
```

The preceding code exports the `save_overall_html_interface_basic_usage/index.html` and the other JavaScript library files.

<iframe src="static/save_overall_html_interface_basic_usage/index.html" width="150" height="150"></iframe>

## Minify the HTML

The `save_overall_html` function has the `minify` optional argument (default is True). This interface minifies an output HTML if this value is `True`\. The `False` setting is sometimes helpful for debugging.

```py
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

ap.save_overall_html(
    dest_dir_path='dest_dir/',
    minify=False)
```

## JavaScript libs directory path setting and skip option

If you want to adjust the JavaScript library paths, set the `js_lib_dir_path` optional argument. This option overrides the JavaScript library paths in an exported HTML (`index.html`).

This setting is sometimes helpful when you want to export the HTML with specified JavaScript library paths, for instance, the Django library static directory.

Also, the `skip_js_lib_exporting` option is helpful when you want to skip the already exported js files. This setting skips the JavaScript library exporting.

```py
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

ap.save_overall_html(
    dest_dir_path='dest_dir/',
    js_lib_dir_path='static/js/',
    skip_js_lib_exporting=True)
```

Notes: The `js_lib_dir_path` option does not change the js files exporting destination directory currently.

## Change the HTML file name by the html_file_name option

If you need to change the output HTML file name, use the `html_file_name` optional argument. This argument changes the HTML file name from `index.html` to any other name.

```py
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

ap.save_overall_html(
    dest_dir_path='dest_dir/',
    html_file_name='chart.html')
```

## Bundle each JavaScript library to the signle HTML file by the embed_js_libs option

You can bundle each JavaScript library to the single output HTML file by the `embed_js_libs` optional argument. This option is maybe useful when you need to pass the output file to the other members.

```py
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

ap.save_overall_html(
    dest_dir_path='dest_dir/',
    embed_js_libs=True)
```

## Change the stdout setting by the verbose option

The `verbose` optional argument changes the exporting stdout behavior. If the specified value is 0, the apysc displays nothing to the stdout will. If 1 or the other values is specified, the apysc displays the stdout.

```py
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

ap.save_overall_html(
    dest_dir_path='dest_dir/',
    verbose=0)
```
