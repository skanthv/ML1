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

from sklearn.linear_model import Ridge
#LINEAR REGRESSION WITH A FEATURE TO PREVENT OVERFITTING BY ADDING PENALTY TERM TO COST FUNCTION
#PENALTY TERM IS alpha* square of model weights
ridgereg=Ridge(alpha=1)
ridgereg.fit(X,y)
y_pred=ridgereg.predict([[10,20, 30, 40, 50]])
print("Y predicted=",y_pred)
print("R squared=",ridgereg.score(X,y))
print("weights learnt for the features are =",ridgereg.coef_)
