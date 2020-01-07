import pandas as pd
import pkg_resources
import numpy as np
import timeit
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
import codecs

file='transcript.txt'

# Read in data
data = pd.read_csv('clean_data.csv')
texts = data['text'].astype(str)
Y = data['is_offensive']

# Vectorize the text
vectorizer = CountVectorizer(stop_words='english', min_df=0.0001) #tokenizing&vectorizing
X = vectorizer.fit_transform(texts)

X_train, X_test,Y_train, Y_test=train_test_split(X, Y, test_size=0.25)
# #Train the model
# model = LinearSVC(class_weight="balanced", dual=False, tol=1e-2, max_iter=1e5)
# cclf = CalibratedClassifierCV(base_estimator=model)
# cclf.fit(X_train, Y_train)
#
# # #Save the modelm
# joblib.dump(vectorizer, 'vectorizer.joblib')
# joblib.dump(cclf, 'model.joblib')

# vectorizer = joblib.load(pkg_resources.resource_filename(__name__,'vectorizer.joblib'))
# model = joblib.load(pkg_resources.resource_filename(__name__, 'model.joblib'))

model = joblib.load('model_37.joblib')

def read_in(file):
    f=open(file, "r")
    if f.mode=='r':
        content=f.read()
        return content

def predict(content):
  return model.predict(vectorizer.transform(content))

# print(predict([
#   'dick',
#   'sacred',
#   'bitch'
# ]))

# prediction = model.predict(X_test)
# # plt.scatter(Y_test, prediction)
# # plt.show()
#
# print(accuracy_score(Y_test, prediction))
def profanity():
    content= read_in(file)
    #print(content)
    words=content.split()
    print(words)
    analyzed=predict(words)
    print(analyzed)
    #print(analyzed[3])

    ind=[]


    inx = np.where(analyzed == 1)
    array = np.arange(len(inx))


    result = []

    for t in inx:
        for x in t:
            result.append(x)
    # for element in result:
    #     print(element)
    for x in range(len(result)):
        index2=result[x]
        data=words[index2]
        ind.append(data)

    print(ind)
    return ind

'''
  index1=int(inx[j])
            for i in index1:
                data=words[i]
                ind.append(data)
            j=j+1
'''

# profanity()
# print(predict(words).index("1"))
