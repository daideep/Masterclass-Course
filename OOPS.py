
##Using the concept of object oriented programming and inheritance, create a super class named Computer, which has two sub classes named Desktop and Laptop.
##
##Define two methods in the Computer class named getspecs and displayspecs, to get the specifications and display the specifications of the computer.
##
##You can use any specifications which you want.
##The Desktop class and the Laptop class should have one specification which is exclusive to them for example laptop can have weight as a special specification.
##
##Make sure that the sub classes have their own methods to get and display their special specification.
##
##Create an object of laptop/ desktop and make sure to call all the methods from the computer class as well as the methods from the own class


class Computer:

    def __init__(self,Ram,Processor):
        self.ram = Ram
        self.processor = Processor

    def getspecs(self):
        print('Enter Detail')
        self.ram = input('Enter Ram size: ')
        self.processor = input('Enter Processor Size: ')

    def displayspecs(self):
        print('ram size : {0} ,\n Processor size : {1}'.format(self.ram,self.processor))
       #print(' Ram size is: ' + self.ram +  ' processor is: ' + self.processor)


class Desktop(Computer):

     def __init__(self,casecolor):
         self.casecolor = casecolor

     def get_casecolor(self):
         self.casecolor = input('Enter casecolor :')

     def dsiplay_casecolor(self):
         print("CaseColor value :" + self.casecolor)



class Laptop(Computer):    

      def __init__(self,weight):
          self.Weight = weight

      def get_weight(self):
          self.weight = input('Enter Weight: ')

      def display_weight(self):
          print("Laptop weight :", self.weight)


L1 = Laptop('10')

print(L1.Weight)

L1.get_weight()

L1.display_weight()

L1.getspecs()

L1.displayspecs()












    
