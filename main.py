#from lib1 import carre, algo
import lib1

def say_hello(input):
    print("hello, world!")
    print("carre de {}: {}".format(input, carre(input)))
    print("resultat algo1:{}".format(algo([5,5,2,1,5])))
say_hello(8)


