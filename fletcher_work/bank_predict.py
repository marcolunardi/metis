import flask
from sklearn.linear_model import LogisticRegression
import numpy as np
import csv
from sklearn import cross_validation
from pandas import *

bank_full = read_csv('bank-additional-full.csv', delimiter=';', header=0)
bank = bank_full[['age','job','marital','contact','campaign','pdays','previous','poutcome','emp.var.rate','euribor3m','y']]
bank['y'] = bank['y'].map({'yes': 1, 'no': 0})
bank['age'] =((bank['age']-47)/30) ** 2
bank['age'][bank['age'] > 1] = 1
bank['job'][bank['job'] == 'student'] = 1
bank['job'][bank['job'] == 'retired'] = 1
bank['job'][bank['job'] != 1] = 0
bank['marital'][bank['marital'] == 'single'] = 1
bank['marital'][bank['marital'] != 1] = 0
bank['contact'][bank['contact'] == 'cellular'] = 1
bank['contact'][bank['contact'] != 1] = 0
bank['campaign'] = 1 / bank['campaign']
bank['pdays'][bank['pdays'] != 999] = 1
bank['pdays'][bank['pdays'] == 999] = 0
bank['previous'][bank['previous'] != 0] = 1
bank['previous'][bank['previous'] != 1] = 0
bank['poutcome'][bank['poutcome'] == 'failure'] = 0
bank['poutcome'][bank['poutcome'] == 'nonexistent'] = 0
bank['poutcome'][bank['poutcome'] == 'success'] = 1
bank['emp.var.rate'] = abs((bank['emp.var.rate'] - 1.4) / 4.8)
bank['euribor3m'] = 1 - (bank['euribor3m'] / 5.5)
X = bank.drop('y', 1)
y = bank['y']
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.15, random_state=0)
X_test = X_test.astype(float)
log_model = LogisticRegression()
PREDICTOR = log_model.fit(X_train, y_train)




# Train a model at the beginning; this guy will stay in memory the whole
# time our server is up!

# The example training data has a single feature and for all training X
# values from 1 to 500 the true response is 0; for all X values from 500
# to 1000 the true response is 1. Pretty simple decision boundary here,
# the model is if you encounter x < 500, classify as 0, if 500 < x,
# classify as 1.

# You could also load a pickled model rather than training on server
# launch, which would be more typical.

#X = np.linspace(1, 1000, 50).reshape(-1,1)
#Y = np.zeros(50,)
#Y[25:] = np.ones(25,)
#PREDICTOR = LogisticRegression().fit(X,Y)


# Initialize the app

app = flask.Flask(__name__)


# An example of routing:
# If they go to the page "/" (this means a GET request
# to the page http://127.0.0.1:5000/), return a simple
# page that says the site is up!

@app.route("/")
def hello():
    return "It's alive!!!"


# Let's turn this into an API where you can post input data and get
# back output data after some calculations.

# If a user makes a POST request to http://127.0.0.1:5000/predict, and
# sends an X vector (to predict a class y_pred) with it as its data,
# we will use our trained LogisticRegression model to make a
# prediction and send back another JSON with the answer. You can use
# this to make interactive visualizations.

@app.route("/predict", methods=["POST"])
def predict():

    # read the data that came with the POST request as a dict
    data = flask.request.json

    # let's convert this into a numpy array so that we can
    # stick it into our model
    x = np.array(data["example"]).reshape(-1,1)

    # Classify!
    y_pred = PREDICTOR.predict(x)

    # Turn the result into a simple list so we can put it in
    # a json (json won't understand numpy arrays)
    y_pred = list(y_pred)

    # Put the result in a nice dict so we can send it as json
    results = {"predicted": y_pred}

    # Return a response with a json in it
    # flask has a quick function for that that takes a dict
    return flask.jsonify(results)


# Start the server, continuously listen to requests.
# We'll have a running web app!

# For local development:
app.run(debug=True)

# For public web serving:
# app.run(host='0.0.0.0')