#pengulangan while


print("\n---pengulangan while---")
h = 1
while (h <= 100):
    if (h % 3 == 0 & h % 5 == 0):
        print("fizz bazz")
    elif (h % 3 == 0):
        print ("fizz")
    elif (h % 5 == 0 ):
        print("bazz")
    else:
        print(h)
    h += 1
print("\n---akhir pengulangan while---")