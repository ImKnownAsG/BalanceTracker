from datetime import datetime
dt1 = datetime(2025, 1, 15, 10, 30, 0)
dt2 = datetime(2024, 5, 20, 14, 0, 0)
if dt1 == dt2:
    print("Dates are equivalent")
elif dt1 > dt2:
    print(f"{dt1} is after {dt2}")
else:
    print(f"{dt1} is before {dt2}")