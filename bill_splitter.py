#Iradukunda Aline
#221018616
#Computer Science
import random

a = input("Enter the number of friends joining (including you):\n")
number = int(a)
friends_dict = {}

if number > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(number):
        names = input()
        friends_dict.update({names: 0})
    
print("Enter the total bill value:")
x = input()
bill = int(x)
split = int(bill) / number
for key, value in friends_dict.items():
    friends_dict[key] = round(split, 2)

print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
choice = input()
if choice == "yes":
    lucky_friend = random.choice(list(friends_dict))
    print(lucky_friend, " is the lucky one!")

    remaining = bill / (number - 1)

    for key, value in friends_dict.items():
        if key == lucky_friend:
            friends_dict[lucky_friend] = 0
        else:
            friends_dict[key] = round(remaining, 2)
else:
    print("No one is going to be lucky")

print(friends_dict)
