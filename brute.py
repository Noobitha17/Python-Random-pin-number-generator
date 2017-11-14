import random
t=[]
class brute:

    def __init__(self):

        print("A simple brute force program developed by PAPU")
        self.b=int(input("\nEnter the starting range  "))
        self.c=int(input("\nEnter the ending value    "))
        self.d=int(input("\nHow many combination do you want   "))
        if int(self.d)>int(self.c-self.b):
            print("\nThe no of combination is more than possible sample outcomes","The possible outcome are ",int(self.c-self.b))
            exit(100)

        for a in range(1, self.d+1 ,1 ):
                self.a1=random.randrange(self.b,self.c,1)
                print(   "","","",self.a1)



b=brute()


