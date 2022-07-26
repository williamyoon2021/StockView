import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf # Yahoo Finance stock data
import tkinter as tk
from metrics import * 
import pandas_datareader.data as web
import config

from setuptools import Command
from pandas.plotting import scatter_matrix
import yfinance as yf # Yahoo Finance stock data
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class main:
    root = tk.Tk()
    root.title('StockView')
    root.geometry('600x400')
    root.resizable(True, True)
    get_stock()

    def get_stock(self):
        name = input("Which company would you like to analyze?")
        while True:
            if name.isupper() and name.isalpha():
                break
            else:
                print('Please enter only uppercase letters!')
        metrics.def_download(name)
        
    def press_button(self):    
        stockButton = ttk.Button(root, text='Get Stock', command=get_stock)
        stockButton.pack(side = 'top')  
        self.other_buttons()
    
    def other_buttons(self):
        randomButton = ttk.Button(root, text='Two hundred day MA', command=metrics.cap("random"))
        randomButton.pack(side = 'bottom')

    # stockButton = ttk.Button(root, text='To HTML', command=metrics.write_to_html())
    # stockButton.pack(side = 'bottom')  
    
  
    

    # shouldIButton = ttk.Button(root, text="Demcision", command=metrics.recomendation)

    root.mainloop()
        
    