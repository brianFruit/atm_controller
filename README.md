# ATM Controller

### DISCLAIMER
Python is not the ideal language for this system because their variables can't be made private, but I added underscores before variables to denote them being private. I chose Python mainly because it can prototype and test the architecture very quickly. After ensuring all the logic works, it can be easily ported into a more appropriate languages like C/C++.

Error handlings in the current implementation are quite minimal. There are various places that require some exceptions to be raised. Since a detail specifications were not provided, I skipped them to avoid complexity.

### Dependency
Python 3.7+

### Running the Code
 The Card, Account, CashBin, and ATMManager classes can be imported into other python scripts for use, but I also included some assertion tests in the main script (after line 114) to demonstrate how the implementation works. To run it, simply type the command in the shell `python atm_controller.py`.

