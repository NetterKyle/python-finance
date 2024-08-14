import pandas as pd
from taxes import calculateFederalTaxes


class Balance:
    def __init__(self, name):
        self.name = name

    def addIncome(self, incomeDict):
        self.income = incomeDict
        # print(self.income)

    def addExpenses(self, costDict):
        self.expenses = costDict

    def calculateIncomeTotal(self):
        self.totalIncome = sum(self.income.values())
        print("Monthly income:", self.totalIncome)

    def calculateCostTotal(self):
        self.totalExpenses = sum(self.expenses.values())
        print("Monthly expenses:", self.totalExpenses)

    def calculatenetSavings(self):
        self.calculateIncomeTotal()
        self.calculateCostTotal()
        self.netSavings = self.totalIncome - self.totalExpenses
        self.yearlySavings = self.netSavings * 12
        print("Amount saved per month:", self.netSavings)
        print("Amount saved per year:", self.yearlySavings)
