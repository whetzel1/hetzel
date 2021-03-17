import csv
import math
import matplotlib.pyplot as plt


count = 1

file_name_r = open("MSFT.csv", "r")
Enter_file_name = ''

while Enter_file_name != ".csv":
    count += 1

    Enter_file_name = input("Enter file name with '.csv': ")
    if Enter_file_name == ".csv":
        print (file_name_r.read())


with open("MSFT.csv", "rU") as infile:
    reader = csv.DictReader(infile)
    data = {}
    for row in reader:
        for header, value in row.items():
            try:
                data[header].append(value)
            except KeyError:
                data[header] = [value]




Price = data["Price"]
list_of_Price = [float(item) for item in Price]

Open = data["Open"]
list_of_Open = [float(item) for item in Open]

High = data["High"]
list_of_High = [float(item) for item in High]

Low = data["Low"]
list_of_Low = [float(item) for item in Low]

Change = data["Change %"]
new_change = [x[:-1] for x in Change]
list_of_new_change = [float(item)for item in new_change]

#descriptive stats on price

print("Descriptive Stats for Price: \n --------------------------------")
price_count = len(list_of_Price)
print("Count: ", f'{price_count}')
price_mean = sum(list_of_Price)/price_count
print("Mean: ", f'{price_mean:.2f}')



var_price  = sum(pow(x-price_mean,2) for x in price_mean) / len(price_mean)  # variance
std_price  = math.sqrt(var_price)  # standard deviation
print("Std: ", f'{std_price:.2f}')
min_price = min(list_of_Price)
print("Min: ", f'{min_price}')

sorted_price = sorted(list_of_Price, key = float)

max_price = max(list_of_Price)
print("Max: ", f'{max_price}')

sorted_open = sorted(list_of_Open)
twenty_five_percentile_open= sorted_open[round(0.25 * (count + 1)) - 1]
print('Twenty-fifth percentile is', f'{twenty_five_percentile_open}')


fifty_percentile_open= sorted_open[round(0.50 * (count + 1)) - 1]
print('Fiftieth percentile is', f'{fifty_percentile_open}')

seventy_fifth_percentile_open= sorted_open[round(0.75 * (count + 1)) - 1]
print('Seventy-fifth percentile is', f'{seventy_fifth_percentile_open}')
#descriptive stats for Open

print("Descriptive Stats for Open: \n --------------------------------")
Open_count = len(list_of_Open)
print("Count: ", f'{Open_count}')
Open_mean = sum(list_of_Open)/Open_count
print("Mean: ", f'{Open_mean:.2f}')

var_open  = sum(pow(x-Open_mean,2) for x in Open_mean) / len(Open_mean)  # variance
std_open = math.sqrt(var_open)  # standard deviation
print("Std: ", f'{std_open:.2f}') # fix this ...

min_open = min(list_of_Open)
print("Min: ", f'{min_open}')

sorted_open = sorted(list_of_Open, key = float) # need to learn how to slice percentiles

max_open = max(list_of_Open)
print("Max: ", f'{max_open}')

#descriptive stats for high

print("Descriptive Stats for High: \n --------------------------------")
high_count = len(list_of_High)
print("Count: ", f'{high_count}')
high_mean = sum(list_of_High)/high_count
print("Mean: ", f'{high_mean:.2f}')




var  = sum(pow(x-high_mean,2) for x in high_mean) / len(high_mean)  # variance
std  = math.sqrt(var)  # standard deviation

print("Std: ", f'{std:.2f}') # fix this ...

min_high = min(list_of_High)
print("Min: ", f'{min_high}')

sorted_high = sorted(list_of_High, key = float)

max_high = max(list_of_High)
print("Max: ", f'{max_high}')

sorted_high = sorted(list_of_High)
twenty_five_percentile_high= sorted_high[round(0.25 * (count + 1)) - 1]
print('Twenty-fifth percentile is', f'{twenty_five_percentile_high}')


fifty_percentile_high= sorted_high[round(0.50 * (count + 1)) - 1]
print('Fiftieth percentile is', f'{fifty_percentile_high}')

seventy_fifth_percentile_high= sorted_high[round(0.75 * (count + 1)) - 1]
print('Seventy-fifth percentile is', f'{seventy_fifth_percentile_high}')


#descriptive statisctics for Low

print("Descriptive Stats for Low: \n --------------------------------")
low_count = len(list_of_Low)
print("Count: ", f'{low_count}')
low_mean = sum(list_of_Low)/price_count
print("Mean: ", f'{low_mean:.2f}')

var_low  = sum(pow(x-low_mean,2) for x in low_mean) / len(low_mean)  # variance
std_low  = math.sqrt(var_low)  # standard deviation
print("Std: ", f'{std_low:.2f}')

min_low = min(list_of_Low)
print("Min: ", f'{min_low}')

sorted_low = sorted(list_of_Low, key = float)

max_low = max(list_of_Low)
print("Max: ", f'{max_low}')

sorted_low = sorted(list_of_Low)
twenty_five_percentile_low= sorted_low[round(0.25 * (count + 1)) - 1]
print('Twenty-fifth percentile is', f'{twenty_five_percentile_low}')


fifty_percentile_low= sorted_low[round(0.50 * (count + 1)) - 1]
print('Fiftieth percentile is', f'{fifty_percentile_low}')

seventy_fifth_percentile_low= sorted_low[round(0.75 * (count + 1)) - 1]
print('Seventy-fifth percentile is', f'{seventy_fifth_percentile_low}')


# descriptive stats for Change

print("Descriptive Stats for Change: \n --------------------------------")
change_count = len(list_of_new_change)
print("Count: ", f'{change_count}')
change_mean = sum(list_of_new_change)/change_count
print("Mean: ", f'{change_mean:.2f}')

var_change  = sum(pow(x-change_mean,2) for x in change_mean) / len(change_mean)  # variance
std_change  = math.sqrt(var_change)  # standard deviation
print("Std: ", f'{std_change:.2f}') # fix this ...

min_change = min(list_of_new_change)
print("Min: ", f'{min_change}')

sorted_change = sorted(list_of_new_change, key = float) # need to learn how to slice percentiles

max_change = max(list_of_new_change)
print("Max: ", f'{max_change}')

sorted_change = sorted(list_of_new_change)
twenty_five_percentile_change= sorted_change[round(0.25 * (count + 1)) - 1]
print('Twenty-fifth percentile is', f'{twenty_five_percentile_change}')


fifty_percentile_change= sorted_change[round(0.50 * (count + 1)) - 1]
print('Fiftieth percentile is', f'{fifty_percentile_change}')

seventy_fifth_percentile_change= sorted_change[round(0.75 * (count + 1)) - 1]
print('Seventy-Fifth percentile is', f'{seventy_fifth_percentile_change}')


# finish off with graphs

plt.plot(list_of_High)
plt.show(list_of_High)
plt.plot(list_of_Low)
plt.show(list_of_Low)
plt.plot(list_of_Open)
plt.show(list_of_Open)
plt.plot(list_of_Price)
plt.show(list_of_Price)
plt.plot(list_of_new_change)
plt.show(list_of_new_change)