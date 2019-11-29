print('begin')
try:
    h=eval(input('enter value'))
    print('data',20/h)
except ValueError as e:
    print("value not valid")
except EOFError as e:
    print("end of file")
except (ZeroDivisionError,TypeError,AttributeError) as e:
    print('Unknown Error',e)
finally:
    print('end')
