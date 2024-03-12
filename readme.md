

# Banking Data Analysis Script

## Overview

This script analyzes banking transaction data, focusing on data cleaning, analysis, and anomaly detection. The analysis includes reconciling transactions and identifying anomalies based on transaction amounts.

## How to Run

1. Ensure you have Python installed on your system.
2. Install the required libraries by running the following command:
   ```
   pip install pandas
   ```

3. Download the script (`banking_analysis.py`) and the CSV data file (`banking_data_assignment.csv`) to the same directory.

4. Open a terminal or command prompt in the directory where the script and CSV file are located.

5. Run the script by executing the following command:
   ```
   python banking_analysis.py
   ```

6. The script will output the summary report, displaying discrepancies in reconciliation and a list of detected anomalies.

## Data Cleaning

The data cleaning process involves two main steps:

- **Account Number:** Removing special characters from the 'Account Number' column using regular expressions.
- **Amount:** Converting the 'Amount' column to numeric format, handling non-numeric characters and currency symbols.

## Data Analysis

The data analysis process consists of the following steps:

1. **Sorting:** The dataset is sorted chronologically by the 'Transaction Date' column.
2. **Separating Totals:** Subtotal and yearly total rows are separated into a separate DataFrame (`totals`).
3. **Closing Balance Calculation:** A closing balance is maintained after each transaction, assuming an initial balance of 0.0.
4. **Anomaly Detection:** Transactions with amounts significantly higher than the mean or median are flagged as anomalies.

## Interpretation of Output

The script generates a summary report with the following information:

1. **Discrepancies in Reconciliation:** The difference between the total amounts in the original data and the total amounts in the 'totals' DataFrame.
2. **Detected Anomalies:** A list of transactions flagged as anomalies, including transaction details.

Additional information, such as the total number of transactions and the closing balance after the last transaction, is also provided.
