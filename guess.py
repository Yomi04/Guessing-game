import random
#generate a random number
random_number = random.randint(1,5)

while True:
    try:     
        user_input = int(input('Please enter a number: '))
        if 0 < user_input < 6:
        #check if user number and random number are equal
            if random_number == user_input:
                print('you are a genius!')
                break
            else:
                pass
        else:
            print('Please enter a number between 1-5 ')
    except ValueError:
         print('Only numbers are allowed')  
         continue 





