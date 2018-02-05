# brainfuck
brainfuck interpreter written in python

It's actually really slow, for now, unless you're using it just for testing out brainfuck, printing simple strings etc.
I did it quickly just for fun, so if anyone wants to make an improvement on it, I'm accepting pull requests.

##Usage:
```
python brainfuck.py file.bf
<output>
```
or
```
python brainfuck.py
<brainfuck code goes here><ENTER>
<output>
```
Example #1:
```
python brainfuck.py hello_world.bf
Hello, world!
```
Example #2:
```
python brainfuck.py
-[------->+<]>-.-[->+++++<]>++.+++++++..+++.[->+++++<]>+.------------.--[->++++<]>-.--------.+++.------.--------.-[--->+<]>.
Hello, world!
```
