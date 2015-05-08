# Objectives
Students will be able to
- write reusable functions with ease
- use classes and object-oriented programming to encapsulate their logic
- comfortably use existing Python libraries, like the `csv` library

# New Workflow

*15 minutes*

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

*15 minutes*

Type (NOT copy and paste) the following code into the `exercise_1.py` file and save (Cmd + S)

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
**Objective**: Review the syntax of a function.

*15 minutes*

1. Create a new file under PythonNinja called even_utils.py
2. In function_practice.py, write a function called `is_even` which will take an integer and return True if it's even, False otherwise.
3. Open the python shell and import `is_even`. Test the function on these values: 3, -2, 0, 2000. Did it work as expected?

## Code Review Workflow

*7 minutes*

1. Sign into this hipchat url: https://www.hipchat.com/geDHwPme2
2. Go to gist.github.com
3. Paste your code for `is_even` into the text body area
4. Click `Create secret gist`
5. Copy the browser url
6. Paste it into the chat

## Partner Exercises (Set 5)
**Objective**: Combine the use of functions; practice loops; use import statements.

*15 minutes*

1. Under PythonNinja, create a new file called function_practice.py
2. In this file, write a function called `filter_out_odds` which takes one argument, called `numbers`. (Remember our for loops from the intro class). This function will return a sublist of the original `numbers` list containing only those numbers which are even. `filter_out_odds` should make use of the `is_even` function, *HINT*: You'll have to import `is_even` from `even_utils.py`. 
3. Open the python shell, import `filter_out_odds` and test the function on these inputs: `[1, 3, 6, 8, -20]` and then on `range(2, 350)`. Did it work?

# A Bit More on Import Statements

*10 minutes*

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

Now just for good measure, exit and reopen the shell.

Then, type the following:
```
>>> filter_out_odds([1, 2, 4])
```

What happens?

## Partner Exercise (Set 6)
1. Turn to a partner and explain what is happening in these two different import examples.

# Let's Learn How to Read/Write Files

*15 minutes*

## The `with` statement
Useful when you have a pair of operations you want to execute, one at the beginning and one at the end and in between you want to run some code.

The classic example is this:

1. Open a file
2. Do stuff with the contents of that file
3. Close the file

## Code example
```python
# The 'wb' is the mode that we're opening the file in. w=write, b=binary (encoding).
# The 'rb' mode is read-binary
with open('data.txt', 'wb') as f:
    f.write('Hey friends!')
```
Let's open that file in Sublime. It should be under PythonNinja.

Here is the same code, without the use of `with`.

```python
f = open('data.txt', 'wb')
f.write('Hey friends!')
f.close()
```
Usually leaving out `.close()` won't result in a problem, but there are weird edgecases depending on your system where it result in some issues, so if we know that we're always going to call the `close()` method, then we might as well use `with`.

## Individual Exercises (Set 7)
1. Write the numbers 1 thru 1000 to a file called `numbers.txt`

# Let's Learn How to Use Existing Libraries
Code libraries are directories of code that other developers have written and made accessible to us. Some of these libraries are built into Python and others we have to install.

We will now deal with ths `csv` library, which is a super useful built-in library.

## Documentation Exercise (Set 8)

*10 minutes*

Documentation is your friend. You'll often need to Google and look up the functions that are available to you, their syntax, etc, so let's cultivate that skill.

1. Open your web browser
2. Google "csv python"
3. The first result should be the official docs. Click on it.
4. With a partner, read through the documentation and example for `csv.reader` and `csv.writer`. What do they do?

## Together Exercise (Set 9)

*10 minutes*

**Objective**: Learn how to write files using the `csv` library; learn how to run python scripts from the terminal.

1. Create a new file called `create_movies_csv.py` 
2. Type (DON'T COPY PASTE!) the code below.
3. In the terminal under PythonNinja, run `python create_movies_csv.py`
4. What datatype does the `.writerow` method take?

```python
import csv

with open('movies.csv', 'wb') as csvfile:
    movie_writer = csv.writer(csvfile)
    # Write the headers to the file
    headers = ['Name', "IMDB', 'ReleaseYear']
    movie_writer.writerow(headers)
    # Write two rows of movies
    movie_writer.writerow(["Top Gun", 6.8, 1986])
    movie_writer.writerow(["The Usual Suspects", 8.7, 1995])
```

## Individual Exercises (Set 10)

*12 minutes*

1. Create a new file called `create_songs_csv.py` 
2. It should create a csv file called `songs.csv`
3. This file should contain five rows, the first being its header, with colum names `Title`, `Artist`
4. The other four rows should be the following four records
5. Run `python create_songs_csv.py` from the Terminal and open the `songs.csv` file to verify it worked.

``` 
Blank Space, Taylor Swift
Young and Beautiful, Lana del Ray
Anaconda, Nicki Minaj
0 to 100, Drake
```

## Together Exercise (Set 11)

*15 minutes*

**Objective**: Learn how to read files using the `csv` library. 

0. Download [this csv file of movie data](https://s3.amazonaws.com/python-level-2/film.csv) and move it under the PythonNinja directory.
0. Open this file in Sublime to see what it looks like.
1. When you type `ls` into the Terminal under PythonNinja, you should see `film.csv`
1. Create a new file called `movie_reader.py`
2. Type the code below and save the file. 

Code:
```
import csv

def read_movies():
    with open('film.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=';')
        rows = [row for row in reader]
    # Question: why am I splitting the 0th row from the rest?
   return rows[0], rows[1:] 
```

In the Python shell:
```
>>> from movie_reader import read_movies
>>> headers, movies = read_movies()
>>> len(movies)
>>> movies[0]
>>> headers
```

## Individual Exercises (Set 12)

*15 minutes*

1. In `movie_reader.py`, write another function that takes one argument `movies`, which will be a list of rows from the csv file. This function should be called `get_short_movies` and should return a subset of movies that have duration less than 120 minutes
2. Test that it works by running the following in the shell 

```
>>> from movie_reader import read_movies, get_short_movies
>>> headers, movies = read_movies()
>>> short_movies = get_short_movies(movies)
>>> len(short_movies)
>>> short_movies[:3]
```

# Let's Learn to Use the `random` Library!
**Objective**: Test your ability to learn from documentation.

## Individual Exercises (Set 13)
1. Google "python random"
2. Check out the official documentation
3. Use the `random.choice` function to randomly choose an element of the below list.

```
movies = [("The Usual Suspects", 111), ("Never Say Never, 142), ("The Matrix", 181)]
```

# Back to Our Movie Data

## Partner Exercises (Set 14)

*10 minutes*

1. Use your knowledge of the random library and write a function called `recommend_from` that takes a list of rows and randomly choose one from the list.
2. Confirm that it works by running the following in the shell:

```
>>> from movie_reader import read_movies, get_short_movies, recommend_from
>>> headers, movies = read_movies()
>>> short_movies = get_short_movies(movies)
>>> recommend_from(short_movies)
```

