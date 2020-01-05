import pandas as pd
import pkg_resources
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
#
# def _get_profane_prob(prob):
#   return prob[1]

def predict(texts):
  return model.predict(vectorizer.transform(texts))
#
# def predict_prob(texts):
#   return np.apply_along_axis(_get_profane_prob, 1, model.predict_proba(vectorizer.transform(texts)))

# Read in data
data = pd.read_csv('clean_data.csv')
texts = data['text'].astype(str)
Y = data['is_offensive']

# Vectorize the text
vectorizer = CountVectorizer(stop_words='english', min_df=0.0001) #tokenizing&vectorizing
X = vectorizer.fit_transform(texts)

X_train, X_test,Y_train, Y_test=train_test_split(X, Y, test_size=0.25)
# Train the model
# model = LogisticRegression()
# model.fit(X_train, Y_train)

# Save the model
# joblib.dump(vectorizer, 'vectorizer_LR.joblib')
# joblib.dump(model, 'model_LR.joblib')

vectorizer = joblib.load(pkg_resources.resource_filename(__name__,'vectorizer_LR.joblib'))
# model = joblib.load(pkg_resources.resource_filename(__name__,'model_LR.joblib'))
model = joblib.load('model_LR.joblib')
def predict(texts):
  return model.predict(vectorizer.transform(texts))
print(predict([
    'ass',
    'fuck you',
    'Holy crap',
    'nigger'
  ]))
prediction = model.predict(X_test)
# plt.scatter(Y_test, prediction)
# plt.show()

print accuracy_score(Y_test, prediction)
