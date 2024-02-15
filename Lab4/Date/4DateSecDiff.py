from datetime import datetime

# Define two dates
date1 = datetime(2024, 2, 10, 19, 23, 19)
date2 = datetime(2024, 2, 15, 19, 23, 19)

# Calculate the difference between the two dates
difference = date2 - date1

# Convert the difference to seconds
difference_in_seconds = difference.total_seconds()

print("Difference in seconds: ", difference_in_seconds)


'''
from datetime import datetime, timedelta

current = datetime.now()
yest = current - timedelta(days = 1)

diff = input()

print('Difference in seconds: ' , diff)
'''