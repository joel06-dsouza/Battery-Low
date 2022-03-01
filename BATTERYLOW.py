# cook your dish here
while True:
    try:
        t = input()
        while(t):
            x = int(input())
            if(x <= 15):
                print("Yes")
            else:
                print("No")
    except EOFError:
        break