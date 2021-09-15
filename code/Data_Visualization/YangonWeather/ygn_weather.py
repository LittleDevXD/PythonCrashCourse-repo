import matplotlib.pyplot as plt
from datetime import datetime
import csv

file = 'YgnWeatherFrom2021-01to2021-08.csv'

with open(file) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    next_row = next(reader)

    # Store Data from the file
    highs, lows, dates = [], [], []
    for row in reader:
        date = datetime.strptime(row[header_row.index('DATE')], '%Y-%m-%d') 
        try:
            high = int(row[header_row.index('TMAX')])
            low = int(row[header_row.index('TMIN')])
        except:
            print(f'Missing Data for {date}')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)

    # Visualize data from the file
    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    ax.plot(dates, highs, c='red', alpha=0.5, label='high temperature')
    ax.plot(dates, lows, c='blue', alpha=0.5, label='low temperature')
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    ax.set_title(f'Daily High and Low temperature reported by {next_row[0]}, 2021 January To August\nYangon', fontsize=18)
    ax.set_xlabel('Date', fontsize=14)
    ax.set_ylabel('Temperature (F)', fontsize=14)
    ax.tick_params(axis='both', which='major', labelsize=16)

    fig.autofmt_xdate()
    plt.show()