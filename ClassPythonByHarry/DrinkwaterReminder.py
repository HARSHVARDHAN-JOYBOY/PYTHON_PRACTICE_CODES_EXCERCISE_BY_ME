import time
from plyer import notification
import winsound

while True:
    # print("Sip Some Water !")
    notification.notify(title="Water Reminder" , message="Drink some water")
    winsound.Beep(1000, 500)
    time.sleep(10)
