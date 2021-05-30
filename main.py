import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

from pandas.io.parsers import read_csv
from functions import validate_int
import csv
from os import environ

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
"|                              |\n"
"|             | 2 |            |\n"
"|     Hur många insjuknar i    |\n"
"|      Covid-19 varje dag      |\n"
"|           i Sverige          |\n"
"|                              |\n"
"--------------------------------\n"
"\n    Gör ditt val(1-2): ")

while True:

    val = validate_int(meny, "Felaktig input, Du måste välja antingen 1 eller 2!")

    if val == 1:

        df = pd.read_csv("National_Daily_Deaths.csv",sep=',') # Läser in filen

        df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True) # gör om datum string till datetime format
      
        deaths = df['National_Daily_Deaths']

        df.plot(x ='Date', y='National_Daily_Deaths', title=f"Dagliga dödsfall i Sverige (Totalt döda:{sum(deaths)} personer)") # plottar grafen

        plt.show() # visar grafen

        

        val2 = validate_int("Vill du veta mer? (1=Ja, 2=Nej): ","Du måste svara antingen 1 eller 2")

        if val2 == 1:
            continue
        else:
            print("Hejdå!")
            break

    elif val == 2:
        
        df2 = pd.read_csv("National_Daily_ICU_Admissions.csv", sep=',')

        df2['Date'] = pd.to_datetime(df2['Date'], infer_datetime_format=True)

        total = df2['National_Daily_ICU_Admissions']

        df2.plot(x ='Date', y='National_Daily_ICU_Admissions', title=f"Dagliga intesivvårds antagningar i sverige (Totalt: {sum(total)} personer)")

        plt.show()

        val3 = validate_int("Vill du veta mer? (1=Ja, 2=Nej): ","Du måste svara antingen 1 eller 2")

        if val3 == 1:
            continue
        else:
            print("Hejdå!")
            break

        