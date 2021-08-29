#preloaded dataset that contains information about terrains and prices in Boston
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

def printDescription(dataset):
    #printing a description of the dataset
    print(dataset['DESCR'])

    #printig all the data of the dataset
    for data in dataset['data']:
        print(data)
        print()


def stratingTheTraining(dataset):

    # matrix which contains the features of the houses in Boston
    X = dataset['data']
    # matrix which contains the price to predict
    y = dataset['target']

if __name__ == '__main__':
    # load the Boston's dataset into the var dataset
    dataset = load_boston()
    printDescription(dataset)

