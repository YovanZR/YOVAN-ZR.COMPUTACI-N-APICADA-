def centigrados_a_fahrenheit(c: float) -> float:
    return (c*9/5)+32

def fahrenheit_a_centigrados(f: float) -> float:
    return (f-32)*5/9

def main():
    print('1. C->F')
    print('2. F->C')
    op=int(input('Opción: '))
    if op==1:
        c=float(input('C: '))
        print(centigrados_a_fahrenheit(c))
    elif op==2:
        f=float(input('F: '))
        print(fahrenheit_a_centigrados(f))
    else:
        print('Inválido')

if __name__=='__main__':
    main()
