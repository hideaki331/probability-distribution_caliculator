def Facto(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*Facto(n-1)

def combination(n,k):
    return int(Facto(n)/(Facto(k)*Facto(n-k)))

def Binomal(n,k,p):
    p_i = float_to_int(p)
    return combination(n,k)*(p_i**k)*(1*(p_i//p)-p_i)**(n-k)/(p_i//p)

def float_to_int(p):
    while(p.is_integer()):
        p *= 10
    return p

def separation_line():
    print("")
    print("="*20)
    print("")

def say_Hello():
    Hello = "# Hello,world! #"
    print("#"*(len(Hello)))
    print(Hello)
    print("#"*(len(Hello)))
    print("")
    print("Exit: q, Start: Anykey ")

if __name__ == "__main__":
    say_Hello()
    command = input("Enter Command:")
    while(command != "q"):
        try:
            separation_line()
            print("Binomal:")
            print("nCk p^k (1-p)^(n-k)")
            n = int(input("all n: "))
            k = int(input("select k: "))
            if n < k:
                print("please: n>k or n=k")
            else:
                p = float(input("probability p: "))
                print("result: "  + str(Binomal(n,k,p)))
                print("="*20)
        except ValueError:
            print("Please Enter: int for n,k and float for p")
        separation_line()
        print("Exit: q, Start: Anykey ")
        command = input("Enter Command:")
    print("....End.....")
    