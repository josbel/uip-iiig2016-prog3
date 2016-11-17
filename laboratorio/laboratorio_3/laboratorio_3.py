while True:
    preg = input ("preguntale a juan: ")

    if preg.endswhith('?'):
        print("ofi")

    elif preg >= 'A' and preg <= 'Z':
        print ("chilea")

    elif (len(preg)==0):
        print ("Mmm")

    else:
        print ("me da igual")