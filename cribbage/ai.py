import pickle
import os
import pandas
from sklearn import preprocessing, linear_model

class Model:
    def __init__(self):
        self.clf = linear_model.LogisticRegressionCV()

    def train_clf():
        df = pandas.read_csv('data_set.csv', index_col=0)
        X = df.iloc[:, 1:]
        y = df.iloc[:, 0]
        self.clf.fit(X, y)

    def ask_for_discards(self, hand):
        return hand[0:2]

    def ask_for_input(self, play_vector, hand):
        return hand[0]

def train_model():
    model = Model()
    print("Training RL model")
    model.train_model()
    print("Saving (pickling) model")
    pickle.pickle(model, 'trained_model.pkl')

def load_trained_model():
    if os.path.isfile('trained_model.pkl'):
        model = pickle.load('trained_model.pkl')
        return model
    else:
        print("Missing Model: No model found. Run the game with \"--train-model\" to train the model first")
