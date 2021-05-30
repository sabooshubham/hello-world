# cook your dish here
withdraw, balance = input().split()
withdraw = int(withdraw)
balance = float(balance)
if withdraw % 5 == 0 and balance - withdraw - 0.50 >= 0:
    balance = balance - withdraw - 0.50
print('{:.2f}'.format(balance))