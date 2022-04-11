import datetime as dt
import pandas_datareader as web
import UI
import sys



class myClass(object):
   
   def __init__(self, company,date,enddate):
        self.company=company
        self.date =date
        self.enddate=enddate

    
def get_stock_data(ticker, start, end):
 return web.DataReader(ticker, "yahoo", start, end)     


UI.printRat()

