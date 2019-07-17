<h3>Concurrency

source: Python Essential Reference: David M. Beazley

Process([group [, target [, name [, args [, kwargs]]]]])
A class that represents a task running in a subprocess. The arguments in the constructor should always be specified using keyword arguments. *target* is a callable object that will execute when the process starts, *args* is a tuple of positional arguments passed to *target*, and *kwargs* is a dictionary of keyword arguments passed to *target*. If *args* and *kwargs* are omitted, *target* is called with no arguments. *name* is a string that gives a descriptive name to the process. *group* is unused and always set to *None*. Its presence is to make the construction of  a *Process* mimic the creation of a thread in the *threading* module.
