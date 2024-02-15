from datetime import datetime, timedelta

current = datetime.now()

five_ago = current - timedelta(days = 5)

print(five_ago)



#import datetime

#current_date = datetime.date.today()
#new_date = current_date - datetime.timedelta(days=5)

#print(new_date)
