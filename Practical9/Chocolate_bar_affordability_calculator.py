def ChocolateNum(total_money, price):
    if total_money >= price:
        num = total_money // price
        left_money = total_money % price
        return num, left_money
    else:
        return 0, total_money
    
#Example
total_money = 100
price = 7
num, left_money = ChocolateNum(total_money, price)
print(num, left_money)
