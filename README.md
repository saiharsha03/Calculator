# Calculator

A small desktop calculator built with Python and Tkinter.

Enter two numbers, then click a button for add, subtract, multiply, divide or modulo. The result appears under the buttons, for example `The result of 8.0 / 2.0 is 4.0`.

## Files

- `Calculator_GUI.py`: the window and button handling
- `add.py`, `sub.py`, `mul.py`, `div.py`, `mod.py`: one function per operation

## Run it

```bash
python Calculator_GUI.py
```

Tkinter ships with Python, so there is nothing to install.

## Known limits

Inputs are read as floats, and there is no error handling. Dividing by zero, or entering something that is not a number, raises an exception in the console instead of showing a message.
