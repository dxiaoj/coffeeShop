"""
  project name : L&J's coffee shop
  author: Jay
  date: 2018-05-06
  version: 0.0.3
  descriotion:
                1) add function order_detail to restore order detail for each customer
                2) add function money_for_order to calculate the whole price
"""


coffee1Name = "black coffee"
coffee1No = "1"
coffee1Price = 20
coffee2Name = "Cappuccino"
coffee2No = "2"
coffee2Price = 25
coffee3Name = "latte"
coffee3No = "3"
coffee3Price = 24
coffee4Name = "Espresso"
coffee4No = "4"
coffee4Price = 18

coffee_Names = { "1" : "black coffee" , "2" : "Cappuccino" , "3" : "Latte" , "4" : "Espresso" }
coffee_Prices = { "1" : 20 , "2" : 25 , "3" : 24 , "4" : 18 }

vip_Nos = ['20180001',
           '20180002',
           '20180003',
           '20180004',
           '20180005',
           '20180006']

total_consumer_info = []

consumer_count = 1


# 记录每位顾客购买咖啡的过程中购买咖啡的种类与数量
def order_detail():
    coffee_order_dic = {}
    coffee_No = input("\nchoose your coffee：")
    while True:
        if coffee_No not in coffee_order_dic.keys():# 如果不在字典记录中，则新增一条记录
            if int(coffee_No) >= 1 and int(coffee_No) <= 4:
                coffee_amount = input("how many cups do you want?")
                coffee_order_dic[coffee_No] = int(coffee_amount)
            else:
                print("sorry, what you choose is not here\n\n!")
        else:# 如果在字典记录中，则将加入新购数量
            coffee_amount = input("how many cups do you want?")
            coffee_order_dic[coffee_No] += int(coffee_amount)

        coffee_No = input("\ndo you want more coffee? choose your coffee! or print Q for quit!")

        if coffee_No.upper() == "Q":
            break

    return coffee_order_dic

# 记录总价
def money_for_order(coffee_od_dic):
    total_money = 0
    for coffee_No, coffee_amount in coffee_od_dic.items():
        total_money += coffee_Prices[coffee_No]*coffee_amount

    return total_money


def main():

    print("your will pay {}".format(money_for_order(order_detail())))

main()