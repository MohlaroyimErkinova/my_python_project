# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ri9P92IBsuWOf_DcG1Rj_I3r24NF5_ob
"""

import random

print("Tasodifiy son tanlash dasturi")


min_son = int(input("Minimal sonni kiriting: "))
max_son = int(input("Maksimal sonni kiriting: "))


tasodifiy_son = random.randint(min_son, max_son)
print(f"Tasodifiy tanlangan son: {tasodifiy_son}")