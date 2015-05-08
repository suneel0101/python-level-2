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


## Individual Exercises (Set 1)
1. Create a folder under Development called PythonNinja
2. Create a file called exercise_1.py using the `touch` command, e.g. `touch test.py` will create a folder in the current directory.
3. Open that file in Sublime.


## Together Exercises
Copy and paste the following code into the `exercise_1.py` file and save (Cmd + S)

```python
def say_hello(name):
    """
    This function takes a name (string) and prints
    a personalized greeting.
    """
    print "Hello, " + name + "!"
```

1. Back in the terminal, we should still be under the PythonNinja directory. Check this by typing `pwd` and then Enter to Print Working Directory (pwd)
2. Let's enter the python shell (remember: type `python` and press Enter) 

Then we'll follow these steps: (>>> indicates we're in the Python shell, you don't type these > signs)

```
>>> from exercise_1 import say_hello
>>> say_hello("Cercei")
```

## Individual Exercises (Set 2)
1. What is happening in the `import` line?
2. What is happening in the second line?

## Individual Exercise (Set 3)
1. Go back to exercise_1.py and change the "Hello, " to "Hey, "
2. Go back to the shell and run the `say_hello` call again. Has it updated?
3. Exit the shell using `>>> exit()` and reopen the shell
4. Run the same two lines (the import and the `say_hello` call) and see that it has updated.


# Let's Up Our Function-Writing Skills

These exercises will help us write clean, modular functions.

## Individual Exercises (Set 4)
*Objective*: Review the syntax of a function.

1. Create a new file under PythonNinja called even_utils.py
2. In function_practice.py, write a function called `is_even` which will take an integer and return True if it's even, False otherwise.
3. Open the python shell and import `is_even`. Test the function on these values: 3, -2, 0, 2000. Did it work as expected?

## Code Review Workflow
1. Sign into this hipchat url: https://www.hipchat.com/geDHwPme2
2. Go to gist.github.com
3. Paste your code for `is_even` into the text body area
4. Click `Create secret gist`
5. Copy the browser url
6. Paste it into the chat

## Partner Exercises (Set 5)
*Objective*: Combine the use of functions; practice loops; use import statements.

1. Under PythonNinja, create a new file called function_practice.py
2. In this file, write a function called `filter_out_odds` which takes one argument, called `numbers`. (Remember our for loops from the intro class). This function will return a sublist of the original `numbers` list containing only those numbers which are even. `filter_out_odds` should make use of the `is_even` function, *HINT*: You'll have to import `is_even` from `even_utils.py`. 
3. Open the python shell, import `filter_out_odds` and test the function on these inputs: `[1, 3, 6, 8, -20]` and then on `range(2, 350)`. Did it work?

# A Bit More on Import Statements

Open the python shell from under PythonNinja.

Then, type the following:
```
>>> import function_practice
>>> nums = range(30)
>>> function_practice.filter_out_odds(nums)
```

Now exit the shell and reopen the shell.

Then, type the following:
```
>>> from function_practice import filter_out_odds
>>> filter_out_odds([1, 3, 2, 8])
```

## Partner Exercise (Set 6)
1. Turn to a partner and explain what is happening in these two different import examples.

# Let's Learn How to Use Existing Libraries
Code libraries are directories of code that other developers have written and made accessible to us. Some of these libraries are built into Python and others we have to install.

We will now deal with ths `csv` library, which is a super useful built-in library.

## Documentation Exercise (Set 7)
Documentation is your friend. You'll often need to Google and look up the functions that are available to you, their syntax, etc, so let's cultivate that skill.

1. Open your web browser
2. Google "csv python"
3. The first result should be the official docs. Click on it.


