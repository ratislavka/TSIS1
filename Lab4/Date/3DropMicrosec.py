from datetime import datetime

# Define a datetime with microseconds
dt_with_microseconds = datetime.now()
print("Datetime with microseconds: ", dt_with_microseconds)

# Drop microseconds
dt_without_microseconds = dt_with_microseconds.replace(microsecond=0)
print("Datetime without microseconds: ", dt_without_microseconds)
