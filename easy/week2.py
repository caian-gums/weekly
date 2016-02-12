#caian 12/02/2016

def main_menu():
    print("(remember you can calculate the 'pseudo' values like described on option 1)")
    print(" 1 - F = m * a (m = F/a or a = F/m)")
    print(" 2 - U = R * i")
    print(" 3 - a^2 = b^2 * c^2")
    r = int(input("> "))
    return r

def fma():
    print("  what you want to know?\n  1 - F\n  2 - m\n  3 - a")
    o = int(input("> "))
    f = 0
    m = 0
    a = 0
    if o == 1:
        m = int(input("insert m\n> "))
        a = int(input("insert a\n> "))
        f = m * a
        print("F = " + str(f))
    elif o == 2:
        f = int(input("insert F\n> "))
        a = int(input("insert a\n> "))
        m = f / a
        print("m = " + str(m))
    elif o == 3:
        f = int(input("insert F\n> "))
        m = int(input("insert m\n> "))
        a = f / m
        print("a = " + str(a))

def uri():
    print("  what you want to know?\n  1 - U\n  2 - R\n  3 - i")
    o = int(input("> "))
    u = 0
    r = 0
    i = 0
    if o == 1:
        r = int(input("insert R\n> "))
        i = int(input("insert i\n> "))
        u = r * i
        print("U = " + str(u))
    elif o == 2:
        u = int(input("insert U\n> "))
        i = int(input("insert i\n> "))
        r = u / i
        print("R = " + str(r))
    elif o == 3:
        u = int(input("insert U\n> "))
        r = int(input("insert R\n> "))
        i = u / r
        print("i = " + str(i))

def a2b2c2():
    print("  what you want to know?\n  1 - a\n  2 - b\n  3 - c")
    o = int(input("> "))
    a = 0
    b = 0
    c = 0
    if o == 1:
        b = int(input("insert b\n> "))
        c = int(input("insert c\n> "))
        a = (b ** 2) + (c ** 2)
        a = a ** (0.5)
        print("a = " + str(a))
    elif o == 2:
        a = int(input("insert a\n> "))
        c = int(input("insert c\n> "))
        b = (a ** 2) - (c ** 2)
        b = b ** (0.5)
        print("b = " + str(b))
    elif o == 3:
        a = int(input("insert a\n> "))
        b = int(input("insert b\n> "))
        c = (a ** 2) + (b ** 2)
        c = c ** (0.5)
        print("c = " + str(c))

print("Pick something to calculate!")

op = main_menu()
if op == 1:
    fma()
elif op == 2:
    uri()
elif op == 3:
    a2b2c2()
    
print("bye!")
