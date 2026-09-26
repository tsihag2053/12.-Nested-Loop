print("=== ATM Cash Dispenser ===")
total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customers_served = 0
total_dispensed = 0

serving = True
while serving:
    name = input("Enter customer name: ")
    amount = int(input(f"Hello {name}! Enter the amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount. Please enter a positive number.\n")
        continue

    print(f"\nDispensing {amount} units for {name}:")
    remaining = amount
    idx = 1
    while idx <= 6 :
        if idx == 1: value = 100
        elif idx == 2: value = 50
        elif idx == 3: value = 20
        elif idx == 4: value = 10
        elif idx == 5: value = 5
        else: value = 1
        count = remaining // value
        if count > 0:
            print(f"{count} x {value} unit note(s) = {count * value}")
            remaining -= count * value
            if value == 100: total_100 += count
            elif value == 50: total_50 += count
            elif value == 20: total_20 += count
            elif value == 10: total_10 += count
            elif value == 5: total_5 += count
            else: total_1 += count

        idx += 1

    customers_served += 1
    total_dispensed += amount
    print(f"Transaction Complete, {name}!\n")
    again = input("Next Customer? (y/n): ").strip().lower()
    if again != 'y':
        serving = False

print("\n=== Daily Denomination Report ===")
for slot in range(1, 7):
    if slot == 1: value = 100; total = total_100
    elif slot == 2: value = 50; total = total_50
    elif slot == 3: value = 20; total = total_20
    elif slot == 4: value = 10; total = total_10
    elif slot == 5: value = 5; total = total_5
    else: value = 1; total = total_1
    if total > 0:
        print(f"{value} units notes dispensed: {total}" , end="")
        for note in range(total):
            print("=", end="")
        print()

print(f"\nTotal customers served: {customers_served}")
print(f"Total amount dispensed: {total_dispensed} units")
print("ATM session closed. Goodbye!")