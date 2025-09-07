#FutureTime.py
#Name:Jadon Wiebe
#Date:9/07/2025
#Assignment:FutureTime

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  #TODO:
  #Ask user for hours
  number_of_hours=int(input("Give me a number of hours: "))
  #Ask user for minutes
  number_of_minutes=int(input("Give me a number of minutes: "))

  #Calculate the time after the user-supplied time has passed.
  New_Hours = ((currentHour + number_of_hours + (number_of_minutes // 60)) % 12)
  New_Minutes = (currentMinute + (number_of_minutes % 60))
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print (str(New_Hours) + ":" + str(New_Minutes))

if __name__ == '__main__':
  main()
