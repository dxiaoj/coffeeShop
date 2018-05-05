"""
  project name : L&J's coffee shop
  author: Jay
  date: 2018-05-06
  version: 0.0.3
  descriotion:
                1) add function order_detail to restore order detail for each customer
"""

# 记录每位顾客购买咖啡的过程中购买咖啡的种类与数量
def order_detail():
    coffee_order = {}
    coffee_No = input("\nchoose your coffee：")
    while True:
        if coffee_No not in coffee_order.keys():# 如果不在字典记录中，则新增一条记录
            if int(coffee_No) >= 1 and int(coffee_No) <= 4:
                coffee_amount = input("how many cups do you want?")
                coffee_order[coffee_No] = int(coffee_amount)
            else:
                print("sorry, what you choose is not here\n\n!")
        else:# 如果在字典记录中，则将加入新购数量
            coffee_amount = input("how many cups do you want?")
            coffee_order[coffee_No] += int(coffee_amount)

        coffee_No = input("\ndo you want more coffee? choose your coffee! or print Q for quit!")

        if coffee_No.upper() == "Q":
            break

    return coffee_order


