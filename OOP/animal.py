from step0 import generate_hist_name
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age



class Dog:

    def __init__(self, name, age,type):
        self.name, self.age, self.type = name, age, type

    def makeVoice(self):
        print ('WangWang')

    def saveDataForFurtherRef(self, data, filename):
        self.data = data
        self.filename = filename


    def generate_hist_name(self):
        self.csvFile = generate_hist_name(self.data, self.filename)
    

pika = Dog('Pika', 3, 'British Short')
pika.makeVoice()
pika.saveDataForFurtherRef('Some garbagge data', 'shiyi.csv')
pika.generate_hist_name()
print(pika.csvFile)

mumu = Dog('Mumu', 2, "British Short Hybrate")

