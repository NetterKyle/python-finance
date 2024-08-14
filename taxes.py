import numpy as np

def calculateTaxes(salary, brackets, taxRates):
    taxesPerBracket = (
        (brackets[:, 1] - brackets[:, 0]) * (salary > brackets[:, 1])
        + (salary - brackets[:, 0])
        * ((brackets[:, 0] < salary) & (salary < brackets[:, 1]))
    ) * taxRates

    return np.sum(taxesPerBracket)


def calculateFederalTaxes(salary):
    brackets = np.array(
        [
            [0, 11000.0],
            [11001.0, 44725.0],
            [44726.0, 95375.0],
            [95376, 182100.0],
            [182101.0, 231250.0],
            [231251.0, 578125.0],
            [578125.0, 1e12],
        ]
    )
    taxRates = np.array([0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37])
    taxesPerBracket = calculateTaxes(salary, brackets, taxRates)

    return np.sum(taxesPerBracket)

def calculateCaliforniaTaxes(salary):
    brackets = np.array(
        [
            [0, 20824.0],
            [20824.0, 49368.0],
            [49368.0, 77918.0],
            [77918, 108162.0],
            [108162.0, 136700.0],
            [136700.0, 698274.0],
            [698274.0, 837922.0],
            [837922.0, 1396542.0],
            [1396542.0, 1e12]
        ]
    )
    taxRates = np.array([0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.013, 0.113, 0.123])
    taxesPerBracket = calculateTaxes(salary, brackets, taxRates)

    return np.sum(taxesPerBracket)


def calculateSocialSecurityTaxes(salary):
    return salary * 0.062

def calculateMedicareTaxes(salary):
    return salary * 0.0145

def calculateCaliforniaSdiTaxes(salary):
    return salary * 0.011