# from pathlib import Path
# import csv
# from matplotlib import pyplot as plt
# from datetime import datetime

# plt.style.use("seaborn-v0_8")

# path = Path("sitka_weather_2021_full.csv")
# lines = path.read_text().splitlines()
# reader = csv.reader(lines)
# header_row = next(reader)
# dates, highs, lows = [], [], []
# fig, ax = plt.subplots()

# for row in reader:
#     current_date = datetime.strptime(row[2], '%Y-%m-%d')
#     single_high = int(row[4])
#     single_low = int(row[5])
#     dates.append(current_date)
#     highs.append(single_high)
#     lows.append(single_low)

# ax.plot(dates, highs, color='red', alpha=0.5)
# ax.plot(dates, lows, color='blue', alpha=0.5)
# ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24, alpha=0.1)

# # ax.set_title("Annual High Temperatures, July 2021", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel("Temperature (F)", fontsize=16)
# ax.tick_params(labelsize=16)

# plt.show()

# def test(parameter, fixed_param=2, *arb_param, **arb_para):

#     print()

# test(arguement, fixed_param=3)

from pathlib import Path
import csv
from matplotlib import pyplot as plt
from datetime import datetime

plt.style.use("seaborn-v0_8")

path = Path("sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows = [], [], []
fig, ax = plt.subplots()

for row in reader:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        
        # Ensure the values are not empty before conversion
        if row[4] and row[5]:  
            single_high = int(float(row[4]))  # Convert safely
            single_low = int(float(row[5]))  
            
            dates.append(current_date)
            highs.append(single_high)
            lows.append(single_low)
        # else:
        #     print(f"Skipping missing data for {row[2]}")

    except ValueError as e:
        print(f"Error on {row[2]}: {e}")

ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24, alpha=1.0)  # Fixed title visibility

ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
