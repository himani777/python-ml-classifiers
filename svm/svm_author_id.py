#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]



#########################################################
### your code goes here ###

from sklearn.svm import SVC
#clf = SVC(kernel="linear")

clf = SVC(C=10000.0,kernel="rbf")
t0 = time()
clf=clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred=clf.predict(features_test)
print "training time:", round(time()-t1, 3), "s"
from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, pred)

print(acc)

a1=pred[26]
a2=pred[50]
a3=pred[10]

print a1,a2,a3
count=0

for i in range(1, len(pred)):
	if pred[i]==1:
		count=count+1


print (count)
print len(pred)

#########################################################


