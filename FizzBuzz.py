class Fizzbuzz:
    def affiche(self, nombre):
        resultat=""

        for i in range(1, nombre + 1):
            if i%15==0 :
                resultat += "FrisBee"
            elif i%5==0:
                Resultat += "Buzz"
            elif i%3==0:
                resultat += "Fizz"
            else:
                resultat += str(i)
        
        return resultat