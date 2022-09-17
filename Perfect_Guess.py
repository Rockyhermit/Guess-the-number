import random

class Guess:
    def guess(self):
        x = 5
        n = random.randint(1,100)
        # print(n)
        i = 1
        while x == 5:
            a = int(input("Enter any Integer as your Guess: "))
            
            if a > n:
                print("Lower please")
            elif a < n:
                print("Higher please")
            elif a == n:
                print(f"Congratulations Perfect Guess!!!\nIt took you {i} Guesses for the Perfect Guess\n\n") 
                break

            i = i + 1


k = Guess()
k.guess()

