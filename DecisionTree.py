X=[[0],[1],[2],[3],[4],[5]]
y=[1,0,1,0,1,0]
from sklearn import tree
dtcls=tree.DecisionTreeClassifier()
dtcls=dtcls.fit(X,y)
y_pred=dtcls.predict([[7]])
print("Y predicted=",y_pred)
pred_prob=dtcls.predict_proba([[7]])
print("probabilities of classifying as a particular class=",pred_prob)

treereport=tree.export_text(dtcls,feature_names=["x"])
print("TREE STRUCTURE IS \n",treereport)

#graphdata=tree.export_graphviz(dtcls,out_file=None)
#import graphviz as g
#graph1=g.Source(graphdata)
#graph1.render("x")
#g.render("decision tree",)
#
###################################
#DECISION TREE REGRESSOR
print("Decision tree regressor:")
dtreg=tree.DecisionTreeRegressor()
dtreg=dtreg.fit(X,y)
ypred_reg=dtreg.predict([[7]])
print("predicted regression value for x is ",ypred_reg)
'''
the first decision tree algorithm was ID3, then C4.5, then C5.0 then CART. 
CART is the algorithm implemented by sklearn. but it does not support categorical variables yet .i.e needs those to be numerically encoded

ID3 (Iterative dichotomizer 3 ) : target should be categorical; features also to be categorical
C4.5 : Features can be continuous; target should be categorical
C5.0: Less memory usage; more efficient
CART: features/target can be continuous

DecisionTreeClassifier
y is expected to be integer 

DecisionTreeREGRESSOR
y is expected to be floating point value

'''
