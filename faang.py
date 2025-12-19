#!/usr/bin/env python3

import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt



def plot_data():                       
    """ 
    Creating a function called plot_data
    """
    
    folder = "data"           
    
    # Defining the folder name "data" where the CSV files I want to read are located.

    files = [
        
        f for f in os.listdir(folder) 
        if f.endswith(".csv")
        
        ]  
    
    # https://docs.python.org/3/library/os.html#os.listdir                                                                   
    os.makedirs("plots", exist_ok=True) 
    
    #creates a plot
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
    plt.figure() 

    for file in files:
         # Join folder and filename into a valid path
        filepath = os.path.join(folder, file)

       # Reads the CSV file
        df = pd.read_csv(
            filepath, 
            index_col=0, 
            parse_dates=True
            ) 

        
        # DEBUG — view the contents and column types 
        print(f"\n--- DEBUG arquivo: {file} ---")
        print(df.head())
        
        # Correction of the Close column type
        print("\nTipos das colunas:")
        print(df.dtypes)
        #(https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html)
        
        
        # Ensure the Close column is numeric
        # https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html
        df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
        
        # Remove rows where Close is NaN
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html
        df = df.dropna(subset=["Close"])

        # Plot Close prices
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.htm
        stock_name = file.split("_")[0]
        plt.plot(df.index, df["Close"], label=stock_name)

        # Save the plot
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.title(datetime.now().strftime("%Y-%m-%d"))
    plt.legend()
    
    # Save the plot to the plots folder
    filename =datetime.now().strftime("stocks_%Y%m%d.png")
    save_path =os.path.join('plots',filename)
    
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
    plt.savefig(save_path)
    
    # display the plot
    plt.show()
    
if __name__ =="__main__" :
    # Ensures the function runs only when the script is executed directly
    # https://docs.python.org/3/library/__main__.html

# Runs the function
    plot_data()

