# Import conventions

The apysc library recommends using the `import apysc as ap` to import the package, like the `import numpy as np`\, `import pandas as pd`\, `import tkinter as tk`\, or something like that.

The root package module packages all interfaces you need (for instance, `Sprite`\, `Int`\, `Stage`).

Also, it packages internal logic modules with the underscore prefix like the `_file`\. These packages are not necessary for you.

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
number_1: ap.Number = int_1 + ap.Number(10.5)
```