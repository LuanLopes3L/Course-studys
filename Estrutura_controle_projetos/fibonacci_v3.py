#!/usr/local/bin/python3

def fibonnaci(limite):
    penultimo = 0
    ultimo = 1
    print(f"{penultimo},{ultimo}", end=',')
    while ultimo < limite:
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(ultimo, end=',')


if __name__ == '__main__':
    fibonnaci(200)