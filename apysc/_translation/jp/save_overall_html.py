"""This module is for the translation mapping data of the
following document:

Document file: save_overall_html.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# save_overall_html interface':
    '',

    'This page explains the `save_overall_html` function interface.':
    '',

    '## What interface is this?':
    '',

    'The `save_overall_html` function interface will export the overall HTML and JavaScript files. At the end of the apysc project, this function\'s calling is necessary to export the HTML.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `save_overall_html` function need at least one argument, `dest_dir_path`. This argument determines a directory path to save HTML and JavaScript files.\n\nThe following code example exports the HTML and JavaScript files, and the exported HTML displays the blank stage (150 px width and height).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nap.save_overall_html(\n    dest_dir_path=\'save_overall_html_interface_basic_usage/\')\n```':  # noqa
    '',

    'The preceding code exports the `save_overall_html_interface_basic_usage/index.html` and the other JavaScript library files.\n\n<iframe src="static/save_overall_html_interface_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## Minify the HTML':
    '',

    'The `save_overall_html` function has the `minify` optional argument (default is True). This interface minifies an output HTML if this value is `True`\\. The `False` setting is sometimes helpful for debugging.':  # noqa
    '',

    '```py\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nap.save_overall_html(\n    dest_dir_path=\'dest_dir/\',\n    minify=False)\n```':  # noqa
    '',

    '':
    '',

    '## JavaScript libs directory path setting and skip option':
    '',

    'If you want to adjust the JavaScript library paths, set the `js_lib_dir_path` optional argument. This option overrides the JavaScript library paths in an exported HTML (`index.html`).\n\nThis setting is sometimes helpful when you want to export the HTML with specified JavaScript library paths, for instance, the Django library static directory.\n\nAlso, the `skip_js_lib_exporting` option is helpful when you want to skip the already exported js files. This setting skips the JavaScript library exporting.':  # noqa
    '',

    '```py\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nap.save_overall_html(\n    dest_dir_path=\'dest_dir/\',\n    js_lib_dir_path=\'static/js/\',\n    skip_js_lib_exporting=True)\n```':  # noqa
    '',

    'Notes: The `js_lib_dir_path` option does not change the js files exporting destination directory currently.':  # noqa
    '',

    '## Change the HTML file name by the html_file_name option':
    '',

    'If you need to change the output HTML file name, use the `html_file_name` optional argument. This argument changes the HTML file name from `index.html` to any other name.':  # noqa
    '',

    '```py\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nap.save_overall_html(\n    dest_dir_path=\'dest_dir/\',\n    html_file_name=\'chart.html\')\n```':  # noqa
    '',

    '':
    '',

    '## Bundle each JavaScript library to the signle HTML file by the embed_js_libs option':  # noqa
    '',

    'You can bundle each JavaScript library to the single output HTML file by the `embed_js_libs` optional argument. This option is maybe useful when you need to pass the output file to the other members.':  # noqa
    '',

    '```py\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nap.save_overall_html(\n    dest_dir_path=\'dest_dir/\',\n    embed_js_libs=True)\n```':  # noqa
    '',

    '':
    '',

    '## Change the stdout setting by the verbose option':
    '',

    'The `verbose` optional argument changes the exporting stdout behavior. If the specified value is 0, the apysc displays nothing to the stdout will. If 1 or the other values is specified, the apysc displays the stdout.':  # noqa
    '',

    '```py\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nap.save_overall_html(\n    dest_dir_path=\'dest_dir/\',\n    verbose=0)\n```':  # noqa
    '',

    '':
    '',

    '## save_overall_html API':
    '',

    '<!-- Docstring: apysc._html.exporter.save_overall_html -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `save_overall_html(dest_dir_path:str, *, html_file_name:str=\'index.html\', minify:bool=True, js_lib_dir_path:str=\'./\', skip_js_lib_exporting:bool=False, embed_js_libs:bool=False, verbose:int=1) -> None`<hr>\n\n**[Interface summary]** Save the overall HTML and js files under the specified directory path.<hr>\n\n**[Parameters]**\n\n- `dest_dir_path`: str\n  - Destination directory path to save each HTML and js file.\n- `html_file_name`: str, default \'index.html\'\n  - The output HTML file name.\n- `minify`: bool, default True\n  - Boolean value indicates whether minify HTML and js or not. The False setting is helpful when debugging.\n- `js_lib_dir_path`: str, default \'./\'\n  - JavaScript libraries directory path. This setting applies to a JavaScript source path in HTML. If not specified, then set the same directory with HTML. This setting is maybe helpful to set js lib directory, such as Django\'s static (static_collected) directory. This interface recommends setting True value to the `skip_js_lib_exporting` argument if this argument sets.\n- `skip_js_lib_exporting`: bool, default False\n  - If True, this interface does not export JavaScript libraries.\n- `embed_js_libs`: bool, default False\n  - Option to embed the JavaScript libraries script to the output HTML or not. If True, the output HTML becomes enormous, and be only one HTML file. Occasionally, this option is useful when sharing the exported file or using the output file with an iframe tag to avoid the CORS error.\n- `verbose`: int, default 1\n  - The Logging setting. If 0 is specified, this interface does not display a logging message. If 1 or the other value is specified, this interface displays a message usually.\n\n<hr>\n\n**[Notes]**\n\nThis interface empties a specified directory before saving.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> # Do something here...\n>>> ap.save_overall_html(dest_dir_path=\'tmp/output/\')\n```':  # noqa
    '',

}
