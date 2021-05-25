class Bank_account :
    def __init__(self,name, phone_number):
            self.name=name
            self.balance=0
        
            self.phone_number=phone_number

    def show_balance(self):
            return f"Hello this is my {self.balance}"       
    def deposit(self,amount):
            if amount<=0:
                    return f"you cannot deposit {amount}"
            else:
    
                self.balance+=amount 
            return f"{self.show_balance()}"    
            self.balance-=amount
            return f"self. show_balance()"
    
    def borrow_loan(self,amount):
             return f"congratulation you have borrowed {amount}"
    def repay_loan(self,amount):
             return f"You have  repaid {amount}"


             
    
    