try:
    42 / 0
except ZeroDivisionError:
    print('It\'s impossible to divide any number for 0!')

def transformToNumber(value):
    try:
        return print(str(float(value)))
    except:
        return print('ERROR!')


transformToNumber('10')
transformToNumber('10,0')