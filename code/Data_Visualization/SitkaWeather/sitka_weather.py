import csv
import matplotlib.pyplot as plt
from datetime import datetime

file = './sitka_weather_2018_simple.csv'

with open(file) as f:
    reader = csv.reader(f)       # reader
    header_row = next(reader)       # csv next

    for index, context in enumerate(header_row):
        print(f"{index} - {context}")

    # Read high and low temperatures, date
    dates, high, low = [], [], []
    for row in reader:
        date = datetime.strptime(row[header_row.index('DATE')], '%Y-%m-%d')  # Formatting date
        high_temp = int(row[header_row.index('TMAX')])
        low_temp = int(row[header_row.index('TMIN')])
        dates.append(date)
        high.append(high_temp)
        low.append(low_temp)

    # Visualization with matplotlib
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, high, c='orange', alpha=0.5, label='High Temperature')
    ax.plot(dates, low, c='blue', alpha=0.5, label='Low Temperature')
    plt.fill_between(dates, high, low, facecolor='blue', alpha=0.1) # Fill between

    ax.set_title('Daily High and Low Temperature, 2018', fontsize=24)
    ax.set_xlabel('Date', fontsize=14)
    ax.set_ylabel('Temperature (F)', fontsize=14)
    ax.tick_params(axis='both', which='major', labelsize=16)
    ax.legend()

    ax.set_xlim([datetime(2018, 1, 1), datetime(2019, 1, 1)])
    ax.set_ylim([20, 130])

    fig.autofmt_xdate()     # manage x label to prevent overlapping

    plt.savefig('sitka_weather')