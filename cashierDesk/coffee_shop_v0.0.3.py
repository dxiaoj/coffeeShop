"""
  project name : L&J's coffee shop
  author: Jay
  date: 2018-05-06
  version: 0.0.6
  descriotion:
                1) add function order_detail to restore order detail for each customer
                2) add function money_for_order to calculate the whole price
                3) add function order_print to print order
                4) add function order_log to restore the order log
                5) add function main to run the codes
"""

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
def money_for_order(coffee_od_dic, coffee_Prices):
    total_money = 0
    for coffee_No, coffee_amount in coffee_od_dic.items():
        total_money += coffee_Prices[coffee_No]*coffee_amount

    return total_money

# 打印订单
def order_print(coffee_od_dic, coffee_Names, coffee_Prices):
    print("here is your order:")
    for coffee_No, coffee_amout in coffee_od_dic.items():
        print("{} cups of {} ".format(coffee_amout, coffee_Names[coffee_No]))

    print("here is your bill:\n${}".format(money_for_order(coffee_od_dic, coffee_Prices)))

# 订单记录
def order_log(coffee_od_dic,vip_no,total_consumer_record, coffee_Prices):
    for coffee_No, coffee_amount in coffee_od_dic.items():
        one_record = {}
        one_record['vip_no'] = vip_no
        one_record['coffee_no'] = coffee_No
        one_record['coffee_amount'] = coffee_amount
        one_record['coffee_bill'] = money_for_order(coffee_od_dic, coffee_Prices)
        total_consumer_record.append(one_record)
    return total_consumer_record

def main():

    coffee_Names = {"1": "black coffee", "2": "Cappuccino", "3": "Latte", "4": "Espresso"}
    coffee_Prices = {"1": 20, "2": 25, "3": 24, "4": 18}

    vip_dic = {}

    consume_info = []

    consumer_count = 1

    while True:
        print("*****************************************************")
        print("*****************************************************")
        print("Welcome to the L&J's coffee shop!\n")
        print("do you want a cup of coffee(y/n)?")

        yes_no = input()
        if yes_no == "y":
            print("you are our No {} consumer today!".format(consumer_count))
            i = 1
            for coffee_No, coffee_Name in coffee_Names.items():
                print("{}) {} ${}".format(i, coffee_Name, coffee_Prices[coffee_No]))
                i += 1

            coffee_order_dic = order_detail()                               # 购买过程
            order_print(coffee_order_dic, coffee_Names, coffee_Prices)      # 打印订单
            price = money_for_order(coffee_order_dic, coffee_Prices)        # 总价

            # 检查是否为会员
            vip_No = input("please input your vip No (new vip will sumbit your No, but you can only have discount next time):")
            if vip_No in vip_dic:
                price *= 0.8
                print("\ncomfirmed!")
                print("you can have a 20% discount! you will pay ${}\n\n".format(price))
            else:
                vip_tel = input("you are not vip yet! please input your tel to become vip:")
                vip_dic[vip_No] = vip_tel
                print("congratuations! you are our VIP now! your VIP No is {}".format(vip_No))
                print("you can have a 20% discount next time. Now you will pay ${}\n\n".format(price))

            consume_info.append(order_log)
            consumer_count += 1

        else:
            print("bye bye!\n\n")  # so why do you come here?!

        if consumer_count >= 20:
            print("We are closed today! Welcome back tomorrow!\n\n")
            break

main()