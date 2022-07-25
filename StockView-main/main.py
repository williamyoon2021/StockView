import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf # Yahoo Finance stock data
import tkinter as tk

from setuptools import Command
from pandas.plotting import scatter_matrix
import yfinance as yf # Yahoo Finance stock data
import tkinter as tk
from tkinter import ttk
from tkinker.messagebox import showinfo

from metrics import *

class main:
    root = tk.Tk()
    root.title('StockView')
    root.geometry('300x200')
    root.resizable(True, True)
    
    def getStock():
        name = input("Which company would you like to analyze?")
        while True:
            if name.isupper() and name.isalpha():
                break
            else:
                print('Please enter only uppercase letters!')
        metrics(name)
        
    stockButton = ttk.Button(text="Get Stock", command=getStock)
    shouldIButton = ttk.Button(root, text="Decision", command=metrics.recommendation)

        
    