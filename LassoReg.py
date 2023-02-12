#if linear model gets overfit to training data ,then it will not generalize well for test data
# there will be overfitting
#to prevent it, we add penalty term to loss function..and then try to optimize the cost function..
import numpy as np

#GENERATE RANDOM DATA FOR TRAINING ..SO GENERATE SOME INDEPENDENT FEATURES X , DEPENDENT FEATURE Y
#FOR A CERTAIN NUMBER OF SAMPLES
rnd=np.random.RandomState(0)
n_samples, n_features= 10, 5
y=rnd.randn(n_samples)
X=rnd.randn(n_samples,n_features)
print("X=",X,"Y=",y,sep="\n")

from sklearn.linear_model import Lasso
#LINEAR REGRESSION WITH A FEATURE TO PREVENT OVERFITTING BY ADDING PENALTY TERM TO COST FUNCTION
#PENALTY TERM IS alpha* SUM OF ABSOLUTE VALUE OF  model weights
lassoreg=Lasso(alpha=1)
lassoreg.fit(X,y)
#print model
print("number of iterations ran=",lassoreg.n_iter_)
print("number of input features=",lassoreg.n_features_in_)
print("weights learnt for the features are =",lassoreg.coef_)
print("intercept",lassoreg.intercept_)

#Check performance metrics
print("R squared=",lassoreg.score(X,y))

#PREDICT ON A TEST DATA
y_pred=lassoreg.predict([[10,20, 30, 40, 50]])
print("Y predicted=",y_pred)

#print("input features",lassoreg.feature_names_in_)
