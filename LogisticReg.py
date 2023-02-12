from sklearn.datasets import load_iris
data=load_iris()
print("sample data",data)
X,y=load_iris(return_X_y=True)
from sklearn.linear_model import LogisticRegression
logreg=LogisticRegression(random_state=0,max_iter=200)
logreg.fit(X,y)
print("PREDICTIONS ",logreg.predict(X[:2,:]),
      " PREDICTION PROBABILITIES: ",logreg.predict_proba(X[:2,:]),
      " PREDICTION LOG PROB: ",logreg.predict_log_proba(X[:2,:]),sep="\n")
print("score i.e. avg accuracy on test data and labels =",logreg.score(X,y))

from sklearn.metrics import confusion_matrix
#confusion_matrix(ytrue,ypred)
from sklearn.metrics import classification_report
classification_report(ytrue,ypred)
