print("The Love Calculator is calculating your score...")
name1 = input("What is your name?") 
name2 = input("What is their name?") 

name1_upper = name1.upper()
name2_upper = name2.upper()

both_names = name1_upper + name2_upper

T = both_names . count("T")
R = both_names . count("R")
U = both_names.count("U")
E = both_names.count("E")
TRUE = T+R+U+E

L = both_names.count("L")
O = both_names.count("O")
V = both_names.count("V")
E = both_names.count("E")

LOVE = L+O+V+E

Score_Str = str(TRUE) + str(LOVE)

Score = int(Score_Str)


if Score < 10 or Score > 90:
  print(f"Your score is {Score}, you go together like coke and mentos.")
elif Score >= 40 and Score <= 50:
  print(f"Your score is {Score}, you are alright together.")
else:
  print(f"Your score is {Score}.")