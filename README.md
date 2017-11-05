# StackSmasher
A Python script to figure out the length of input before you could overwrite the return address. It relies on the fact that the successfully executed program returns a 0.

Prerequisite:
-------------
Python3

Options Available:
------------------

* --start

The length of input to begin stack smashing with. It's an integer value and by default it's value is 5.
 
* --start

Value by which the length of input should be incremented with each successive loop. It's an integer value and by default it's value is 5.

* --start

The length of input upto which the stack smashing should be tested. The program will stop smashing if the executable crashes before this value is reached. It's an integer value and by default it's value is 10000.



Usage:
------

```
python3 BOF.py --start 10 --step 1 --end 1000 ./talisman
```
