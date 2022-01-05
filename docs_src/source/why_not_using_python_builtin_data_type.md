# Why the apysc library doesn't use the Python built-in data type

This page explains why the apysc library doesn't use the Python built-in data type, such as `int`\, `float`\, `bool`\, `list`\. And why the apysc library uses the apysc data type like the `Int`\, `Number`\, `Array` instead.

## apysc needs to convert Python to JavaScript and track variables change

The apysc library needs to track variable creation and update to convert the Python code to JavaScript. For this reason, apysc using the original data types, such as `Int`\, `Number` (`Float`)\, `String`\, `Boolean`\, `Array`\, and `Dictionary`\.

Occasionally, these are unnecessary to create HTML. Still, these types become essential when you use the asynchronous function, such as the event handler.

The apysc library automatically sets each variable's names and uses them when exporting the HTML and JavaScript files. It also tracks variables creation and updating and applies them to the exported JavaScript.

Using the Python built-in data type, these variables' values become fixed (the apysc doesn't apply asynchronous function's changes).
