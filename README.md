# AirBnB_clone


## Concept

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Step 1: Write a command interpreter to manage your AirBnB objects

 * To implement the parent class "BaseModel".
 * To create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
 * To create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
 * To create the first abstracted storage engine of the project: File storage
 * To create all unittests to validate all our classes and storage engine
 

### What’s a command interpreter?

 * Create a new object (ex: a new User or a new Place)
 * Retrieve an object from a file, a database etc…
 * Do operations on objects (count, compute stats, etc…)
 * Update attributes of an object
 * Destroy an object

### __Resources__

* Python abstract classes
* cmd module
* Packages concept page
* uuid module
* datetime
* unittest module
* args/kwargs
* Python test cheatsheet

### __General__

* __How to create a Python package ?__

First, we create a directory and give it a package name, preferably related to its operation. Then we put the classes and the required functions in it. Finally we create an `__init__.py` file inside the directory, to let Python know that the directory is a package.

* __How to create a command interpreter in Python using the `cmd` module ?__

* __What is Unit testing and how to implement it in a large project ?__

* __How to serialize and deserialize a Class ?__

* __How to write and read a JSON file ?__

* __How to manage `datetime` ?__

* __What is an `UUID` ?__

* __What is `*args` and how to use it ?__

* __What is `**kwargs` and how to use it ?__

* __How to handle named arguments in a function ?__


## Requirements
### Python Scripts
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
* All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
* All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start by test_
* Your file organization in the tests folder should be the same as your project
* e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
* e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
* All your tests should be executed by using this command: `python3 -m unittest discover tests`
* You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
* All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
* All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
* All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Execution

Your shell should work like this in interactive mode: :

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C) :

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash


### Console : the command interpreter

| COMMAND                                                |                 DESCRIPTION                  |
|--------------------------------------------------------|----------------------------------------------|
| quit                                                   | To exit the console                          |
| EOF                                                    | To exit the console by EOF                   |
| help                                                   | Display the help documentation.              |
| create + class name                                        | Creates an object and print the ID           |
| show + class name + id                                      | To show the informations of the object       |
| destroy + class name + id                                   | To delete an object                          |
| all + class name                                            | To show all the instances of a class         |
| update + class name + id + attribute name + attribute value | To update the attribute of a class         |

 
## :couple: About us ##
This is the first group project in Holberton Paris School in the 26 June 2022!!<br>
If you have a question or a comment, please contact us.<br>
Lucile DELEFORGE (4316@holbertonschool.com)<br>
Juliette MESNILE (2550@holbertonschool.com)<br>
Hiromi VARNIER (4336@holbertonschool.com)<br>


 
