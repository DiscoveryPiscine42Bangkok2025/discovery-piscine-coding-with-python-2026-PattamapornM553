n = input("Give me a number: ")
n = float(n)
rounded_up = round(n)

if n > rounded_up:
    print(rounded_up + 1)
else:
    print(int(n))