# display_on_colaboratory interface

This page will explain the `display_on_colaboratory` function interface.

## What interface is this?

The `display_on_colaboratory` interface displays the apysc HTML on the Google Colaboratory.

## Requirements

You need to install apysc on the Google Colaboratory before going on. A `!` symbol and pip command on the Google Colaboratory installs this library:

```
!pip install apysc
```

## Basic usage

You can use the `display_on_colaboratory` interface to display an output HTML instead of the `save_overall_html` function.

This interface requires the `html_file_name` argument to be unique if you need to output multiple HTML. Otherwise, it overwrites the HTML file:

```py
import apysc as ap

ap.Stage(
    stage_width=250, stage_height=150, background_color='#333')
sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

sprite.graphics.begin_fill(color='#f0a')
sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)

ap.display_on_colaboratory(html_file_name='jupyter_test_1.html')
```

![](_static/colaboratory_interface.png)

## display_on_colaboratory API

<!-- Docstring: apysc._jupyter.jupyter_util.display_on_colaboratory -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `display_on_colaboratory(html_file_name:str, *, minify:bool=True) -> None`<hr>

**[Interface summary]** Save the overall HTML and display it on Google Colaboratory.<hr>

**[Parameters]**

- `html_file_name`: str, default 'index.html'
  - The output HTML file name.
- `minify`: bool, default True
  - Boolean value whether minify a HTML or not. False setting is useful when debugging.