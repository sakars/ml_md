#!/usr/bin/env python3
'''
Python 7 mājasdarbs Nr.1

Uzdevums: aizpildīt vietas ar atzīmi TODO

Izveidot jaunu datu tipu, kurš paņem vārdisku un skaitlisku vērtību, un pēc tam spēj atdod numeriskas vērtības
Datu tips atļauj sekojošos ievadvērtības:
- "one", "two", "three", "four", "five"
'''

class JaunsDatuTips:

    def __init__(self, vertiba):
        
        self.vertiba = vertiba

    def get_int(self):
        if self.vertiba=="one":
            return 1
        if self.vertiba=="two":
            return 2
        if self.vertiba=="three":
            return 3
        if self.vertiba=="four":
            return 4
        if self.vertiba=="five":
            return 5
        return 0

    def get_float(self):
         
        return float(self.get_int())

    def get_string(self):
        # kad tiek izsaukta metode atdod parametru "vertiba" kā string datu tipu
        # TODO
        return self.vertiba

if __name__ == "__main__":
    x1 = JaunsDatuTips("one")
    x2 = JaunsDatuTips("two")
    x3 = JaunsDatuTips("three")
    x4 = JaunsDatuTips("four")
    x5 = JaunsDatuTips("five")

    # Kad uzvedums izpildīts, var pārbaudīt vai rezultāts ir pareizs, atkomentējot assert
    # TODO
    assert x1.get_int()==1
    assert x2.get_int()==2
    assert x3.get_int()==3
    assert x4.get_int()==4
    assert x5.get_int()==5

    assert x1.get_float()==1.0
    assert x2.get_float()==2.0
    assert x3.get_float()==3.0
    assert x4.get_float()==4.0
    assert x5.get_float()==5.0

    assert x1.get_string()=="one"
    assert x2.get_string()=="two"
    assert x3.get_string()=="three"
    assert x4.get_string()=="four"
    assert x5.get_string()=="five"