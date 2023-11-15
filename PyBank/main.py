# open and read CSV
import os
import csv

# budget_csv = os.path.join('Resources', 'budget_data.csv')
# budget_csv = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")
# print("budget_data.csv resource path is:    ",budget_csv)

# #open and read csv
# with open(budget_csv) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')

# # read the header row first
#     csv_header = next(csv_file)
#     print(f"Header: {csv_header}")

# # read through each row of data acter the header
#    # for row in csv_reader:
#       #  print(row)

# # calculate total number of months in dataset
#     for row in csv_reader:
#         months = months + 1
#         print


# net toal amount of profts/losses 

# changes in profits/losses over entire period 
    # average of those changes

# greatest increase in  profits (date and amount) over entire period 

# greatest dec in profits over entire period 

# final script should BOTH print analysis to termianl and export a text file with the results



budget_csv = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")
# print("budget_data.csv resource path is:    ",budget_csv)

#open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

# read the header row first
    csv_header = next(csv_reader)
    # print(f"Header: {csv_header}")
    csv_list = list(csv_reader)
    # print(csv_list[0:5])


# for row in csv_list:
    # print(f"{row[0]}    {row[1]}")

# month list
month_list = [row[0] for row in csv_list]

#profit list
profit_list = [int(row[1]) for row in csv_list]

# total months
month_num = len(month_list)
print(month_num)

# total profit
profit_tot = sum(profit_list)
print(profit_tot)

# list of profit changes per month
profit_change = [profit_list[i] - profit_list[i-1] for i in range(1, month_num)]
#print(profit_change[0:5])

# month changes
month_change = [month_list[i] for i in range(1, month_num)]
#print(month_change[0:5])

# changes in profit over entire period 
average_change = sum(profit_change)/(month_num-1)
print(average_change)

# greatest increase in profits with date and amount
greatest_inc = max(profit_change)
# print(greatest_inc)
for i in range(month_num -1):
    # print(f"{i:3}  {profit_change[i]:12,}")
    if profit_change[i] == greatest_inc:
        greatest_month = month_change[i]
        # print(f"{i:3}  {profit_change[i]:12,} {greatest_month:7}")
print(greatest_month, greatest_inc)

# greatest decrease in profits with date and amount
greatest_dec = min(profit_change)
# print(greatest_dec)
for i in range(month_num -1):
    if profit_change[i] == greatest_dec:
        least_month = month_change[i]
print(least_month, greatest_dec)

# print results to a text file 
output_path = os.path.join(os.path.dirname(__file__), "Analysis", "pybank_text.txt")
# report = ( 
#         f"{' Financial Analysis ':-^48}\n"
#     f"{'Total Months:':24}{month_num:24,.0f}\n"
#     f"{'Net Profits:':24}{profit_tot:24,.0f}\n"
#     f"{'Avg Change:':24}{average_change:24,.0f}\n"
#     f"{'Max Increase:':14}{greatest_inc[0]:^20}{greatest_inc[1]:14,.0f}\n"
#     f"{'Max Decrease:':14}{greatest_dec[0]:^20}{greatest_dec[1]:14,.0f}\n"
#     f"{'--':-^48}"
# )
# with open(output_path, "w", encoding="UTF-8") as textfile:
#     textfile.write(report)

with open(output_path, "w") as textfile:   
    textfile.write("Financial Analysis\n")
    textfile.write(f"Total Months: {month_num}\n")
    textfile.write(f"Total: ${profit_tot:,}\n")
    textfile.write(f"Average Change ${round(average_change,2):,}\n")
    textfile.write(f"Greatest Increase in Profits: ${greatest_inc:,}\n")
    textfile.write(f"Greatest Decrease in Profits: ${greatest_dec:,}")
    