Num = int(input('Digite Cuantos Numeros de la sucesion Fibonacci Deseas Ver.'))
Antecesor , Sucesor = 0 , 1

    while Sucesor < Num :
        print(Sucesor,end=',')
        Antecesor , Sucesor = Sucesor , Antecesor + Sucesor