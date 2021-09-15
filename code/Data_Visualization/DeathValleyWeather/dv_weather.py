import csv
import matplotlib.pyplot as plt
from datetime import datetime

file = './death_valley_2018_simple.csv'

with open(file) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, context in enumerate(header_row):
        print(f'{index} - {context}')

    # Access high and low temperature, date datas from the file
    highs, lows, dates = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except:
            print(f"Missing data for {date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)

    # Visualize the data
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    ax.set_title('Daily Temperature, 2018\nDeath Valley', fontsize=24)
    ax.set_xlabel('Date', fontsize=14)
    ax.set_ylabel('Temperature (F)', fontsize=14)
    ax.tick_params(axis='both', which='major', labelsize=16)

    ax.set_ylim([20, 130])

    fig.autofmt_xdate()
    plt.savefig("dv_weather")