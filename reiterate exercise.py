from datetime import datetime
def is_date_in_range(date, start_date, end_date):
   return start_date <= date <= end_date
date = datetime(2023, 5, 25)
start_date = datetime(1991, 1, 1)
end_date = datetime(2023, 12, 31)   

if is_date_in_range(date, start_date, end_date):
   print("Date is within the range.")
else:
   print("Date is outside the range.")