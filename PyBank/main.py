# Your task is to create a Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# import libraries
import csv
import os

# define paths for imported and exported files
imported_csv = os.path.join("budget_data.csv")
ouput_file = os.path.join("budget_analysis.txt")

#define variables
total_months = 0
net_profit = 0
profit_change = []
ave_profit_change = 0
greatest_increase_profits = ["", 0]
greatest_decrease_losses = ["", 10000000000000000]



# read the data from csv
with open(imported_csv) as financial_data:
    reader = csv.reader(financial_data)

    # read the header row
    header = next(reader)
    print(header)

    #change the first row so the calculations do not include the headers
    first_row = next(reader)
    total_months = total_months + 1
    net_profit = net_profit + int(first_row[1])
    prev_net = int(first_row[1])


    for row in reader:
        # increment total months and net profit
        total_months = total_months + 1
        net_profit = net_profit + int(row[1])


        # calculate the change in profit
        net_change = int(row[1])-prev_net
        profit_change = profit_change + [net_change]
        prev_net = int(row[1])

        # test if the change is the greatest
        if greatest_increase_profits[1] < net_change:
            greatest_increase_profits[1] = net_change
            greatest_increase_profits[0] = row[0]
        # test if the change is smallest loss 
        if greatest_decrease_losses[1] > net_change:
            greatest_decrease_losses[1] = net_change
            greatest_decrease_losses[0] = row[0]


    # calculate the average change from the formed list
    ave_profit_change = sum(profit_change)/len(profit_change)

# output
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_profit}\n"
    f"Average  Change: ${ave_profit_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_profits[0]} (${greatest_increase_profits[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_losses[0]} (${greatest_decrease_losses[1]})\n"
)

print(output)

with open(ouput_file, "w") as txt_file:
    txt_file.write(output)
    