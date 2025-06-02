from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf1 = LogisticRegression()
clf2 = GaussianNB()
clf3 = DecisionTreeClassifier()

ensemble = VotingClassifier(estimators=[
    ('lr', clf1), ('nb', clf2), ('dt', clf3)],
    voting='hard')

ensemble.fit(X_train, y_train)
print("Accuracy:", ensemble.score(X_test, y_test))



print("Final Population:", population)
