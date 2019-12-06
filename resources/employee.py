class Employee:
    # Create basic Variables
    # Basic income plus benefits/ allowances = Gross
    basic_income = 0
    benefits = 0
    gross_income = 0
    # Gross income less nssf = taxable income
    nssf_contribution = 0
    taxable_income = 0
    # Tax is calculated on taxable income
    # Net tax less personal relief is the tax_payable
    paye_charged = 0
    personal_relief = 1408
    tax_payable = 0
    # Taxable income less tax payable less nhif gives net income
    nhif_contribution = 0
    net_salary = 0

    # The constructor
    def __init__(self, basic_income, benefits):
        self.basic_income = basic_income
        self.benefits = benefits
        self.calculate_gross_income()
        self.calculate_nssf_contribution()
        self.calculate_taxable_income()
        self.calculate_paye_tax()
        self.calculate_tax_payable()
        self.calculate_nhif_contribution()

    # Calculating Gross Income
    def calculate_gross_income(self):
        gross_salary = self.basic_income + self.benefits
        self.gross_income = gross_salary
        return gross_salary

    # Calculating NSSF Contribution
    def calculate_nssf_contribution(self):
        if  0 < self.gross_income <= 6000:
            nssf = 0.06 * self.gross_income
            
        elif 6001 <= self.gross_income <= 18000:
            nssf = self.gross_income - 6000
            
        elif self.gross_income > 18000:
            nssf = 18000 * 0.06
            
        self.nssf_contribution = nssf
        return nssf

    # Calculate taxable income
    def calculate_taxable_income(self):
        taxable_income = self.gross_income - self.nssf_contribution
        self.taxable_income = taxable_income
        return taxable_income

    # Calculate Pay as you earn
    def calculate_paye_tax(self):

        block_1 = 12298
        block_1_tax = 12298 * 0.1

        block_2 = block_1 + 11587
        block_2_tax = block_1_tax + 11587 * 0.15

        block_3 = block_2 + 11587
        block_3_tax = block_2_tax + 11587 * 0.2

        block_4 = block_3 + 11587
        block_4_tax = block_3_tax + 11587 * 0.25

        if self.taxable_income > block_1:
            if self.taxable_income > block_2:
                if self.taxable_income > block_3:
                    if self.taxable_income > block_4:
                        remainder = self.taxable_income - block_4
                        paye = block_4_tax + remainder * 0.3
                    else:
                        remainder = self.taxable_income - block_3
                        paye = block_3_tax + remainder * 0.25
                else:
                    remainder = self.taxable_income - block_2
                    paye = block_2_tax + remainder * 0.2
            else:
                remainder = self.taxable_income - block_1
                paye = block_1_tax + remainder * 0.15
        else:
            paye = self.taxable_income * 0.1

        self.paye_charged = paye
        return paye

    # Calculating tax payable
    def calculate_tax_payable(self):
        tax_payable = self.taxable_income - self.personal_relief
        self.tax_payable = tax_payable
        return tax_payable
    
    # Calculating nhif contribution on gross salary
    def calculate_nhif_contribution(self):
        if self.gross_income >= 6000:
            if self.gross_income >= 8000:
                if self.gross_income >= 12000:
                    if self.gross_income >= 15000:
                        if self.gross_income >= 20000:
                            if self.gross_income >= 25000:
                                if self.gross_income >= 30000:
                                    if self.gross_income >= 35000:
                                        if self.gross_income >= 40000:
                                            if self.gross_income >= 45000:
                                                if self.gross_income >= 50000:
                                                    if self.gross_income>= 60000:
                                                        if self.gross_income >= 70000:
                                                            if self.gross_income >= 80000:
                                                                if self.gross_income >= 90000:
                                                                    if self.gross_income >= 100000:
                                                                        nhif = 1700
                                                                    else:
                                                                        nhif = 1600
                                                                else:
                                                                    nhif = 1500
                                                            else:
                                                                nhif = 1400
                                                        else:
                                                            nhif =1300
                                                    else: 
                                                        nhif = 1200
                                                else:
                                                    nhif = 1100
                                            else:
                                                nhif = 1000
                                        else:
                                            nhif = 950
                                    else:
                                        nhif = 900
                                else:
                                    nhif = 850
                            else:
                                nhif = 750
                        else:
                            nhif = 600
                    else:
                        nhif = 500
                else:
                    nhif = 400
            else:
                nhif = 300
        else:
            nhif = 150

        self.nhif_contribution = nhif
        return nhif

    # Calculating net pay
    def calculate_net_pay(self):
        net_pay = self.taxable_income - self.paye_charged + self.personal_relief - self.nhif_contribution
        self.net_salary = net_pay
        return net_pay

emp1 = Employee(15000,  0 )
print('Gross Pay',emp1.gross_income)
print('NSSF',emp1.nssf_contribution)
print('NHIF',emp1.nhif_contribution)
print('Taxable income (net pay)',emp1.taxable_income)
print('tax charged',emp1.paye_charged)





    

        
