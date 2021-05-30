import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

from pandas.io.parsers import read_csv
from functions import *
import csv
from os import environ, sep

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == "__main__":
    suppress_qt_warnings()

# Skapar en meny som ska visas för användaren

meny = ("--------------------------------\n"
"|                              |\n"
"|   | Vad vill du veta om? |   |\n"
"|                              |\n"
"|             | 1 |            |\n"
"|      Hur många har dött      |\n"
"|          i Covid-19?         |\n"
"|               VS             |\n"
"|      dagliga intensivvårds   |\n"
"|           antagningar        |\n"
"|                              |\n"
"|             | 2 |            |\n"
"|       Covid 19 statistik     |\n"
"|       för män mot kvinnor    |\n"
"|                              |\n"
"|                              |\n"
"|                              |\n"
"--------------------------------\n"
"\n    Gör ditt val(1-2): ")


# Programloopen
while True:

    val = validate_int(meny, "Felaktig input, Du måste välja antingen 1 eller 2!")

    if val == 1:
        
        # Läser in data

        df = get_csv('National_Daily_Deaths.csv') 
        df2 = get_csv('National_Daily_ICU_Admissions.csv')
       

        # linjegraf 1
        df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True) # gör om datum string till datetime format
      
        deaths = df['National_Daily_Deaths']

        df.plot(x ='Date', y='National_Daily_Deaths', title=f"Dagliga dödsfall i Sverige (Totalt döda:{sum(deaths)} personer)") # plottar grafen
    

        # linjegraf 2
        df2['Date'] = pd.to_datetime(df2['Date'], infer_datetime_format=True)

        total = df2['National_Daily_ICU_Admissions']

        df2.plot(x ='Date', y='National_Daily_ICU_Admissions', title=f"Dagliga intesivvårds antagningar i sverige (Totalt: {sum(total)} personer)")

        plt.plot(range(120))

        plt.show() # visar graferna

        val2 = validate_int("Vill du veta mer? (1=Ja, 2=Nej): ","Du måste svara antingen 1 eller 2")

        if val2 == 1:
            continue
        else:
            print("Hejdå!")
            break


    elif val == 2:
        df3 = get_csv('Gender_Data.csv')

        colorsdf = ['lightblue', 'pink']

        ax1 = plt.subplot2grid((2,2),(0,0))

        plt.pie(df3['Total_Cases'], labels=df3['Gender'],autopct='%1.1f%%', startangle=90, colors=colorsdf)

        plt.title("Totalt antal fall")

        plt.axis('equal')

        ax2 = plt.subplot2grid((2,2),(0,1))

        plt.pie(df3['Total_ICU_Admissions'], labels=df3['Gender'],autopct='%1.1f%%', startangle=90, colors=colorsdf)

        plt.title("Totala intensivvårds antagningar")

        plt.axis('equal')

        ax3 = plt.subplot2grid((2,2),(1,0))

        plt.pie(df3['Total_Deaths'], labels=df3['Gender'],autopct='%1.1f%%', startangle=90, colors=colorsdf)

        plt.title("Totala dödsfall")

        plt.axis('equal')

        plt.show()

        val3 = validate_int("Vill du veta mer? (1=Ja, 2=Nej): ","Du måste svara antingen 1 eller 2")

        if val3 == 1:
            continue
        else:
            print("Hejdå!")
            break