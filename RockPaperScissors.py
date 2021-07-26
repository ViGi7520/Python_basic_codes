import random

#p1 = random.randint(1,3)
#p2 = random.randint(1,3)

print("""
Rock=1
Paper=2
Scissors=3
          """)
p1 = int(input('Select your move p1:-'))
p2 = int(input('Select your move p2:-'))

rock = 1
paper = 2
scissors = 3

if p1 == rock and p2 == scissors:
  print("p1 wins, rock beats scissors")
elif p1 == scissors and p2 == paper:
  print("p1 wins, scissors beats paper")
elif p1 == paper and p2 == rock:
  print("p1 wins, paper beats rock")
if p2 == rock and p1 == scissors:
  print("p2 wins, rock beats scissors")
elif p2 == scissors and p1 == paper:
  print("p2 wins, scissors beats paper")
elif p2 == paper and p1 == rock:
  print("p2 wins, paper beats rock")
elif p1 == p2 and p1 == rock:
  print("tie, both have rock")
elif p1 == p2 and p1 == paper:
  print("tie, both have paper")
elif p1 == p2 and p1 == scissors:
  print("tie, both have scissors")