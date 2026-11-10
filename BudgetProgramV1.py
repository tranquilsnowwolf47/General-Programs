class Budget:
    def __init__(self, hours_worked, PAY_PER_HOUR, tax_percent, gross_pay):
        self._hours_worked = hours_worked
        self._PAY_PER_HOUR = PAY_PER_HOUR
        self._tax_percent = tax_percent
        self._gross_pay = gross_pay
        
    def calculate_gross_pay(self):
        if self._hours_worked > 0 and self._PAY_PER_HOUR == 19:
            self._gross_pay = self._hours_worked * self._PAY_PER_HOUR
        else: 
            print("Error.")
    
    def get_gross_pay(self):
        return self._gross_pay
    
    
    def calculate_net_pay:
        if self._hours_worked > 0 and self._PAY_PER_HOUR == 19:
            gross_pay = self._
        else:
            print("Error")
