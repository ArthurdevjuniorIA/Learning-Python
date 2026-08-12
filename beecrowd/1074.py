N = int(input())

for i in range(N):

    X = int(input())

    if X == 0:
        print("NULL")

    
    elif X % 2 == 0 and X > 0:
        print("EVEN POSITIVE")

    elif X % 2 == 0 and X < 0:
        print("EVEN NEGATIVE") 
  
    elif X % 2 != 0 and X > 0:
        print("ODD POSITIVE")

    else:
        print("ODD NEGATIVE") 