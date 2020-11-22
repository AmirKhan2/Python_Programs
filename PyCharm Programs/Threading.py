from threading import *
from time import sleep


class pogaa(Thread):
    def run(self):
        for i in range(5):
            print("Pogaa")
            sleep(1)


class aapigo(Thread):
    def run(self):
        for i in range(5):
            print("Papoy")
            sleep(1)


pog = pogaa()
aap = aapigo()

pog.start()
sleep(0.2)
aap.start()

pog.join()
aap.join()

print("Fin.")
