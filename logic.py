import random

def pickup(cards):
    output = cards[random.randint(0, 9)]
    return output

def dealer_turn(dSum, uSum):
    while dSum < 17:    # this means the dealer still needs to pickup cards 
        dSum = dSum + pickup(cards)
        print("dealer sum: ", dSum)
    if dSum > 21: 
        print("dealer busts")
    elif 17 <= dSum <= 21:
        if dSum > uSum: 
            print("dealer wins")
        elif dSum < uSum: 
            print("player wins")
        else:
            print("you push")

    

    # this means the dealer has at least 17

# if dSum > 21: player wins 
# if dSum >= 17 and <= 21 
# if dSum > uSum then dealer wins 
# if dSum < uSum then player wins 
# if dSum == uSum then draw



cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True: 
    uCard_1 = pickup(cards)
    uCard_2 = pickup(cards)
    print("Your hand: ", uCard_1, uCard_2)

    uSum = uCard_1 + uCard_2
    print("Your sum: ", uSum)

    dCard_1 = pickup(cards)
    dCard_2 = pickup(cards)
    print("Dealer's hand: ", dCard_1, dCard_2)

    dSum = dCard_1 + dCard_2
    print("Dealer's sum: ", dSum)


    while uSum <= 21:
        choice = input("what do you want to do? (hit/stand/double) ")
        if choice == "hit":
            uCard_3 = pickup(cards)
            print("card3 drawn: " + str(uCard_3) ) 
            uSum = uSum + uCard_3
            print("Your hand: ", uSum)

        if uSum > 21:
            print("you lose")
            print("dealer had" + str(dSum))
            break
        
        if choice == "stand":
            dealer_turn(dSum, uSum)
            break
    play_again = input("deal cards again? (yes, no)") 
    if play_again == "no":
        break   
        
        # if uSum > dSum: 
        #     print("you win")
        #     print("dealer had" + str(dSum))
        #     break
        # elif uSum < dSum:
        #     print("you lose")
        #     print("dealer had" + str(dSum))
        #     break   
        # else:
        #     print("tie")
        #     print("dealer had" + str(dSum))
            
            


