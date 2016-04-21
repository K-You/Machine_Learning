#Machine Learning -> Apple or Orange? 
​
from sklearn import tree
​
#features : [weight, texture]
#texture : 0 bumpy 1 smooth
features = [[140, 1],[130, 1],[150, 0],[170, 0]]
​
#labels : [1 apple 0 orange]
labels = [0, 0, 1, 1]
​
#Create the classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
​
#Let's predict a new fruit :D 
​
result = clf.predict([[160,0]])
​
​
#Ooooooh precious
print(result)