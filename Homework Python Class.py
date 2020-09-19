pay = int(input("How much did you spend at the store? "))

if pay >= 60:
    print("You get 30 percent off!")
    percent_off1 = pay * .3
    total = (pay - percent_off1)
    print("Total: " + str(total))

elif pay >= 50 and pay < 60:
    print("You get 25 percent off!")
    percent_off1 = pay * .25
    total = (pay - percent_off1)
    print("Total: " + str(total))

elif pay < 50:
    print("You get 20 percent off!")
    percent_off1 = pay * .2
    total = (pay - percent_off1)
    print("Total: " + str(total))