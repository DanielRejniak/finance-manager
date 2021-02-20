import json
from prettytable import PrettyTable
from datetime import datetime

# Global income and spendign variables
total_income = 0
total_spending = 0

# Define tables
spendingIncomeSavingSummary = PrettyTable(['Income','Amount'])
upcomingBillsSummary = PrettyTable(['Direct Debit','Amount','Due in (n) days'])
otherSpendingSummary = PrettyTable(['Spending','Amount'])

def calculateDaysLeft(day):

    # Get current day
    currentDay = datetime.now().day

    # Calculate days left
    dueInDays = day - currentDay

    if(dueInDays < 0):
        return "Payed"

    if(dueInDays == 0):
        return "Due today"

    if(dueInDays > 0):
        return "Due in " + str(dueInDays)

# Opening JSON file 
with open('finance-sheet.json') as json_file: 
    data = json.load(json_file)

# Print income data
for incomeItem in data['income']:

    # Sum up the income
    total_income += incomeItem['amount']

# Print spendign data
for directDebitItem in data['direct_debit']:

    # Sum up the spending's
    total_spending += directDebitItem['amount']

    # Populate the table
    upcomingBillsSummary.add_row([directDebitItem['name'],directDebitItem['amount'],calculateDaysLeft(directDebitItem['dayOfMonth'])])

# Calculate other spendign data
for otherSpendingItem in data['other_spendings']:

    # Sum up the spending's
    total_spending += otherSpendingItem['amount']

    # Populate the table
    otherSpendingSummary.add_row([otherSpendingItem['name'],otherSpendingItem['amount']])

# Calculate savings
savings = total_income - total_spending

# Update spending income saving summary table
spendingIncomeSavingSummary.add_row(['Total income', str(total_income)])
spendingIncomeSavingSummary.add_row(['Total spending', str(total_spending)])
spendingIncomeSavingSummary.add_row(['Total saving', str(savings)])

# Print summary tables
print("\n## Income Summary")
print(spendingIncomeSavingSummary)
print("\n## Direct Debit Summary")
print(upcomingBillsSummary)
print("\n## Other spending's Summary")
print(otherSpendingSummary)
