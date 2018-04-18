"""
  project name : L&J's coffee shop
  author: Jay
  date: 2018-04-18
  version: 0.0.2
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

while True:
    print("*****************************************************")
    print("*****************************************************")
    print("Welcome to the L&J's coffee shop!\n")
    print("do you want a cup of coffee(y/n)?")

    yes_no = input();

    if yes_no == "y":

        print("you are our No {} consumer today!".format(consumer_count))
        print( "1){} ${}".format(coffee1Name,coffee1Price),
               "\n2){} ${}".format(coffee2Name,coffee2Price),
               "\n3){} ${}".format(coffee3Name,coffee3Price),
               "\n4){} ${}".format(coffee4Name,coffee4Price))

        print("\nchoose your coffee：")

        coffee_No = input()

        if int(coffee_No) >= 1 and int(coffee_No) <= 4:

            coffee_Name = coffee_Names[coffee_No]

            print("how many cups do you want?")
            coffee_amount = input()
            price = coffee_Prices[coffee_No] * int(coffee_amount)
            print("OK! you choose {} cups of {}, you will pay ${}".format(coffee_amount, coffee_Name, price))

            print("please input your vip No (new vip will sumbit your No, but you can only have discount next time):")
            vip_No = input()
            if vip_No in vip_Nos:
                price *= 0.8
                print("\ncomfirmed!")
                print("you can have a 20% discount! you will pay ${}\n\n".format(price))
            else:
                vip_Nos.append(vip_No)
                print("congratuations! you are our VIP now! your VIP No is {}".format(vip_No))
                print("you can have a 20% discount next time. Now you will pay ${}\n\n".format(price))

            consume_info = [vip_No, coffee_Name, coffee_amount, price]
            total_consumer_info.append(consume_info)
            consumer_count += 1

        else:
            print("sorry, what you choose is not here\n\n!")

    else:
        print("bye bye!\n\n")

    if consumer_count >= 20:
        print("We are closed today! Welcome back tomorrow!\n\n")
        break


