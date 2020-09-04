import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('Book1.csv')
df_names = df
df_names.classes.replace({'Name': 0, 'Type': 1}, inplace=True)
Xfeatures = df_names['Name']
cvect = CountVectorizer()
X = cvect.fit_transform(Xfeatures)
y = df_names.classes
clf = MultinomialNB()
clf.fit(X, y)


def extractedName(val):
    new = cvect.transform([val])
    y_pred = clf.predict(new)
    if (y_pred == 0):
        return "Name"
    else:
        return "Type"