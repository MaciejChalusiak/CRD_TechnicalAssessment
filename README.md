# CRD_TechnicalAssessment

# Setup
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Run tests
```
pytest tests.py
```


# Assumptions:
1. App not verify if amount from sold shares is enough to cover shares to buy.
2. Number of shares to buy/sell are rounded down.

# Manual Test Cases
Because automated tests are already written (logic is checked) manual TC are focus on GUI performance and logic part 
which is not implemented yet

| TC | Name                          | Input                                                                                                       | Expected result        |
|----|-------------------------------|-------------------------------------------------------------------------------------------------------------|------------------------|
| 1  | High number of shares to buy  | unit_price = 0.1<br/>current = 0%<br/>target = 100%                                                         | -1000000 shares to buy |
| 2  | High number of shares to sell | unit_price = 0.1<br/>current = 100%<br/>target = 0%                                                         | 1000000 shares to sell |
| 3  | Targets over 100%             | Sum of security targets gives above 100%                                                                    | app error              |
| 4  | Targets and current over 100% | Sum of security targets and current gives above 100%                                                        | app error              |
| 5  | Current over 100%                              | Sum of current security gives above 100%                                                             | app error                       |
| 6  | Not enough money to buy      | Security 1 : target 14% current: 15% unit_price: 10<br/>Security 2 : target 16% current: 15% unit_price: 200 | app error              |

