"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('calls.csv', 'r') as f:
  reader = csv.reader(f)
  calls = list(reader)
  numberArr = {}
  for c in calls:
      if c[0] in numberArr:
        numberArr[c[0]] += int(c[3])
      else:
        numberArr[c[0]] = int(c[3])
      if c[1] in numberArr:
        numberArr[c[1]] +=int(c[3])
      else:
        numberArr[c[1]] = int(c[3])
  telephoneNumber = max(numberArr, key=numberArr.get)
  print(f"{telephoneNumber} spent the longest time, {numberArr[telephoneNumber]} seconds, on the phone during September 2016.")


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

