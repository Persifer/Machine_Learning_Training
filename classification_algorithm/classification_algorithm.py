from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def training_classificator(dataset):
    # taking the data of the iris flower from the dataset
    X = dataset['data']
    # taking the classification of the flower from the dataset
    # 0 = Setosa | 1 = Versicolurs | 2 = Virginica
    y =  dataset['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    prediction_train = model.predict(X_train)
    prediction_test = model.predict(X_test)

    


if __name__ == '__main__':
    dataset = load_iris()

    training_classificator(dataset)