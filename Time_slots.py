from datetime import datetime, timedelta
time_format = ["AM", "PM"]
time_slots_am = ["08:00-09:00", "09:00-10:00", "10:00-11:00", "11:00-12:00"]
time_slots_pm = ["12:00-01:00", "01:00-02:00", "02:00-03:00", "05:00-06:00", "06:00-07:00", "07:00-08:00",
                 "08:00-09:00", "09:00-10:00", "10:00-11:00"]

time_slots_am_dict = {"08:00-09:00": 5, "09:00-10:00": 5, "10:00-11:00": 5, "11:00-12:00": 5}
time_slots_pm_dict = {"12:00-01:00": 5, "01:00-02:00": 5, "02:00-03:00": 5, "05:00-06:00": 5, "06:00-07:00": 5,
                      "07:00-08:00": 5,
                      "08:00-09:00": 5, "09:00-10:00": 5, "10:00-11:00": 5}

# Set today's date manually
today_date = datetime.now().date()  # Change the date as needed

# Create a list with the next 10 dates
next_10_dates = [today_date + timedelta(days=i) for i in range(0, 10)]

# Print the list of next 10 dates in a readable format

dates=[]
for date in next_10_dates:
    dates.append(date.strftime("%d/%m/%Y"))
table_1_am=dict.fromkeys(dates,time_slots_am_dict)
table_1_pm=dict.fromkeys(dates,time_slots_pm_dict)
table_2_am=dict.fromkeys(dates,time_slots_am_dict)
table_2_pm=dict.fromkeys(dates,time_slots_pm_dict)
table_3_am=dict.fromkeys(dates,time_slots_am_dict)
table_3_pm=dict.fromkeys(dates,time_slots_pm_dict)
table_4_am=dict.fromkeys(dates,time_slots_am_dict)
table_4_pm=dict.fromkeys(dates,time_slots_pm_dict)
print(table_1_am)




