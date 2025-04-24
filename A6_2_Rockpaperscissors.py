import random
class Rock_Paper_Scissors:
    options=['r', 'p', 's']
    
    def game(self,totalnum):
        curnum=0
        win=0
        while curnum<totalnum:
            comp=random.choice((self.options))
            play=input(f"Enter your choice for {curnum+1}: ")
            if play not in self.options:
                print("INVALID!! Enter the correct option")
                continue
            if((play=='r' and comp=='s')or(play=='p' and comp=='r')or(play=='s' and comp=='p')):
                print(f"You win this round! Computer chose {comp}.")
                win+=1
            elif play == comp:
                print(f"It's a tie! Both chose {comp}.")
                curnum-=1 
            
            else: 
                print(f"You lose this round! Computer chose {comp}.") 
            curnum+=1
        return win

totalnum=int(input("Enter the total number of rounds: "))
player=Rock_Paper_Scissors()
result=player.game(totalnum)
print("Your total wins: ",result)




