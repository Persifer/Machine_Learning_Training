#preloaded dataset that contains information about terrains and prices in Boston
from sklearn.datasets import load_boston

#load the Boston's dataset into the var dataset
dataset = load_boston()

def printDescription():
    #printing a description of the dataset
    print(dataset['DESCR'])

if __name__ == '__main__':
    printDescription()