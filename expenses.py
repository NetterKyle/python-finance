# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 12:09:11 2024

@author: nette
"""

from balance_calculator import Balance
from taxes import calculateFederalTaxes, calculateCaliforniaTaxes, calculateSocialSecurityTaxes, calculateMedicareTaxes, calculateCaliforniaSdiTaxes


def calculate():
    salary = 160160.0

    balance = Balance("11/2023 - 2/2025")
    
    federalYearlyTaxes = calculateFederalTaxes(salary)
    stateYearlyTaxes = calculateCaliforniaTaxes(salary)
    socialSecurityYearlyTaxes = calculateSocialSecurityTaxes(salary)
    medicareYearlyTaxes = calculateMedicareTaxes(salary)
    californiaSdiYearlyTaxes = calculateCaliforniaSdiTaxes(salary)

    federalBiweeklyTaxes = federalYearlyTaxes / 26
    stateBiweeklyTaxes = stateYearlyTaxes / 26
    socialSecurityBiweeklyTaxes = socialSecurityYearlyTaxes / 26
    medicareBiweeklyTaxes = medicareYearlyTaxes / 26
    sdiBiweeklyTaxes = californiaSdiYearlyTaxes / 26
    
    biweeklyNetTaxes = federalBiweeklyTaxes + stateBiweeklyTaxes + socialSecurityBiweeklyTaxes + medicareBiweeklyTaxes + sdiBiweeklyTaxes
    biweeklyGrossIncome = salary / 26
    biWeekly401kContribution = 0.1 * biweeklyGrossIncome

    biweeklyNetIncome = biweeklyGrossIncome - biweeklyNetTaxes - biWeekly401kContribution
    
    monthlyNetIncome = biweeklyNetIncome * 26 / 12
    
    monthlyIncome = {"Job": monthlyNetIncome, "Rent Relief": 300.}

    monthlyExpenses = {
        "Rent": 2600.0,
        "Renter's Insurance": 15.0,
        "Electricity": 100.0,
        "Water": 30.0,
        "Gas": 30.0,
        "Trash": 50.0,
        "Parking": 0.0,
        "Party": 800,
        "Car": 390.0,
        "Car Insurance": 200.0,
        "Car Gas": 240.0,
        "Hulu": 75.0,
        "Netflix": 8.0,
        "Spotify": 10.0,
        "Apple TV": 10.0,
        "Guitar Tabs": 5.0,
        "Cat": 150
    }

    balance.addIncome(monthlyIncome)
    balance.addExpenses(monthlyExpenses)

    balance.calculatenetSavings()
    

    return balance




def main():
    balance = calculate()

    # print(
    #     "Monthly savings:",
    #     balance.netSavings
    # )
    # print(
    #     "Yearly savings:",
    #     balance.yearlySavings
    # )


main()