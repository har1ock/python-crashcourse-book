import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data_generate/lesson16/data/sitka_weather_07-2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates = []
    avgs = []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            avg = int(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            avgs.append(avg)


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, avgs, c='red', alpha=0.5)

# Відформатувати графік.
title ="Daily high and low temperatures - 2021\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()