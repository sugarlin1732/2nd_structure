from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np
f = open("/home/sugarlin1732/2nd_structure/feature.txt", "r")
e = open("/home/sugarlin1732/2nd_structure/structure_label.txt", "r")
o = open("/home/sugarlin1732/2nd_structure/RF_2SP(0.3test)_depth_loop.txt", "w")
feature = list()
label = list()


for line in f.readlines():
    line = line.strip("\n").rstrip().split(" ")
    line = list(map(eval, line))
    feature.append(line)


for line in e.readlines():
    line = line.strip("\n")
    label.append(line)

x_train, x_test, y_train, y_test = train_test_split(
    feature, label, test_size=.3)

"""
x_train = feature
y_train = label
x_test = feature
y_test = label
"""

depth = [1, 2, 5, 10]
for i in depth:
    clf = RandomForestClassifier(n_estimators=200, oob_score=True, n_jobs=-1, random_state=0,
                                 max_features="auto", max_depth=i)
    clf.fit(x_train, y_train)

    print(clf.classes_, file=o)
    print(clf.predict_proba(x_test), file=o)
    print("max_depth =", i, file=o)
    print(clf.score(x_test, y_test), file=o)


"""
clf = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                             max_depth=2, max_features='auto', max_leaf_nodes=None,
                             min_impurity_decrease=0.0, min_impurity_split=None,
                             min_samples_leaf=1, min_samples_split=2,
                             min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=-1,
                             oob_score=False, random_state=0, verbose=0, warm_start=False)

clf.fit(x_train, y_train)
print(clf.classes_, file=o)
print(clf.get_params(), file=o)
print(clf.predict_proba(x_test), file=o)
print(clf.score(x_test, y_test), file=o)
"""


f.close
e.close
o.close
