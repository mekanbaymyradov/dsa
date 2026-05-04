# Expenses for every month January to May
expenses = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to to Jan?
print(f"1. In Feb you spent {expenses[1] - expenses[0]}$ more compare to Jan.")

# 2. Find out total expense in first three month.
print(f"2. Total sum of first three month is {sum(expenses[:3])}$")

# 3. Did you spend exactly 200$ in any month?
print(f"3. Did you spend exactly 200$ in any month? {2000 in expenses}")
# 4. June is finished and expense is 1980. Add this to expenses list.
expenses.append(1980)
print(f"3. {expenses}")

# 5. You returned an item that you bought in Apr and got a refund of 200$. Make a corecction.
expenses[3] -= 200
print(f"4. {expenses}") 


