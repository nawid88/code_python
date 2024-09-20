balance = int(input("Current Balance: "))
cookies_sold = input("Enter cookies sold: ")
money_made = 0
big_cookie = 0
small_cookie = 0

for cookie in cookies_sold:
    if cookie == "c" or cookie == "C":
        money_made = money_made + 1.25
        small_cookie = small_cookie + 1
    elif cookie == "b" or cookie == "B":
        money_made = money_made + 2.00
        big_cookie = big_cookie + 1
    

profit = money_made - ((big_cookie*0.75) + (small_cookie*0.50))
total_end = profit + balance

print(f"""
End of day Total: ${total_end}
Profit: ${profit}
""")

