# spreetail_dictionary_app
Finished project found in spreetail_dictionary_app.py file

	1. Project title: Spreetail Dictionary Console App: Python functions
	
    2. Project description:
        A code challenge to create an app in chosen language that follows the given sequence of Console returns for 10 different functionalities. 

	3. How to install and run the project: 
        the project should run on any IDE that has a terminal. I built/tested it using BASH terminal.
        
    4. how to use the project: 
        run the program in a console/terminal and use these commands: 
        KEYS - returns all keys
        MEMBERS key - returns all values for the key 
        ADD key value (two words needed)- add a value for a key 
        REMOVE key value (two words needed)- deletes a value for a key  
        REMOVEALL key - deletes all values of a key, in turn, deleting the key
        CLEAR - clears all keys and their values  
        KEYEXISTS key - returns True/False for a key
        MEMBEREXISTS key value - returns true/false of a value for a key
        ALLMEMBERS - returns a list of ALL members
        ITEMS - returns a list of ALL key:value pairs

Licenses: None



---------------------------------------------------------------------------
WORK SAMPLE

The Multi-Value Dictionary app is a command line application that stores a multivalue dictionary in memory. 
All keys and values(as lists) are strings.

    a.  check thoroughly for bugs. If there is one bug, they will fail you.
 
    b.  When you are finished double-check for bugs. 
        When everything is complete send the work sample to everyone on the email invite. 




It should support the following commands.


### KEYS 1 + 4
1Add key + value. 
2Returns all the keys in the dictionary.  Order is not guaranteed.
Example
```
> ADD foo bar
) Added
> ADD baz bang
) Added
> KEYS
1) foo
2) baz
```
### MEMBERS 3
Returns the collection of strings for the given key.  Return order is not guaranteed.  Returns an error if the key does not exists.
Example:
```
> ADD foo bar
> ADD foo baz
> MEMBERS foo
1) bar
2) baz
> MEMBERS bad
) ERROR, key does not exist.
```
### ADD 1 + 4
Adds a member to a collection for a given key. Displays an error if the member already exists for the key.
```
> ADD foo bar
) Added
> ADD foo baz
) Added
> ADD foo bar
) ERROR, member already exists for key
```
### REMOVE 5
Removes a member from a key.  If the last member is removed from the key, the key is removed from the dictionary. If the key or member does not exist, displays an error.
Example:
```
> ADD foo bar
) Added
> ADD foo baz
) Added
> REMOVE foo bar
) Removed
> REMOVE foo bar
) ERROR, member does not exist
> KEYS
1) foo
> REMOVE foo baz
) Removed
> KEYS
) empty set
> REMOVE boom pow
) ERROR, key does not exist
```
### REMOVEALL 6
Removes all members for a key and removes the key from the dictionary. Returns an error if the key does not exist.
Example:
```
> ADD foo bar
) Added
> ADD foo baz
) Added
> KEYS
1) foo
> REMOVEALL foo
) Removed
> KEYS
(empty set)
REMOVEALL foo
) ERROR, key does not exist
```
### CLEAR 7
Removes all keys and all members from the dictionary.
Example:
```
> ADD foo bar
) Added
> ADD bang zip
) Added
> KEYS
1) foo
2) bang
> CLEAR
) Cleared
> KEYS
(empty set)
> CLEAR
) Cleared
> KEYS
(empty set)
```
### KEYEXISTS ??????????????
Returns whether a key exists or not.
Example:
```
> KEYEXISTS foo
) false
> ADD foo bar
) Added
> KEYEXISTS foo
) true
```
### MEMBEREXISTS 8
Returns whether a member exists within a key.  Returns false if the key does not exist.
Example:
```
> MEMBEREXISTS foo bar
) false
> ADD foo bar
) Added
> MEMBEREXISTS foo bar
) true
> MEMBEREXISTS foo baz
) false
```
### ALLMEMBERS 9
Returns all the members in the dictionary.  Returns nothing if there are none. Order is not guaranteed.
Example:
```
> ALLMEMBERS
(empty set)
> ADD foo bar
) Added
> ADD foo baz
) Added
> ALLMEMBERS
1) bar
2) baz
> ADD bang bar
) Added
> ADD bang baz
> ALLMEMBERS
1) bar
2) baz
3) bar
4) baz
```
### ITEMS 10
Returns all keys in the dictionary and all of their members.  Returns nothing if there are none.  Order is not guaranteed.
Example:
```
> ITEMS
(empty set)
> ADD foo bar
) Added
> ADD foo baz
) Added
> ITEMS
1) foo: bar
2) foo: baz
> ADD bang bar
) Added
> ADD bang baz
> ITEMS
1) foo: bar
2) foo: baz
3) bang: bar
4) bang: baz
```

-------------------



