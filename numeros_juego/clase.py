import random

guessesTaken = 0
minNumber = 1
maxNumber = 20

print('Hola Cual es tu nombre: ')
usrname = input()

number = random.randint(minNumber, maxNumber)
print('hola, ' + usrname + ' estoy pensando en numero entre '+ str(minNumber) + ' y ' + str(maxNumber))

while guessesTaken < 6:
    print("intentalo: ")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("No es un numero mas alto")

    if guess > number:
        print("NO es numero mas bajo")

    if guess == number:
        #print('acertaste!!!!')
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('buen trabajo' + usrname + '! el numero de intento es '+ guessesTaken + ' intentos ')

if guess != number:
    number = str(number)
    print('NO el numero en el que estoy pensando es ' + number) 
