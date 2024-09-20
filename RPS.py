p1 = (input("player 1 choice R/P/S: ")).lower()
p2 = (input("player 2 choice R/P/S: ")).lower()

if p2 == "r" and p1 == "r":
    print("Draw")
elif p2 == "p" and p1 == "p":
    print("Draw")
elif p2 == "s" and p1 == "s":
    print("Draw")
elif p2 == "r" and p1 == "p":
    print("player 1 wins")
elif p2 == "p" and p1 == "r":
    print("player 2 wins")
elif p2 == "r" and p1 == "s":
    print("player 2 wins")
elif p2 == "s" and p1 == "r":
    print("player 1 wins")
elif p2 == "p" and p1 == "s":
    print("player 1 wins")
elif p2 == "s" and p1 == "p":
    print("player 2 wins")

