
def validate_int(output, error):
    while True:
        try:
            value = int(input(output))
            break
        except:
            print(error)
    return value
