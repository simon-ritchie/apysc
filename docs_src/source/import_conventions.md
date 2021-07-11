# Import conventions

In the `apysc` library, it is recommended to use the `import apysc as ap` to import the package, like the `import numpy as np`, `import pandas as pd`, `import tkinter as tk`, or something like that.

All interfaces that you need are packaged in the `apysc` package (for instance, `Sprite`, `Int`, `Stage`).

The `apysc` internal logic packages are named with the underscore prefix like the `_file`. These packages are not necessary.

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
number_1: ap.Number = int_1 + ap.Number(10.5)
```
