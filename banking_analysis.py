import pandas as pd
import re
import warnings

warnings.filterwarnings("ignore")

# Data Cleaning
def clean_data(df):
    df['Account Number'] = df['Account Number'].str.replace(r'[^a-zA-Z0-9]', '')
    df['Amount'] = pd.to_numeric(df['Amount'].replace('[^\d.]', '', regex=True))
    return df


# Data Analysis
def analyze_data(df):
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
    df = df.sort_values(by='Transaction Date')

    # Maintaining subtotal/yearly total seperately
    totals = df[df['Account Number'].str.contains('TOTAL')]
    totals.loc[totals['Account Number'].isin(['SUBTOTAL', 'YEARLYTOTAL']), 'Description'] = totals['Account Number']
    totals = totals.drop('Account Number', axis=1)
    totals = totals.drop('Transaction Type', axis=1)

    # Removing totals from data for further analysis
    df = df[~df['Account Number'].str.contains('TOTAL')]

    # Maintaing a Closing Balance after every transaction with assumption that the initial Balance is 0.0
    transaction_types = {'Card Payment': '-', 'Deposit': '+', 'Withdrawal': '-', 'ATM Withdrawal': '-', 'Online Transfer': '-', 'Direct Debit': '-'}
    initialValue=0.0
    for index, row in df.iterrows():
        operation = transaction_types[row['Transaction Type']]
        initialValue = initialValue + eval(f"{operation}{row['Amount']}")
        df.at[index, 'Closing Balance'] = initialValue
    return df,totals

# Anomaly :  flag transactions where the absolute value of the amount is significantly higher than the mean or median.
def detect_anomalies(df):
    threshold = 3 * df['Amount'].std()
    df['Anomaly'] = df['Amount'].abs() > threshold
    return df

# Reporting
def summary_report(df,totals):
    # Discrepancies in Reconciliation
    reconciliation_discrepancies = totals['Amount'].sum() - df['Amount'].sum()

    # List of Detected Anomalies
    detected_anomalies = df[df['Anomaly']]

    # Summary Report
    print("=== Summary Report ===")
    print(f"1. Discrepancies in Reconciliation: ${reconciliation_discrepancies:.2f}")
    print("\n2. List of Detected Anomalies:")
    print(detected_anomalies[['Transaction Date', 'Account Number', 'Transaction Type', 'Amount']])

    # Additional Information
    print("\n=== Additional Information ===")
    print("3. Total Transactions (excluding totals):", len(df))
    print("4. Total Transactions with Anomalies:", len(detected_anomalies))
    print("5. Closing Balance after Last Transaction:", df.iloc[-1]['Closing Balance'])


if __name__ == "__main__":
    csv_file_path = './banking_data_assignment.csv'
    df = pd.read_csv(csv_file_path)
    df = clean_data(df)
    df,totals = analyze_data(df)
    df = detect_anomalies(df)
    summary_report(df,totals)


