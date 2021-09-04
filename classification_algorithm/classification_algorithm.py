from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def training_classificator(dataset):
    # taking the data of the iris flower from the dataset
    X = dataset['data']
    # taking the classification of the flower from the dataset
    # 0 = Setosa | 1 = Versicolurs | 2 = Virginica
    y =  dataset['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y)




if __name__ == '__main__':
    dataset = load_iris()

    training_classificator(dataset)