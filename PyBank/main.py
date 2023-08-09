import os
import csv

csvbudget = os.path.join('..','Resources','budget_data.csv')
with open(csvbudget) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader,None)
    #print(f"Header:{csv_header}")

    
    months = []
    profit = []
 
    for row in csvreader:

        months.append(row[0])

        profit.append(row[1])

    Total_profit = 0
    for profit_str in profit:
        profit_value= int(profit_str)
        Total_profit += profit_value
    #print("Original list:", profit)
    #print("total_profit:", Total_profit)


    revenue_change = []
    for i in range(1,len(profit)):

        revenue_change.append((int(profit[i])-int(profit[i-1])))

        average_change = round(sum(revenue_change)/len(revenue_change),2)

        greatest_increase = max(revenue_change)

        greatest_decrease = min(revenue_change)

    total_months = len(months)
    #total = sum(profit)

    print("Financial Analysis")

    print("----------------------------")

    print("Total Months: " + str(total_months))

    print("Total: " + "$" + str(Total_profit))

    print("Average Change " + "$" + str(average_change))

    print("Greatest Increase in Profits: " + str(months[revenue_change.index(greatest_increase)+1]) + " (" + "$" + str(greatest_increase) + ")")

    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(greatest_decrease)+1]) + " (" + "$" + str(greatest_decrease) + ")")

#sending txt file to analysis folder

output_path = os.path.join("..", "analysis", "output.txt")

with open(output_path, 'w', newline='') as file:
    

    #file = open("output.txt", "w")

    file.write("Financial Analysis" + "\n")

    file.write("----------------------------" + "\n")

    file.write("Total Months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(Total_profit) + "\n")

    file.write("Average Change " + "$" + str(average_change) + "\n") 

    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(greatest_increase)+1]) + " (" + "$" + str(greatest_increase) + ")" + "\n")

    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(greatest_decrease)+1]) + " (" + "$" + str(greatest_decrease) + ")" + "\n") 

  
   