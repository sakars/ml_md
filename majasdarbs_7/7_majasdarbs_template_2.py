#!/usr/bin/env python3
'''
Python 7 mājasdarbs Nr.2

Uzdevums: aizpildīt vietas ar atzīmi TODO

'''

from IntroOpenCV import IntroOpenCV
from TopWords import TopWords

# definēt klasi, kura manto klases TopVardi un IevadsOpenCV
# TODO
class Majasdarbs(IntroOpenCV,TopWords):
    '''

    '''
    pass



if __name__ == "__main__":
    obj = Majasdarbs()
    obj.set_picture("python.jpg")
    obj.get_blue_red()
    obj.set_dict("top_vardi.json")
    obj.get_bar_plot()
