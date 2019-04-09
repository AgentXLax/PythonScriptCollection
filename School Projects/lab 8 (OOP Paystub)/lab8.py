class Employee():
    def __init__(self, lastName,firstName,wage=12.20):
        self.last = lastName
        self.first = firstName
        self.wage = float(wage)
        self.hours = 0 #creates a reference for hours that can be called

    def __repr__(self):
        return 'Employee: ' + self.first + ' ' + self.last

    def __add__(self1, self2):
        return float('{:.2f}'.format(self1.wage + self2.wage))

    def grossPay(self):
        otHours = self.hours - 40
        if self.hours > 40:
            return 40 * self.wage + otHours * self.wage * 2
        else:
            return self.wage * self.hours
    
    def taxDeduction(self):
        taxBracket = self.grossPay() * 52
        if taxBracket > 42000:
            return 0.22 * self.grossPay()
        else:
            return 0.15 * self.grossPay()

    def deductedPay(self):
        return self.grossPay() - self.taxDeduction()

    
    def printBody(self, hours):
        self.hours = float(hours)
        print('-' * 67)
        print()
        print('{:<10}{:<30}{:<10}${:>,.2f}'\
              .format('PAY TO:', self.first + ' ' + self.last,'AMOUNT:',self.deductedPay()))
        print()
        print()
        print('{:<15}${:>,.2f}'\
              .format('Gross Pay:', self.grossPay()))
        print('Deductions:')
        print('{:^10}{:5}${:>,.2f}'\
              .format('Tax', ' ', self.taxDeduction()))
        
    def printCheque(self, hours):
        self.printBody(hours)
        print('-' * 67)

santa = Employee('Claus', 'Santa', 55)
santa.printCheque(40)

class SalariedEmployee(Employee):
    def __init__(self, lastName, firstName, salary=float(25000)):
        super().__init__(lastName,firstName,salary)
        self.salary = float(salary)
        self.wage = salary / 52 / 40
        
    def grossPay(self):
        return self.salary / 52

    def benDeduction(self):
        return self.grossPay() * 0.015

    def deductedPay(self):
        return self.grossPay() - self.taxDeduction() - self.benDeduction()

    def vacationHours(self):
        if self.hours > 45:
            return int(self.hours - 45)
        elif self.hours < 35:
            return int(self.hours - 35)

    def printCheque(self, hours):
        super().printBody(hours)
        print('{:^10}{:5}${:>,.2f}'\
              .format('Benefits',' ',self.benDeduction()))
        print('{:<15}{:>}'\
              .format('Vacation:', str(self.vacationHours()) + ' hours'))
        print('-' * 67)

tf = SalariedEmployee('Fairy', 'Tooth', 67000)
tf.printCheque(60)
santa = SalariedEmployee('Jackson', 'John', )
