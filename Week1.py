# Principles of Computing
# Week1 Quiz

# Question 1:Enter the type of the Python expression 3.14159 below. Remember that capitalization is important.
# -Float

# Question 3:Consider the following Python code snippet:
 def clock_helper(total_seconds):
    """
    Helper function for a clock
    """
    seconds_in_minute = total_seconds % 60
print (clock_helper(90))

# -None

# Question 9: Repeatedly append the sum of the current last three elements of lst to lst
def appendsums(lst):
    new = 0
    for i in range(0,25):
        new = lst[-1] + lst[-2] + lst[-3]
        lst.append(new)

# Question 10:
class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.fee = 0
        
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.dep = amount
        self.balance += self.dep
        
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.withdrw = amount
        
        if (self.balance-self.withdrw) < 0:
            self.balance = self.balance - 5 - self.withdrw
            self.fee += 5
        else:
            self.balance -= self.withdrw
   
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance
        
    def get_fees(self):
        return self.fee

    """Returns the total fees ever deducted from the account.""
