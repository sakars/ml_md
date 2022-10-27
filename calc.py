#!/usr/bin/env python3

## 1. uzdevums 
## TODO uzraksti funkciju ar nosaukumu "summa" un izveidot loģiku
''' Funkcija summe divus skaitļus.

    input: divi float argumenti 
    
    output: summas vērtība
            (return 0 var izdzēst)
'''
def summa(a,b):
    return a+b
    

## 2. uzdevums
## TODO uzraksti funkciju ar nosaukumu "atnemsana" un izveidot loģiku
''' Funkcija, kas atņem divus skaitļus.

    input: divi float argumenti 
    
    output: atņemšanas vērtība
'''
def atnemsana(a,b):
    return a-b

## 3. uzdevums
## TODO uzraksti funkciju ar nosaukumu "multiplikacija" un izveidot loģiku
''' Funkcija, kas multiplicē divus skaitļus.

    input: divi float argumenti 
    
    output: multiplicēšanas vērtība
'''
def multiplikacija(a,b):
    return a*b

## 4. uzdevums
## TODO uzraksti funkciju ar nosaukumu "dalisana" un izveidot loģiku
''' Funkcija, kas dala divus skaitļus. Ja nulle, tad izbeidz programmu

    input: divi float argumenti 
    
    output: dalījuma vērtība
'''
def dalisana(a,b):
    return a/b

## 5. uzdevums
## TODO uzraksti funkciju ar nosaukumu "eksponenta" un izveidot loģiku
''' Funkcija, kas eksponē arg1 pakāpē arg2.

    input: divi float argumenti 
    
    output: eksponenta vērtība
'''
def eksponenta(a,b):
    return a**b



## Šo daļu nedzēst!
if __name__=="__main__":
    print("Executing tests...")
    assert summa(1,2) == 3
    assert atnemsana(3,1) == 2
    assert multiplikacija(1,2) == 2
    assert dalisana(2,2) == 1
    assert eksponenta(2,2) == 4
    print("Done.")