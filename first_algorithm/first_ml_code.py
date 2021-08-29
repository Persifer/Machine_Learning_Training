#preloaded dataset that contains information about terrains and prices in Boston
from sklearn.datasets import load_boston

def printDescription(dataset):
    #printing a description of the dataset
    print(dataset['DESCR'])

    for data in dataset['data']:
        print(data)

if __name__ == '__main__':
    # load the Boston's dataset into the var dataset
    dataset = load_boston()
    printDescription(dataset)