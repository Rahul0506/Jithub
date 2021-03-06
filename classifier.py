from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

def train_model(dataset_location):
    #Load files and split into train and test sets
    dataset = load_files(dataset_location, shuffle=False, encoding='utf-8')
    files_train = dataset.data
    Y_train = dataset.target
    
    #Create the pipeline for the Vectorizer and Classifier
    text_clf = Pipeline([
                ('vect', TfidfVectorizer(min_df=3, max_df=0.95, ngram_range=(1,2))),
                ('clf', LinearSVC(C=1110)),
    ])

    text_clf.fit(files_train, Y_train)
    return text_clf

def predict(text_clf, data):
    return text_clf.predict((data,))
