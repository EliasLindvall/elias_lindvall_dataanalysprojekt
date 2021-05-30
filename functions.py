import pandas as pd

def validate_int(output, error):
    while True:
        try:
            value = int(input(output))
            break
        except:
            print(error)
    return value

def get_csv(filename):
    value = pd.read_csv(filename, sep=',')
    return value
