# Nathan Todzy
# Foundations of Programming.
# Use Stock Data to determine profeits.
# November 18th -> Nov 22.

#LIBRARIES
import requests as req
import json
import numpy
from pandas.tseries.holiday import USFederalHolidayCalendar

# VARIBLE DECLARATION
API_KEY = YOUR_API_KEY_HERE # I am going to leave this API Key here for you in case you want to run it

# FUNCTION DECLARTION

def stock_info(SYMBOL, DAY): # SYMBOL IE. TSLA and YYYY-MM-DD

  if SYMBOL.upper() == "EXIT":
    exit() # Way to break loop besides finishing the program.
    
  REQUEST = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + SYMBOL.upper() + "&apikey=" + API_KEY

  stock_json = req.get(REQUEST) # Retrieve stock data, this includes all data from the last 20 years from 2019.

  stock_list = json.loads(stock_json.text).get("Time Series (Daily)") #Parse JSON for only the data, exclude the metadata

  # Use stock_list["YYYY-MM-DD"] because this is also a list it is treated as an array so we can get the values assigned under that value. (Essentially a Tensor.)
  
  # @TODO Use dynamic days back with buisness days exclude US Holidays because the api only interfaces with S&P, NYSE and NASDAQ Only.

  
  try: 
    day_data = stock_list[DAY]

    return day_data
  
  except TypeError as error: # Trading Symbol does not exist
    print("ERROR:", error)
    print("ERROR:", "That Symbol does not exist on the S&P, NYSE or NASDAQ.\n")
    main() # THIS IS VERY BAD YOU WILL CREATE AN INFINITE LOOP. THIS IS OKAY FOR REPL.IT ATM @ TODO MAKE A KILL SWITCH. JUST USE CTRL + C OR STOP.
  
  except KeyError as error: # Day Data does not exist.
    print("ERROR:", error)
    print("ERROR:", "Stock Data for that day does not exist\n")
    main() # THIS IS VERY BAD YOU WILL CREATE AN INFINITE LOOP. THIS IS OKAY FOR REPL.IT ATM @ TODO MAKE A KILL SWITCH. JUST USE CTRL + C OR STOP.

  except: # Program did an oopsie. Just a precaution.
    print("ERROR:", "An unknown issue occured please report.")
    main() # THIS IS VERY BAD YOU WILL CREATE AN INFINITE LOOP. THIS IS OKAY FOR REPL.IT ATM @ TODO MAKE A KILL SWITCH JUST USE CTRL + C OR STOP.

def stock_differences(SYMBOL):

  # I know assuming is bad, but because this program is going to be used in a practical way, we are going to assume that they will use t

  PAST = input("When did you buy your stock? (YYYY-MM-DD): ")
  FUTURE = input("What day would you like to evalutate against? (YYYY-MM-DD): ")

  FUTURE_CLOSE = float(stock_info(SYMBOL, FUTURE)["4. close"]) # This varible is very misleading, although it is right because it is in the future of the past but we only have data upto the present.

  #print(FUTURE_CLOSE)
  PAST_CLOSE = float(stock_info(SYMBOL, PAST)["4. close"])
  #print(PAST_CLOSE)

  return round(FUTURE_CLOSE - PAST_CLOSE, 2), FUTURE_CLOSE, PAST_CLOSE
#######################

def main():
  stock_symbol = input("What symbol would you like to retrive info for? ")

  NET_GL = stock_differences(stock_symbol)

  if NET_GL[0] > 0:
    print("You have made", NET_GL[0], "USD per share.\n")

  elif NET_GL[0] < 0:
    print("You have lost", NET_GL[0], "USD per share\n")
    
  elif NET_GL[0] == 0:
    print("You did not make any money. ):\n")

  shares = int(input("How many shares did you buy? "))
  total_net =  shares * NET_GL[0] # You cannot get half a share.

  print("You bought", shares, "shares at", NET_GL[2], "a share. For a total of", shares * NET_GL[2], "USD." )
  print("You have netted", round(total_net, 2), "USD")
    
#######################
main()

  # day_5 = day_0[0:8] + str(int(day_0[8:10]) - 7)
  # print(day_5)

  # stock_info(stock_symbol, day_0) #stock_info(SYMBOL, DAY)
  # stock_info(stock_symbol, day_5) #stock_info(SYMBOL, DAY)

  # print(numpy.busday_offset(input("YYYY-MM-DD: "), offsets=0 , roll='backward', weekmask='1111100')) #busday_offset(dates, offsets, roll='raise', weekmask='1111100', holidays=None, busdaycal=None, out=None)
