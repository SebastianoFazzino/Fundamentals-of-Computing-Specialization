import random
def powerball():
        
    your_nums = []
    i = 0
#using a while loop, we get the player to input 6 numbers
    while i < 6:
       Nums = input("Enter your numbers here: ")
       if int(Nums) not in your_nums:
          your_nums.append(int(Nums))
          i += 1
       else:
           continue
          
#we generate 6 random winning numbers  
    numbers = []
    i = 0
    while i < 5:
        num = random.randrange(1,60)
        if num not in numbers:
            numbers.append(num)
            i += 1
        else:
            continue
    while i < 6:
        power_num = random.randrange(1,36)
        if power_num not in numbers:
            numbers.append(power_num)
            i += 1
        else:
            continue
    #we print out the winning numbers
    print ("Winning numbers are: {},{},{},{},{}, Powerball number is: {}".format(numbers[0],
                                                                                 numbers[1],
                                                                                 numbers[2],
                                                                                 numbers[3],
                                                                                 numbers[4],
                                                                                 numbers[5]))
    
    
    #we check how many numbers has the player guessed
    guessed_nums = []
    for num in your_nums:
        if num in numbers:
            guessed_nums.append(num)
            
    print("You guessed", len(guessed_nums), "numbers!")
    
    
    if len(guessed_nums) <= 2:
        print("Bummer, you'll be luckier next time!")
    elif len(guessed_nums) >= 3 and len(guessed_nums) < 5:
        print("Wow! Not bad at all!!!")
    elif len(guessed_nums) == 5:
        print("Amazing! You almost did jackpot!!!")
    else:
        print("*****CONGRATULATIONS, YOU DID JACKPOT*****")
    
  
#we call the function
powerball()