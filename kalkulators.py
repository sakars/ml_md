import calc
import sys

def throwErr(s):
    print(s)
    input("Press enter to exit program")
    exit()

def main():
    if not sys.argv[1].isnumeric():
       throwErr("Pirmais elements nav numerisks")
    if not sys.argv[3].isnumeric():
        throwErr("Otrais elements nav numerisks") 
    
    a=float(sys.argv[1])
    b=float(sys.argv[3])
    if sys.argv[2]=="+":
        print(calc.summa(a,b))
    elif sys.argv[2]=="-":
        print(calc.atnemsana(a,b))
    elif sys.argv[2]=="*":
        print(calc.multiplikacija(a,b))
    elif sys.argv[2]=="/":
        print(calc.dalisana(a,b))
    elif sys.argv[2]=="^":
        print(calc.eksponenta(a,b))
    else:
        throwErr("Nav valīda darbība")
    x=input("Press enter to exit program")
    #exit()

if __name__=="__main__":
    main()
