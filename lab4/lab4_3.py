from datetime import datetime

current_date = datetime.now()
print("Current datetime with microseconds:", current_date)

datetime_without_microseconds = current_date.replace(microsecond=0)
print("Datetime without microseconds:", datetime_without_microseconds)