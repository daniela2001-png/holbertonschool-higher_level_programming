#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        v = 0
        v = a / b
        return v
    except ZeroDivisionError:
        return None
    finally:
        if b != 0:
            print("Inside result: {:.1f}".format(v))
        else:
            print("Inside result: {}".format(None))
