import sys
import pandas as pd
import csv
import random
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn import tree

def preProcessing(df,seed,trainPerc):
    #all of the columns in the dataSet
    columns = ["label","id","name","screen_name","statuses_count","followers_count","friends_count","favourites_count","listed_count","url","lang","time_zone",
                "location","default_profile","default_profile_image","geo_enabled","profile_image_url","profile_banner_url","profile_use_background_image",
                "profile_background_image_url_https","profile_text_color","profile_image_url_https","profile_sidebar_border_color","profile_background_tile",
                "profile_sidebar_fill_color","profile_background_image_url","profile_background_color","profile_link_color","utc_offset","is_translator",
                "follow_request_sent","protected","verified","notifications","description","contributors_enabled","following","created_at","timestamp","crawled_at",
                "updated"]
    #columns that are actually relevant that we end up keeping (edit over time to find best attributes)
    columnsToKeep = ["label","statuses_count","followers_count","friends_count","favourites_count","listed_count","lang","time_zone",
                                "location","is_translator",
                                "follow_request_sent","protected","verified","notifications","contributors_enabled","following"]
    columnsToDelete = []
    for i in range(len(columns)): #removing columns 
        if(columns[i] not in columnsToKeep):
            columnsToDelete.append(columns[i])
    df = df.drop(columnsToDelete,axis=1) 
    for column in df.columns[1:]: #one-hot encoding values
        if(df[column].dtype == 'object'):
            df = pd.concat([df,pd.get_dummies(df[column],prefix=column,drop_first=True)],axis=1)
            df.drop([column],axis=1,inplace=True)
    imp = SimpleImputer(strategy="most_frequent") #filling in missing values (sklearn will not accept data if values are missing)
    df = pd.DataFrame(imp.fit_transform(df))
    training = df.sample(frac=trainPerc,random_state=seed) #creating training set
    
    test = df.drop(training.index) #creating test set
    return training,test

def matrix(actual,predicted,labels,approach,dataSet): #takes results from algorithms and creates a csv file matrix
    matrix = []
    for m in range(len(labels)): #creating the template for the matrix
        matrixEntry = [0] * (len(labels)+1)
        matrixEntry[0] = labels[m]
        matrix.append(matrixEntry)
    for p in range(len(predicted)): #filling in the values for the matrix
        predictedIndex = np.where(labels == predicted[p])[0][0]
        actualIndex = np.where(labels == actual[p])[0][0] + 1
        matrix[predictedIndex][actualIndex] += 1
    fileName = "results_"+approach+"_"+dataSet #creates a csv file with the results of the matrix
    file = open(fileName,"w+")
    for i in range(len(matrix)):
        file.write(matrix[i][0]+",")
    file.write("\n")
    for j in range(1,len(matrix)+1):
        for k in range(len(matrix)):
            file.write(str(matrix[k][j])+",")
        file.write(matrix[j-1][0]+"\n")

def main():
    df = pd.read_csv(sys.argv[1])
    trainPerc = float(sys.argv[2])
    seed = int(sys.argv[3])
    training,test= preProcessing(df,seed,trainPerc)
    
    #in order to feed data into the sklearn algorithms, we need to split into y(the labels) and x(the data that determines the labels)
    x_train = training.drop(training.columns[0],axis = 1)  
    y_train = training[training.columns[0]]
    x_test = test.drop(test.columns[0],axis=1)
    y_test = test[test.columns[0]].values
    labels = df[df.columns[0]].unique()
        
    #Decision Tree
    classifier = DecisionTreeClassifier()
    clf = classifier.fit(x_train,y_train)
    tree.export_graphviz(clf,out_file='tree.dot') #to be implemented (trying to figure out how to view tree)
    y_pred = clf.predict(x_test)
    approach = "DecisionTree"
    matrix(y_test,y_pred,labels,approach,"data.csv")

if __name__ == '__main__':
    main()
