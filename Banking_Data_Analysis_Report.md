# Banking Data Analysis Report

## Overview

This report presents an analysis of banking transactions using the provided dataset. The analysis includes data cleaning, normalization, reconciliation, and anomaly detection.

## Data Cleaning

- Account numbers and descriptions were cleaned to remove special characters and ensure consistency.
- Amount values were normalized to a consistent format, handling currency symbols and negative values for withdrawals.

## Data Analysis

- Transactions were sorted chronologically to maintain a sequential order.
- Subtotal and yearly total transactions were separated from individual transactions.
- Closing balances were calculated based on transaction types and amounts.
- Anomalies were detected by flagging transactions with significantly higher absolute amounts than the mean or median.

## Anomaly Detection

- Anomalies were identified using a threshold of three times the standard deviation of transaction amounts.
- Detected anomalies are listed in the report.

## Findings

### Reconciliation Discrepancies

- Discrepancies in reconciliation were found, with a total difference of $-236,342.00.

### Detected Anomalies

The following transactions were flagged as anomalies:

| Transaction Date | Account Number | Transaction Type | Amount  |
| ----------------- | -------------- | ----------------- | -------|
| 2023-01-10        | ACClOO9        | Withdrawal        | $4,853  |
| 2023-01-27        | ACClOO7        | Deposit           | $4,830  |
| 2023-02-17        | ACClOOO        | Withdrawal        | $4,752  |
| 2023-02-19        | ACClOO4        | Direct Debit       | $4,550  |
| 2023-02-23        | ACClOO5        | Direct Debit       | $4,825  |
| 2023-03-01        | ACClOOl        | Card Payment       | $4,903  |
| 2023-03-06        | ACClOO7        | Online Transfer    | $4,551  |
| 2023-05-12        | ACClOO6        | ATM Withdrawal     | $4,562  |
| 2023-06-07        | ACClOO3        | Online Transfer    | $4,605  |
| 2023-06-19        | ACClOO7        | Card Payment       | $4,863  |
| 2023-06-28        | ACClOO2        | Deposit            | $4,438  |
| 2023-07-21        | ACClOO7        | Withdrawal         | $4,848  |
| 2023-07-22        | ACClOO4        | Deposit            | $4,851  |
| 2023-07-26        | ACClOO3        | ATM Withdrawal     | $4,574  |
| 2023-08-02        | ACClOO9        | Direct Debit       | $4,793  |
| 2023-08-26        | ACClOO6        | Deposit            | $4,976  |
| 2023-09-14        | ACClOO4        | Deposit            | $4,780  |
| 2023-11-11        | ACClOO2        | Direct Debit       | $4,543  |
| 2023-11-21        | ACClOO3        | ATM Withdrawal     | $4,447  |

## Additional Information

- Total transactions (excluding totals): 150
- Total transactions with anomalies: 19
- Closing balance after the last transaction: -$245,034.00

## Notes

- Closing balance is calculated with the assumption of an initial balance of zero.
- `transaction_types` were defined to indicate whether a transaction is a debit or credit.
```python
transaction_types = {
    'Card Payment': '-',
    'Deposit': '+',
    'Withdrawal': '-',
    'ATM Withdrawal': '-',
    'Online Transfer': '-',
    'Direct Debit': '-'
}
```
- Anomaly logic: Flag transactions where the absolute value of the amount is significantly higher than the mean or median.

---

*This report is generated using a Python script. Refer to the code and README for details on data processing and anomaly detection.*

