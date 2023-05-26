import time
import random

int1 = 0
int2 = 9
level = 1
points = 10
print("You have", points, "points to being with. With each correct answer, you will gain 10 points, and with each wrong answer, you will lose 10 points. (Additional 5 points if answered under 5 seconds) Game over when you lose all points or level up when you reach 100 points.")
while points > 0:
    x1 = random.randint(int1,int2)
    x2 = random.randint(int1,int2)

    starttime = time.time()
    print("What is ", x1, "times ", x2, "?")
    useranswer = int(input("Your Answer is:"))
    actualanswer = x1 * x2
    answertime = round((time.time()-starttime), 2)
    print("Your answer time is", answertime, "seconds.")

    if useranswer == actualanswer:
        points = points + 10
        if answertime < 5:
            points = points + 5
        else:
            points = points
        print("Nice. You now have ", points, "points.")
    else:
        points = points - 10
        print("Wrong answer. You now have ", points, "points.")

    if points % 100 == 0:
        int1 += 3
        int2 += 3
        level += 1
        print("Congratulations, You have reached", points, "points. You levelled up to level", level,)
else:
    print("You have 0 points. Game Over.")