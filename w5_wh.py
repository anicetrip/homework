# Marked Exercise 1 (1 mark):
# Ask the user to enter their name and a number.
# If the number is less than 10,
# then display their name that number of times.
# Otherwise display the message “Too high” three times.

# name, number = input("Give me your name and a number \n")\
#     .split()
# number_int = int(number)
# if number_int <= 10:
#     for i in range(0,number_int):
#         print(name)
# elif number_int <= 10:
#     print("too low")
# else:
#     print("too high")


# Marked Exercise 2 (1 mark):
# Ask the user which direction
# then want to count (up or down).
# If they select up,
# then ask them for the top number
# and then count from 1 to that number.
# If they select down,
# ask them to enter a number below 20
# and then count down from 20 to that number.
# If they entered something other than up or down,
# display the message “I don’t understand”.
# Your program should allow the user to enter up or down
# in lowercase, uppercase or titlecase.

# while True:
#     s = input("What's the number direction, up or down? \n")
#     top = int(input("enter top number \n"))
#     low = 20
#     start = 0
#     end = 0
#     step = 1
#     if s == "down":
#         while low >= 20 or low >= top:
#             low = int(input("enter a number below 20 \n"))
#             if low >= 20 or low >= top:
#                 print("Your number is too high")
#                 continue
#         start = top
#         end = low
#         step = -1
#     elif s == "up":
#         start = 1
#         end = top
#         step = 1
#     else:
#         print("mistake input")
#         break
#     for i in range(start, end + step, step):
#         print(i)
#
#     break


# Marked Exercise 3 (1 mark):
# capacity = int(input("how many people can fit into their apartment?\n"))
# amount = 1
# while amount <= capacity:
#     guest_name = input("who would yuo invite?\n")
#     print(guest_name + " has now been invited")
#     amount += 1
#     boolean = input("would you ask anyone else?\n")
#     if boolean != "yes":
#         break
# print("There are " + str(amount)+ "people")



flag = 0
while True:
    print("Welcome to Limerick City Your mission is to have a \ngreat night out with your friends, after losing them \nYou see the castle doors open")
    while True:
        q1 = input("Go inside or walk past, yes(Go inside) or no(walk past)?\n").lower()
        if q1 == "yes":
            print("There is a building work inside, you fall into a hole, game over.\n")
            flag = 1
            break
        elif q1 != "no":
            print("wrong input, you didn't go inside, and just walk past.")
        print("You reach treaty city brewery.")
        q2 = input("Go inside or walk past, yes(Go inside) or no(walk past)?\n").lower()
        if q2 == "yes":
            print("You have a great time, making new friends and drinking beer"
                  "Mark and aisling are upset that you abandoned them and "
                  "never speak to you again."
                  "Game over\n")
            break
        elif q2 != "no":
            print("wrong input, you didn't go inside, and just walk past.")
        print("You reach the intersection a t Nicholas St.")
        print("which direction are you taking?")
        s = input("you can go left(l),right(r),straight ahead(s) or anywhere else, where would you want to go?\n")
        if s == "l" | s == "left":
            print("you walk around corbally for a while and get lost. Hours later, you get a call from your aisling,"
                  "they were looking for you but went home."
                  "Game over.\n")
        elif s == "r":
            print("You bump into Aisling and Mark at the locke bar and have a great time with them")
            flag = 1
        elif s == "s":
            print("There's nothing here, you are very boring and go home."
                  "Go over\n")
        else:
            print("This is ridiculous, they should really be looking for you. "
                  "You go home, game over.\n")
        break
    if flag == 1:
        break
