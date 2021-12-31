# display_on_colaboratory interface

This page will explain the `display_on_colaboratory` function interface.

## What interface is this?

The `display_on_colaboratory` interface will display the apysc HTML on the Google Colaboratory.

## Requirements

You need to install apysc on the Google Colaboratory before going on.  A `!` symbol and pip command on the Google Colaboratory will install this library:

```
!pip install apysc
```

## Basic usage

You can use the `display_on_colaboratory` interface to display an output HTML instead of the `save_overall_html` function.

The `html_file_name` argument is required to be unique if you need to output multiple HTML otherwise the HTML file will be overwritten:

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
