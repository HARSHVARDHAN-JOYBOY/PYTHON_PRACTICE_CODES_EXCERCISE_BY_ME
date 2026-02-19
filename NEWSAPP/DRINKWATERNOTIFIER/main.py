import time
from plyer import notification
while True:
    print("You need to drink some water ! ")
    notification.notify(title="Water Remainder !!! ",message="You Need To Drink Some Water !!! ",)
    time.sleep(3)
