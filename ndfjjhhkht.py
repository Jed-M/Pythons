count = 0
for x in range(1, 11):
    if x % 2 == 0:
        count += 1 
        print(x)
print(f"We have {count} even numbers.")