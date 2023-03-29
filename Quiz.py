print("Welcome to the Talent Quiz!")

playing = input ("Do you want to play ?")
if playing.upper() != "YES":
 quit()
print("Welcome")
score = 0
answer = input("Which planet has the most moons? ")
if answer.lower() == "saturn":
    print("Correct Ans")
    score += 1
    score = score+1
else:
    print("Wrong Ans")
answer = input("Which planet in the Milky Way is the hottest?")
if answer.lower() == "venus":
    print("Correct Ans")
    score += 1
else:
   print ("Wrong Ans")
answer = input("What is the name of the galaxy we live in ?")
if answer == "the milky way galaxy":
    print("Correct Ans")
    score += 1
else:
    print("Wrong Ans")
answer = input("which galaxy is closest to the earth ?")
if answer.lower() == ("canis major dwarf galaxy"):
        print("Correct Ans")
        score += 1
else:
    print("Wrong Ans")

print("you got" +  str("score") + "questions correct!" )
print("you got" +  str(("score / 4")  100) + "%." )