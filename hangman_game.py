import random

def game():
    words=["component","carbon","planet","blood"]
    var1=random.choice(words).lower()
    alpha=[]
    chances = 6
    var3=["_"]*len(var1)
    print(" ".join(var3)) 
    while chances > 0 and "_" in var3:
        var=input("enter a letter:")
        if not var.isalpha():
            print("please enter letter only")
            continue
        if var in alpha:
            print("you already guess this letter")
            continue
        alpha.append(var)
        if var in var1:
            print("correct!")
            for i in range(len(var1)):
                if  var1[i]==var:
                    var3[i]=var
                    continue
        else:
            chances-=1
            print(f"Incorrect!,you have {chances} chances left")
            
        print(" ".join(var3)) 
    if "_" not in  var3 :
            print("Congratulation you won the game!!")
    else:
            print(f"Game over!!,the word was '{var1}")
if __name__ == "__main__":
    game()



