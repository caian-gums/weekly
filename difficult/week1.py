# caian 14/02/2016

print("Pick a number between 1 - 100.")
found = False
n = 50
guess = n
options = ['h', 'l', 'i']
valid = True
while not found:
    print("It is (h)igher from, (l)ower from, or it (i)s " + str(guess))
    o = input("> ")
    if o[0] in options:
        n = abs(int(n/2))
        if n == 0: n = 1
        if o[0] == 'i': found = True
    else:
        print("plz, pick a valid option")
        valid = False

    if valid and not found:
        if o[0] == 'l': n = - n
        guess = guess + n
    valid = True

    if guess > 100 or guess < 1:
        print("That's not a possible number. Pick another.")
        n = 50
        guess = n

print("bye!")
