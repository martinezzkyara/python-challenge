import csv

# read excel 
data=[]

with open('Resources/budget_data.csv', 'r', newline='') as fr:
    reader=csv.reader(fr)

    for row in reader:
        data.append(row)
data=data[1:len(data)]
 

# total number of months in data set

total_months= len(data)


# net total amount of "profit/losses" over the entire period
net_total=0.0
for p in data:
    net_total=net_total +float(p[1])    
    

# the changes in "profit/Losses" over the entire period, and then the average of those changes
changes=[]
for ii in range(1,len(data)):
    temp_change=float(data[ii][1])-float(data[ii-1][1])
    changes.append(temp_change)
total_changes=0.0
for iii in changes:
    total_changes=total_changes+iii
average_change=total_changes/(total_months-1)
   

# the greatest increase in profits (date and amount) over the entire period 
current_max=0
for jj in range(len(changes)):
    if jj==0:
        current_max=0
    else:
        #if float(data[jj][1])> float(data[current_max][1]):
        if (changes[jj])> (changes[current_max]):
            current_max=jj
max_profit=changes[current_max]
max_month=data[current_max+1][0]
max_statement='Greatest Increase in Profits: '+max_month+' ($'+str(max_profit)+')'


# the greatest decrease in profits (date and amount) over the entire period

current_min=0
for jj in range(len(changes)):
    if jj==0:
        current_min=0
    else:
        #if float(data[jj][1])> float(data[current_min][1]):
        if (changes[jj])< (changes[current_min]):
            current_min=jj
min_profit=changes[current_min]
min_month=data[current_min+1][0]
min_statement='Greatest Decrease in Profits: '+min_month+' ($'+str(min_profit)+')'
total_month_statement='Total Months: '+str(total_months)
net_total_statement='Total: $' +str(net_total)
average_change_statement='Average Change: $'+str(average_change)
line1='Financial Analysis' 
line2='----------------------------'
print(line1)
print(line2)
print(total_month_statement)
print(net_total_statement)
print(average_change_statement)
print(max_statement)
print(min_statement)


