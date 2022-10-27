#!/usr/bin/env python3
'''
Python 6 nodarbības mājasdarbs Nr.2

Uzdevums: aizpildīt vietas ar atzīmi TODO
'''
import matplotlib.pyplot as plt
import json
import numpy as np

# Importēt failu "top_vardi.json" un saglabāt atslēgas kā listi ar nosaukumu "x"
# vērtības kā listi ar nosaukumu "y"
# TODO
f=open("ml_md/top_vardi.json")
a=json.load(f)
x = list(a.keys()) 
y = list(a.values())
print(x,y)

# izveidot stabiņveidu grafiku kas rāda vārdu biežumu (y ass), Vārdus uz x ass
# piemērs ir mājasdarbu failā
fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_ylabel('Biežums')
ax.set_xlabel('Vārdi')
ax.set_title('Biežākie vārdi')
plt.show()



