"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    isCalledNumber = set()
    totalCallFrom080 = 0
    totalCalledNumberStartWith080 = 0

    for c in calls:
      if c[0].startswith("(080)"):
        totalCallFrom080 +=1
        if "(" and ")" in c[1]:
          start_index = c[1].find('(')
          end_index = c[1].find(')')
          isCalledNumber.add(c[1][start_index:end_index + 1])
          if c[1].startswith("(080)"):
            totalCalledNumberStartWith080 +=1
        elif c[1].startswith("7") or c[1].startswith("8") or c[1].startswith("9"):
            isCalledNumber.add(c[1][:4])
        elif c[1].startswith("140"):
          isCalledNumber.add("140")
    print("The numbers called by people in Bangalore have codes:")
    sortIsCalledNumber = sorted(isCalledNumber)
    for n in sortIsCalledNumber:
        print(n)
    print(f"{round((totalCalledNumberStartWith080 / totalCallFrom080 * 100), 2)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
