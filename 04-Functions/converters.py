def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inches(n):
    return n/2.54

def feet_to_cm(n):
    return n*30.48

def inches_to_cm(n):
    return n*2,54

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'67cm = {cm_to_inches(67)}inches')
    print(f'8ft = {feet_to_cm(8)}cm')
    print(f'125inch = {inches_to_cm(123)}cm')