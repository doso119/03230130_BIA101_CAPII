# personal income tax calculation

class TaxCalculator: # Initialize the TaxCalculator object with the provided parameters.
    def __init__(self, income, organization_type, is_regular_employee=True):
        self.income = income
        self.organization_type = organization_type
        self.is_regular_employee = is_regular_employee

    def calculate_tax(self): #  Calculate the tax based on the income and tax rates.
        if self.income <= 300000:
            tax_rate = 0 # no need to pay the tax
        elif 300001 <= self.income <= 400000:
            tax_rate = 0.1 # 10% tax rate for income between 300,001 and 400,000
        elif 400001 <= self.income <= 650000:
            tax_rate = 0.15 # 15% tax rate for income between 400,001 and 650,000
        elif 650001 <= self.income <= 1000000:
            tax_rate = 0.20 # 20% tax rate for income between 650,001 and 1,000,000
        elif 1000001 <= self.income <= 1500000:
            tax_rate = 0.25 # 25% tax rate for income between 1,000,001 and 1,500,000
        else:
            tax_rate = 0.30  # 30% tax rate for income above 1,500,000

        if self.income >= 1000000:
            tax_rate += 0.1  # Surcharge if income >= 1,000,000

        tax = self.income * tax_rate # Calculate tax amount by multiplying income with tax rate

        return tax

    def apply_deductions(self, tax):
        if self.organization_type == "Government" and not self.is_regular_employee:
            # Government organizations do not offer PF for contract employees
            pf_deduction = 0
        else:
            pf_deduction = 0.05 * self.income  # Assuming 5% for PF is deducted

        # Assuming deductions for children, GIS, and other deductions here
        children_deduction = 0  # Deduction for children
        gis_deduction = 0  # Deduction for GIS

        total_deduction = pf_deduction + children_deduction + gis_deduction

        tax -= total_deduction

        return max(0, tax)  # Ensure tax is non-negative


def main():
    # you will need these inputs to get asses to optional questions while calculating the tax
    income = float(input("Enter income: "))
    organization_type = input("Enter organization type (Government/Private/Corporate): ")
    is_regular_employee = input("Is the employee a regular employee? (True/False): ").lower() == "true"

    tax_calculator = TaxCalculator(income, organization_type, is_regular_employee)
    tax = tax_calculator.calculate_tax()
    net_tax = tax_calculator.apply_deductions(tax)

    print(f"Total tax payable: {net_tax}")


if __name__ == "__main__": #  Main function to run the tax calculator or Display the result
    main()
