# comp163_assignment_5.py

# === Challenge 1: Collatz Conjecture ===
print("=== Challenge 1: Collatz Conjecture ===")
current_num = int(input("Enter starting number: "))
step_count = 0

# Print starting num first
print("Sequence:", end=" ")
print(current_num, end=" ")

# Special case: if input is 1, sequence ends immediately
if current_num == 1:
    print("Steps: 0")
else:
    # Keep running sequence until we hit 1
    while current_num != 1:
        if current_num % 2 == 0:       # even → divide by 2
            current_num //= 2
        else:                             # odd → 3n + 1
            current_num = 3 * current_num + 1
        print(current_num, end=" ")
        step_count += 1
    print()
    print(f"Steps: {step_count}")

# === Challenge 2: Prime Num Checker ===
print("\n=== Challenge 2: Prime Number Checker ===")
n = int(input("Enter a number: "))
print(f"Testing divisors from 2 to {n-1}...")

prime = True
divisor_found = None

# Test all nums from 2 up to n-1
for d in range(2, n):
    if n % d == 0:        # found a divisor
        prime = False
        divisor_found = d
        break

if prime:
    print(f"{n} is prime!")
else:
    print(f"{n} is not prime (divisible by {divisor_found})")

# === Challenge 3: Multiplication Table Grid ===
print("\n=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")

# Header row
print("    ", end="")
for col in range(1, 11):
    print(f"{col:4}", end="")
print()

# Table body
for row in range(1, 11):
    print(f"{row:2} ", end="")     # row label
    for col in range(1, 11):
        print(f"{row*col:4}", end="")  # product
    print()
