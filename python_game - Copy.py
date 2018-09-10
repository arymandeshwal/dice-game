import random
import operator

def roll_a_die():
    return random.randint(1,6)

def even_odd(n):
    if (n%2 ==0):
        return True
    else:
        return False

def main():

    player_1_name = str(input("player 1\nenter name:"))
    player_2_name = str(input("player 2\nenter name:"))

    i = 1
    player_1_score = 0
    player_2_score = 0
    die_1 =0
    die_2 =0
    round_score_1 =0
    round_score_2 =0
    
    while(i<=5):

        print("----------------------------------------------------------------")
        print("Round: "+str(i))
        print("----------------------------------------------------------------")




        die_1 = roll_a_die()
        die_2 = roll_a_die()

        print(player_1_name+" Rolled :"+ str(die_1)+" & "+str(die_2))

        round_score_1 = die_1 + die_2

        if even_odd(die_1+die_2):
            round_score_1 += 10
        else:
            round_score_1 -= 5
        if die_1 == die_2:
            extra_roll = roll_a_die()
            print(player_1_name+" Extra Roll"+str(extra_roll))
            round_score_1 += extra_roll

        player_1_score += round_score_1

        if player_1_score <0:
            player_1_score =0
    
        print(player_1_name+" Scored :"+str(round_score_1))
        




        die_1 = roll_a_die()
        die_2 = roll_a_die()

        print(player_2_name+" Rolled :"+ str(die_1)+" & "+str(die_2))

        round_score_2 = die_1 + die_2

        if even_odd(die_1+die_2):
            round_score_2 += 10
        else:
            round_score_2 -= 5
        if die_1 == die_2:
            extra_roll = roll_a_die()
            print(player_2_name+" Extra Roll"+str(extra_roll))
            round_score_2 += extra_roll

        player_2_score += round_score_2

        if player_2_score <0:
            player_2_score =0


        print(player_2_name+" Scored :"+str(round_score_2))
        

        print("\nTOTAL SCORE:-")

        print(player_1_name+"\t"+str(player_1_score))
        print(player_2_name+"\t"+str(player_2_score))


        i+=1

    i =1
    while (player_1_score == player_2_score):
        print("BONUS ROUND:"+ str(i))

        die_1 =roll_a_die()
        die_2 = roll_a_die()

        print("player 1 rolls :"+str(die_1))
        print("player 2 rolls :"+str(die_2))

        
        player_1_score += die_1
        player_2_score += die_2

        print("T_player 1 :"+str(player_1_score))
        print("T_player 2 :"+str(player_2_score))

        i+= 1

    f1 = open("LeaderBoard.txt","a")

    if (player_1_score > player_2_score):
        print(player_1_name+" is the Winner")
        f1.write(player_1_name+" - "+str(player_1_score)+'\n')
    else:
        print(player_2_name+" is the Winner")

        f1.write(player_2_name+" - "+str(player_2_score)+'\n')
    f1.close()

    f1= open("LeaderBoard.txt","r+")
    f1.seek(0)
    scores = f1.readlines()

    player_scores ={}
    for line in scores:
        name,score = line.rstrip('\n').split(' - ')
        score = int(score)
        if name not in player_scores or player_scores[name] < score:   # if the same person plays twice
            player_scores[name] = score

    sorted_player_scores = sorted(player_scores.items(), key=operator.itemgetter(1),reverse =True)

    count =0
    print("\nthe top 5 scores are :\n")
    for i in sorted_player_scores:
        if count < 5:
            print(i[0],i[1])
        count += 1
        


main()
