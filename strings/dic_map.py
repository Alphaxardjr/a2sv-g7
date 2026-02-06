# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# Read all input lines
lines = sys.stdin.read().splitlines()

# First line = number of entries
n = int(lines[0])

# Build the phone book dictionary
phone_book = {}
for i in range(1, n+1):
    name, number = lines[i].split()
    phone_book[name] = number

# Process queries (remaining lines)
for query in lines[n+1:]:
    if query in phone_book:
        print(f"{query}={phone_book[query]}")
    else:
        print("Not found")
