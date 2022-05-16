import random

def Generate_Operation_List():
    with open("Company_1_Operation_List.txt", "w") as f:
        for row in range(4):
            randNum = random.randint(0, 1)
            if randNum == 0:
                f.write("Operation A\n")
            else:
                f.write("Operation B\n")

    with open("Company_2_Operation_List.txt", "w") as f:
        for row in range(3):
            f.write("Operation C\n")