import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data_generate/lesson16/data/death_valley_2021_simple.csv'
with open(filename) as f:
    reader = csv.DictReader(f)
    # Отримати дати, високі та низькі температури з цього файлу.
    dates = []
    highs = []
    lows = []
    
    for row in reader:
        current_date = datetime.strptime(row['DATE'], '%Y-%m-%d')
        try:
            high = int(row['TMAX'])
            low = int(row['TMIN'])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Створити графік високих температур.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Відформатувати графік.
title ="Daily high and low temperatures - 2021\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
ax.set_ylim(0, 130)
plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()