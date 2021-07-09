# save_overall_html interface

This page will explain the `save_overall_html` function interface.

## What interface is this?

The `save_overall_html` function interface will export the overall HTML and JavaScript files. This function's calling is necessary at the end of the apysc project to export the HTML.

## Basic usage

The `save_overall_html` function need at least one argument, `dest_dir_path`. This argument will determine a directory path to save HTML and JavaScript files.

The following code example will export the HTML and JavaScript files, and the blank stage (150 px width and height) will be displayed on the HTML.

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

The preceding code will export the `save_overall_html_interface_basic_usage/index.html` and the other JavaScript library files.

<iframe src="static/save_overall_html_interface_basic_usage/index.html" width="150" height="150"></iframe>

## Minify the HTML

The `save_overall_html` function has the `minify` optional argument (default is True). If this value is True an output HTML (`index.html`) will be minified. The `False` setting will be useful for the debug.

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

If you want to adjust the JavaScript library paths, then set the `js_lib_dir_path` optional argument. This option will override the JavaScript library paths in an exported HTML (`index.html`).

This is sometimes useful when you want to export the HTML with specified JavaScript library paths, for instance, the Django library static directory.

Also, the `skip_js_lib_exporting` option will maybe be useful when you want to skip the already exported js files.

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

Notes: The `js_lib_dir_path` option will not change the js files exporting destination directory currently.

## Change the HTML file name by the html_file_name option

If you need to change the output HTML file name, then use the `html_file_name` optional argument. This argument will change the HTML file name from `index.html` to any other name.

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

You can bundle each JavaScript library to the single output HTML file by the `embed_js_libs` optional argument. This option will maybe be useful when you need to pass the output file to the other members.

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

The `verbose` optional argument will change the exporting stdout behavior. If 0 is specified to this option, the stdout will not be displayed. If 1 or the other values is specified, the stdout will be displayed.

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
