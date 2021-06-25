# Why not using the Python built-in data type in the apysc library?

This page will explain why the apysc library is not using the Python built-in data type, such as `int`, `float`, `bool`, `list`, and using the apysc data type like the `Int`, `Number`, `Array`.

## apysc needs to convert Python to JavaScript and track variables change

To convert Python codes written with the apysc library, apysc needs to track variables creation and changing. For this reason, apysc using the original data types, such as `Int`, `Number`, `String`, `Boolean`, `Array`, and `Dictionary`.

Occasionally, these are not necessary to create HTML, but these types will be important when you use the asynchronous function, such as the event handler.

The apysc library will set the names to each variable automatically and use it when exporting the HTML and JavaScript files. This one will also track variables creation and change, and apply them to the exported JavaScript.

If you use the Python built-in data type, these variables' change will not be applied to an exported result.
