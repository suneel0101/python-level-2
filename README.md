# Objectives
Students will be able to
- write reusable functions with ease
- use classes and object-oriented programming to encapsulate their logic
- comfortably use existing Python libraries, like the `csv` library

# New Workflow
1. Get a text editor. [Sublime](http://www.sublimetext.com/) is great.
2. Open Terminal
3. Run `cd ` (This navigates you to the home directory)
4. Run `mkdir Development` (mkdir=make directory, so this creates a new directory called Development, which is on the same level as Desktop and Documents)
5. Run `cd Development` (This navigates within the Development directory)


## Indivual Exercises
1. Create a folder under Development called PythonNinja
2. Create a file called exercise_1.py using the `touch` command, e.g. `touch test.py` will create a folder in the current directory.
3. Open that file in Sublime.


## Together Exercises
Copy and paste the following code into the `exercise_1.py` file and save (Cmd + S)

```python
def say_hello(name):
    print "Hello, " + name + "!"
```

1. Back in the terminal, we should still be under the PythonNinja directory. Check this by typing `pwd` and then Enter to Print Working Directory (pwd)
2. Let's enter the python shell (remember: type `python` and press Enter) 

Then we'll follow these steps: (>>> indicates we're in the Python shell, you don't type these > signs)

```
>>> from exercise_1 import say_hello
>>> say_hello("Cercei")
```

## Individual Exercises
1. What is happening in the `import` line?
2. What is happening in the second line?

## Individual Exercise
1. Go back to exercise_1.py and change the "Hello, " to "Hey, "
2. Go back to the shell and run the `say_hello` call again. Has it updated?
3. Exit the shell using `>>> exit()` and reopen the shell
4. Run the same two lines (the import and the `say_hello` call) and see that it has updated.



