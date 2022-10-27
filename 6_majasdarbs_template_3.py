#!/usr/bin/env python3
'''
Python 6 nodarbības mājasdarbs Nr.3

Uzdevums: aizpildīt vietas ar atzīmi TODO
'''

import numpy as np
import cv2 as cv

# importēt "python.jpg" bildi
img = cv.imread(cv.samples.findFile("ml_md/python.jpg"), cv.IMREAD_COLOR)

cv.imshow("ok", img)
c = cv.waitKey(-1)

# Pārveidot bildi melnbaltu un izvadīt uz ekrāna
img_melnbalts = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("ok", img_melnbalts)
c = cv.waitKey(-1)

# pielietot Caddy edge detection uz originālās bildes un izvadīt uz ekrāna
img_caddy = cv.Canny(img, 100, 150)

cv.imshow("ok", img_caddy)
c = cv.waitKey(-1)

# Pārveidot zilo krāsu par sarkanu un izvadīt uz ekrāna
img_zils_sarkans = cv.cvtColor(img, cv.COLOR_BGR2RGB)


cv.imshow("ok", img_zils_sarkans)
c = cv.waitKey(-1)