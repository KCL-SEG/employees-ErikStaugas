class Employee:
    def __init__(self, name, perPayAmount):
        self.name = name
        self.perPayAmount = perPayAmount

    def getRegularPay(self):
        return self.perPayAmount

    def get_pay(self):
        return self.getRegularPay()
    
    def __str__(self):
        return self.name

    def getBonusComm(self, bonusAmount):
        return bonusAmount
    
    def getContractComm(self, contractCommissionAmount, contractNumber):
        return contractCommissionAmount * contractNumber
    

class SalaryEmployee(Employee):
    def __init__(self, name, perPayAmount):
        super().__init__(name, perPayAmount)
   
    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.perPayAmount}.  Their total pay is {self.get_pay()}."

class SalaryBonusEmployee(SalaryEmployee):
    def __init__(self, name, perPayAmount, bonusAmount):
        super().__init__(name, perPayAmount)
        self.bonusAmount = bonusAmount

    def get_pay(self):
        return super().getRegularPay() + super().getBonusComm(self.bonusAmount)
        
    def __str__(self):
        return f"{self.name} works on a monthly salary of {str(self.perPayAmount)} and receives a bonus commission of {str(self.bonusAmount)}.  Their total pay is {self.get_pay()}."

class SalaryContractEmployee(SalaryEmployee):
    def __init__(self, name, perPayAmount, contractCommissionAmount, contractNumber):
        super().__init__(name, perPayAmount)
        self.contractCommissionAmount = contractCommissionAmount
        self.contractNumber = contractNumber

    def get_pay(self):
        return super().getRegularPay() + super().getContractComm(self.contractCommissionAmount, self.contractNumber)

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.perPayAmount} and receives a commission for {self.contractNumber} contract(s) at {self.contractCommissionAmount}/contract.  Their total pay is {self.get_pay()}."

class HourlyEmployee(Employee):
    def __init__(self, name, perPayAmount, hour):
        super().__init__(name, perPayAmount)
        self.hour = hour

    def getRegularPay(self):
        return self.perPayAmount * self.hour

    def get_pay(self):
        return super().getRegularPay() * self.hour

    def __str__(self):
        return f"{self.name} works on a contract of {self.hour} hours at {self.perPayAmount}/hour.  Their total pay is {self.get_pay()}."


class HourlyBonusEmployee(HourlyEmployee):
    def __init__(self, name, perPayAmount, hour, bonusAmount):
        super().__init__(name, perPayAmount, hour)
        self.bonusAmount = bonusAmount

    def get_pay(self):
        return super().getRegularPay() + self.bonusAmount

    def __str__(self):
        return f"{self.name} works on a contract of {self.hour} hours at {self.perPayAmount}/hour and receives a bonus commission of {self.bonusAmount}.  Their total pay is {self.get_pay()}."


class HourlyContractEmployee(HourlyEmployee):
    def __init__(self, name, perPayAmount, hour, contractCommissionAmount, contractNumber):
        super().__init__(name, perPayAmount, hour)
        self.contractCommissionAmount = contractCommissionAmount
        self.contractNumber = contractNumber

    def get_pay(self):
        return super().getRegularPay() + super().getContractComm(self.contractCommissionAmount, self.contractNumber)

    def __str__(self):
        return f"{self.name} works on a contract of {self.hour} hours at {self.perPayAmount}/hour and receives a commission for {self.contractNumber} contract(s) at {self.contractCommissionAmount}/contract.  Their total pay is {self.get_pay()}."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryContractEmployee('Renee', 3000, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyContractEmployee('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryBonusEmployee('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyBonusEmployee('Ariel', 30, 120, 600)