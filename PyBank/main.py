#PyBank
#Lauren Todd-Mariano
#Assignment 3
#Create a python script to analyze financial records

# import operating system & csv file
import os
import csv

# tell mr. python where to find the csv file
csvpath = os.path.join("budget_data.csv")

#tell mr. python how to read file and that there is a header
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #create a place for the data to go, required so can pull corresponding month to the max/min amounts
    profit_loss = []
    date = []
    profit_loss_change = []
    
    #need to update the profit_loss column with the # from the 2nd column and update the date with the month_row data from 1st column
    for row in csvreader:        
        profit_loss.append(float(row[1]))
        date.append(row[0])
    
    #print header, total months, and total profit/loss
    print ("Financial Analysis")
    print ("Total Months:", len(date))
    print ("Total Profit/Loss: $", sum(profit_loss))
   
   #need to find a way to reference previous row (i-1) to determine change in profit, want to store that for all lines
   #average of the change between rows
   #max of the change between rows & corresponding date
   #min of the change between rows & corresponding date
    for i in range (1, len(profit_loss)):
        profit_loss_change.append(profit_loss[i] - profit_loss[i-1])
        avg_profit_loss_change = sum(profit_loss_change)/len(profit_loss_change)
        max_profit_loss_change = max(profit_loss_change)
        min_profit_loss_change = min(profit_loss_change)

        max_profit_loss_change_date = str(date[profit_loss_change.index(max(profit_loss_change))])
        min_profit_loss_change_date = str(date[profit_loss_change.index(min(profit_loss_change))])

    #print average profit loss, max profit loss, and min profit loss
    print("Average Profit Loss Change: $", (avg_profit_loss_change))
    print ("Max Profit Loss Change:", (max_profit_loss_change), "Month & Year of Largest Increase", (max_profit_loss_change_date))
    print("Min Profit Loss Change:", (min_profit_loss_change), "Month & Year of Largest Decrease", (min_profit_loss_change_date))
   

#First Attempt (just for Lauren's Records)
#import os
#import csv

#csvpath = os.path.join("budget_data.csv")
    
#count = 0 
#profit_loss_total = 0

#with open(csvpath, newline='') as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=',')
    #csv_header = next(csvreader)

    #for row in csvreader:        
        #count = count + 1
        #profit_loss_total = profit_loss_total + int(row[1])
        
#print('Financial Analysis')
#print(f'# of Months: {(count)}')
#print(f'Total: ${profit_loss_total}')