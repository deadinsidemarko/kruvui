import pandas as pd
from colorama import init, Fore, Back, Style

pd.options.display.max_columns = 9
pd.set_option('display.width', 1400)
init(autoreset=True) 

with open('bulochki.txt') as fileobject:
    bulochkis = []
    bulochkis = fileobject.readlines()
    bulochkis = [line.rstrip('\n') for line in bulochkis]

print("\n")
print(Style.BRIGHT + Fore.BLUE + "Булочки:",*bulochkis,sep="\n")
print("\n")

with open('parameters.txt') as fileparameters:
    parameters = []
    parameters = fileparameters.readlines()
    parameters = [line.rstrip('\n') for line in parameters]

print(Style.BRIGHT + Fore.BLUE + "Параметри:",*parameters,sep="\n")
print("\n")

with open('importance.txt') as fileimportance:
    importance = []
    importance = fileimportance.readlines()
    importance = [line.rstrip('\n') for line in importance]

file1 = open ('1.txt' , 'r')
exp1 = []
exp1 = [ line.split() for line in file1]

file2 = open ('2.txt' , 'r')
exp2 = []
exp2 = [ line.split() for line in file2]

file3 = open ('3.txt' , 'r')
exp3 = []
exp3 = [ line.split() for line in file3]

file4 = open ('4.txt' , 'r')
exp4 = []
exp4 = [ line.split() for line in file4]

def Price (bulochki):
    price = float(importance[0]) * (float(exp1[bulochki][0])+float(exp2[bulochki][0])+float(exp3[bulochki][0])+float(exp4[bulochki][0]))
    return price

def Stuffing (bulochki):
    stuffing = float(importance[1]) * (float(exp1[bulochki][1])+float(exp2[bulochki][1])+float(exp3[bulochki][1])+float(exp4[bulochki][1]))
    return stuffing

def Design (bulochki):
    design = float(importance[2]) * (float(exp1[bulochki][2])+float(exp2[bulochki][2])+float(exp3[bulochki][2])+float(exp4[bulochki][2]))
    return design

def Size (bulochki):
    size = float(importance[3]) * (float(exp1[bulochki][3])+float(exp2[bulochki][3])+float(exp3[bulochki][3])+float(exp4[bulochki][3]))
    return size

def Dough (bulochki):
    dough = float(importance[4]) * (float(exp1[bulochki][4])+float(exp2[bulochki][4])+float(exp3[bulochki][4])+float(exp4[bulochki][4]))
    return dough

def Value (bulochki):
    value = float(importance[5]) * (float(exp1[bulochki][5])+float(exp2[bulochki][5])+float(exp3[bulochki][5])+float(exp4[bulochki][5]))
    return value

def Light (bulochki):
    light = float(importance[6]) * (float(exp1[bulochki][6])+float(exp2[bulochki][6])+float(exp3[bulochki][6])+float(exp4[bulochki][6]))
    return light

#Croissant
price1 = Price(0)
stuffing1 = Stuffing(0)
design1 = Design(0)
size1 = Size(0)
dough1 = Dough(0)

#Kalachi
price2 = Price(1)
stuffing2 = Stuffing(1)
design2 = Design(1)
size2 = Size(1)
dough2 = Dough(1)

#Brioche
price3 = Price(2)
stuffing3 = Stuffing(2)
design3 = Design(2)
size3 = Size(2)
dough3 = Dough(2)

#Pampushki
price4 = Price(3)
stuffing4 = Stuffing(3)
design4 = Design(3)
size4 = Size(3)
dough4 = Dough(3)

#Waffles
price5 = Price(4)
stuffing5 = Stuffing(4)
design5 = Design(4)
size5 = Size(4)
dough5 = Dough(4)

#Sum

sum1 = price1 + design1 + stuffing1 + dough1 + size1
sum2 = price2 + design2 + stuffing2 + dough2 + size2
sum3 = price3 + design3 + stuffing3 + dough3 + size3
sum4 = price4 + design4 + stuffing4 + dough4 + size4
sum5 = price5 + design5 + stuffing5 + dough5 + size5

parameters.append('')
importance.append('')

df = pd.DataFrame({'№': ['1', '2', '3', '4', '5', 'Сума'],
                   'Параметри': parameters,
                   'Вага': importance,
                   bulochkis[0]: [price1, stuffing1, design1, size1, dough1, sum1],
                   bulochkis[1]: [price2, stuffing2, design2, size2, dough2, sum2],
                   bulochkis[2]: [price3, stuffing3, design3, size3, dough3, sum3],
                   bulochkis[3]: [price4, stuffing4, design4, size4, dough4, sum4],
                   bulochkis[4]: [price5, stuffing5, design5, size5, dough5, sum5]})

print(Style.BRIGHT + Fore.GREEN + "Результат:")
print(df)
print('\n')

winer = ''
points = ''

if sum1 > sum5 and sum1 > sum3 and sum1 > sum2 and sum1 > sum4:
    winer = bulochkis[0]
    points = sum1
elif sum2 > sum5 and sum2 > sum3 and sum2 > sum1 and sum2 > sum4:
    winer = bulochkis[1]
    points = sum2
elif sum3 > sum5 and sum3 > sum2 and sum3 > sum1 and sum3 > sum4:
    winer = bulochkis[2]
    points = sum3
elif sum4 > sum5 and sum4 > sum2 and sum4 > sum1 and sum4 > sum3:
    winer = bulochkis[3]
    points = sum4
elif sum5 > sum4 and sum5 > sum2 and sum5 > sum1 and sum5 > sum3:
    winer = bulochkis[4]
    points = sum5
else:
    print("Щось пішло не так при обличсленнях переможця, або переможець не один!")

print(Fore.YELLOW + "Найкращим варіантом вийшов -",winer, '-', points)
print('\n')