import pickle
import os
import pandas
from sklearn import preprocessing, linear_model


class PlayerModel:
    """
    A model of a player we can ask for its "choices"
    based on what it "knows" about its hand and game
    position
    """

    def __init__(self):
        self.clf = linear_model.LogisticRegression()

    def train(self):
        data = [(0, 0, 1, 1, 1, 0, 0), (1, 0, 0, 0, 0, 0, 1)]
        df = pandas.DataFrame(data)
        X = df.iloc[:, 1:]
        y = df.iloc[:, 0]
        self.clf.fit(X, y)

    def ask_model_for_discard(self, hand):
        return hand[0:2]

    def ask_for_pegging_play(self, play_vector, hand):
        return hand[0]


def load_trained_model():
    if os.path.isfile("trained_model.pkl"):
        model = pickle.load("trained_model.pkl")
        return model
    else:
        print(
            "Missing Model: No model found. Hold on a sec while we train a small data set."
        )
        model = PlayerModel()
        model.train()
        return model
