def weight_on_planets():
   # write your code here
   weightEarth = input("What do you weigh on earth? ") #take in user weight using test input
   weightEarthFloat = float(weightEarth)
   weightMars = weightEarthFloat * .38
   weightJupiter = weightEarthFloat * 2.34

   print("\nOn Mars you would weigh " + str(weightMars) + " pounds.\n" + "On Jupiter you would weigh " + str(weightJupiter) + " pounds.")

if __name__ == '__main__':
   weight_on_planets()
