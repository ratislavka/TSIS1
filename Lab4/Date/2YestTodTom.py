from datetime import datetime, timedelta

current = datetime.now()
yest = current - timedelta(days = 1)
tom = current + timedelta(days = 1)

print('Yesterday: ' , yest)
print('Today: ' , current)
print('Tomorrow: ' , tom)