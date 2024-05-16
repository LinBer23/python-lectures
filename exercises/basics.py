'''
Schreibe je eine Funtion add, substract, multiply, divide, die die
jeweilige Grundrechenart auf die beiden übergebenen Parameter A und B
anwendet.
'''
def add(a, b): 
    return a + b

def multilpy(a,b):
    return a * b

def divide(a,b):
    return a / b

def subtract(a,b):
    return a - b

print(add(1,2))
print(multilpy(1,2))
print(divide(1,2))
print(subtract(1,2))


'''
Schreibe eine Funktion, die eine Temeratur in Celsius in eine Temperatur in
Fahrenheit umrechnet.
'''
def inFahrenheit(celsius):
    celsius = float(celsius)
    grad = celsius * 1.8 + 32
    return  grad # grad * 1.8 + 32

print(inFahrenheit(100))
# F = °C * 1,8 + 32 

'''
:param celsius: Temperature to convert in Celsius
:type celsius: float
:return: Converted temperature in Fahrenheit
'''
pass

'''
Schreibe eine Funktion, die eine Temeratur in Fahrenheit in eine Temperatur
in Celsius umrechnet.
'''
#  C = (°F - 32) * 5/9

def inCelsius(fahrenheit):
    float(fahrenheit)
    return (fahrenheit -32)*5/9

print( inCelsius(100))

'''
:param fahrenheit: Temperature to convert in Fahrenheit
:type fahrenheit: float

:return: Converted temperature in Celsius
:rtype: float
'''
pass

'''
Schreibe eine Funktion, die prüft, ob eine Zahl gerade ist.
'''
def isEven(a):
   
    if(a % 2 == 0):
        return True
    else:
        return False
    '''
    :param num: Number to test
    :type num: int

    :rtype: bool
    '''
    pass
print(isEven(3))
'''
Schreibe eine Funktion, die prüft, ob eine Zahl ungerade ist.
'''
def isOdd (a):
   if(a % 2):
        return True
   else:
    return False

print(isOdd(2))

'''
:param num: Number to test
:type num: int

:rtype: bool
'''
pass

# Kontrollfluss

# if

'''
Schreibe eine Funkntion, die abhängig von dem als Zahl eingegebenen Monat die
passende Jahreszeit zurückgibt. Und zwar

"Frühling" für die Monate März, April, Mai
"Sommer" für die Monate Juni, Juli, August
"Herbst" für die Monate September, Oktober, November und
"Winter" für die Monate Dezember, Januar und Februar.
'''
def jahreszeit(monat):

    match monat:
        case 3:
            return "Frühling"
        case 4:
            return "Frühling"
        case 5:
            return "Frühling"
        case 6:
            return "Sommer"
        case 7:
            return "Sommer"
        case 8:
            return "Sommer"
        case 9:
            return "Herbst"
        case 10:
            return "Herbst"
        case 11:
            return "Herbst"
        case 12:
            return "Winter"
        case 1:
            return "Winter"
        case 2:
            return "Winter"
        case _:
            return "Bitte eine Zahl für den Monat eingeben."
        
    '''
    :type monat: int
    :return: Jahreszeit
    :rtype: string
    '''

print(jahreszeit(12))
pass

'''
Schreibe eine Funktion, die die Umsatzsteuer anhand des Umsatzes und des
Steuerjahres berechnet. Der Steuersatz beträgt 19%. Liegt der Umsatz unter
der Freigrenze von 17.500 EUR (für die Steuerjahre 2003-2019) bzw. 22.000 EUR
(für die Steuerjahre ab 2020) soll die Kleinunternehmerregelung angewendet
und keine Umsatzsteuer berechnet werden. Der Rückgabewert ist dann 0.
'''
def umsatzsteuer(umsatz, steuerjahr = 2024):
    if((steuerjahr < 2024 or steuerjahr >2019) and umsatz < 17500):
            return 0
    elif((steuerjahr < 2024 or steuerjahr >2019) and umsatz > 17500):
            return float(umsatz) * 0.19
    elif((steuerjahr < 2019)):
            return 0
    
    '''
    :param umsatz: Umsatz im Steuerjahr
    :type umsatz: float
    :param steuerjahr: Steuerjahr
    :type steuerjahr: int

    :return: Umsatzsteuer
    :rtype: float
    '''
    pass
print(umsatzsteuer(20000,2022))
# match

'''
Schreibe eine Funktion, die den Flächeninhalt verschiedener geometrischer
Formen berechnet. Die Funktion soll zwei Argumente erhalten:
Den Namen der geometrischen Form (circle, triangle, rectangle), sowie die
dafür relevanten Parameter als ein Dictionary.
Für die Berechnung eines Kreises wird der Radius (radius) benötigt.
Für die Berechnung eines Dreieckes sowie eines Rechteckes werden die Länge
der Grundseite (base) sowie die Höhe (height) benötigt.

Beispiele für den `params` Parameter:

{ 'radius': 1.0 }
{ 'base': 2, 'height': 1 }

'''
def area (shape, params):

    '''
    :param shape: Shape
    :type shape: string
    :param params: Parameters of the shape
    :type params: dict

    :return: Area of the shape
    :rtype: float
    '''
    import math
    pass

# loops

'''
Schreibe eine Funktion, die alle Karten eines Kartenspiels jeweils mit ihrer
Farbe (Clubs, Spades, Hearts, Diamonds) und ihrem Wert (2 - 10, J, K, Q, A)
erzeugt.
Die Karten werden als Tupel bestehend aus Farbe und Wert dargestellt und alle
Karten in einer Liste gesammelt zurückgegeben.
'''
def deckOfCards():
    pass

'''
Schreibe eine Funktion, die die ersten N Antworten für das FizzBuzz-Spiel
erzeugt und auf der Konsole ausgibt.

drei teilbare Zahl wird jedoch durch das Wort „fizz“ und jede durch fünf teilbare Zahl 
durch das Wort „buzz“ ersetzt. Durch 15 teilbare Zahlen werden zu „fizz buzz“. 

Siehe auch https://de.wikipedia.org/wiki/Fizz_buzz
'''
def fizzbuzz(n):
    if(n % 3 ):
        print(n)
    elif(n % 3 == 0):
        print("fizz")
       
    if(n % 5 == 0):
        
        print("buzz") 
    if(n % 15 == 0 ):
        print("fizz buzz")   
    else:
         print(n) 
         
   
fizzbuzz(15)
# recursion

'''
Schreibe eine rekursive Funktion, die die N-te Fibonacci-Zahl berechnet.

Siehe auch https://de.wikipedia.org/wiki/Fibonacci-Folge
'''


 
def fibonacci(n):
    
    if (n <= 0):
        return 0
    if (n == 1):
        return 1
  
    
    return fibonacci(n-2) + fibonacci(n-1)

'''
:type n: int

:return: n-th Fibonacci number
:rtype: int
'''
print(fibonacci(6))