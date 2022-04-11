import End
import main
from functools import partial
import datetime as dt
import pandas_datareader as web
import sys


class searchUser(object):
 
 ending = True 
 
 

 def comeonman(ending):
  
  while (ending ==True):
    End.setVar(ending= True)
    company = input(str) 
    date = input(str)
    enddate = input(str)
  
    print(main.get_stock_data(company, date, enddate)) 
    setNotepad(company, date, enddate)


 

def setNotepad(company, date, enddate, ):
    args = ["y" , "n"]
    print("save to file")
    save = input(str)
  
    for x in range(2):

     if args[0]==save:
       
        print("enter file")
        filename = input(str)
        f= open(filename,"w+")
        f.write(str(main.get_stock_data(company, date, enddate)))
        break
     if args[1] == save:
        print("Not Saving Data")
        break
         
            
    



      

searchUser.comeonman(ending=True)






  
