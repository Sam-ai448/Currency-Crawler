# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oTyoBsTFGu6FxjI186auRmwZfBgR7kyI
"""

import requests
req = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
print(req.text)

import pandas
dfs = pandas.read_html("https://rate.bot.com.tw/xrt?Lang=zh-TW")
print(dfs[0])