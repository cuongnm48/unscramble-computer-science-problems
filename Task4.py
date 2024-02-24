"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    numberTelephoneMarketing = set()
    numberSendOrReciveTextOrReciveIncomingCalls = set()

    for t in texts:
        numberSendOrReciveTextOrReciveIncomingCalls.update({t[0], t[1]})
    for c in calls:
        numberSendOrReciveTextOrReciveIncomingCalls.add(c[1])
    for c in calls:
        if c[0] not in numberSendOrReciveTextOrReciveIncomingCalls:
            numberTelephoneMarketing.add(c[0])
    sortNumber = sorted(numberTelephoneMarketing)
    print("These numbers could be telemarketers: ")
    for n in sortNumber:
        print(n)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

