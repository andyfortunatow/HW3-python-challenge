#Import Modules
import os
import csv

#Setting path file
csvpath = os.path.join("/Users/drew/HW3-python-challenge/PyBank/Resources/budget_data.csv")

#Creating empty lists to loop through specific rows for the following variables
total_months = []
total_profit = []
monthly_profit_change = []

# Open CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",") 

    # Skip first row
    header = next(csvreader)  

    # Loop through rows
    for row in csvreader: 

        # Append the total months & total profit to their respective lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Loop through profits in order to determine the monthly change
    for i in range(len(total_profit)-1):
        
        # Determining the difference between one month and the next, adding it to the monthly profit change list
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Finding the maximum and minimum values in the the monthly profit change list which will determine maximum increase & maximum decrease
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)


#Using index, finding the respective month for the maximum increase & maximum decrease. As the greatest increase and maximum decrease effects the month after it is recorded, we +1 to each value. 

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Printing Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Number of Months: {len(total_months)}")
print(f"Net Total: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} ({(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} ({(str(max_decrease_value))})")

# File Output
output_path = os.path.join("/Users/drew/HW3-python-challenge/PyBank/Analysis/HW3PyBank.txt")

with open(output_path,'w') as f:

    f.write('Financial Analysis')
    f.write("\n")
    f.write("----------------------------")
    f.write("\n")
    f.write(f"Total Number of Months: {len(total_months)}")
    f.write("\n")
    f.write(f"Net Total: ${sum(total_profit)}")
    f.write("\n")
    f.write(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    f.write("\n")
    f.write(f"Greatest Increase in Profit: {total_months[max_increase_month]} ({(str(max_increase_value))})")
    f.write("\n")
    f.write(f"Greatest Decrease in Profit: {total_months[max_decrease_month]} ({(str(max_decrease_value))})")  
 


