#!/usr/bin/env python3
'''
Python 7 mājasdarbs Nr.2

Uzdevums: aizpildīt vietas ar atzīmi TODO

Izveidot klasi, kura pārveido 5. nodarbības mājasdarbu Nr. 2 saturu par klasi

'''
import matplotlib.pyplot as plt
import json
import os

class TopWords:
    '''
    Izveidot klasi, kurai ir 2 publiskas metodes:
    - setVardnica -  definē failu
    - grafiks - izvada grafiku

    Klasei nav pieejami publiski parametri
    '''
    def set_dict(self,vardnicaFails):
        f=open(vardnicaFails)
        self.__vardnica = json.load(f)
        f.close()

    def get_bar_plot(self):     
        plt.bar(range(len(self.__vardnica)), list(self.__vardnica.values()), align='center')
        plt.xticks(range(len(self.__vardnica)), list(self.__vardnica.keys()))
        plt.show()
        return 0


if __name__ == "__main__":
    obj = TopWords()
    obj.set_dict("top_vardi.json")
