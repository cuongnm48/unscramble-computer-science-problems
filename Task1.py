"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    differentNumbersInTexts = set()
    for x in texts:
        differentNumbersInTexts.update([x[0], x[1]])
    print(len(differentNumbersInTexts))

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    differentNumbersInCalls = set()
    for x in calls:
        differentNumbersInCalls.update([x[0], x[1]])
    print(len(differentNumbersInCalls))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
