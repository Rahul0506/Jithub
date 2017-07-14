from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV

def init_model(dataset_location='.\\txt_sentoken'):
    #Load files and split into train and test sets
    dataset = load_files(dataset_location, shuffle=False, encoding='utf-8')
    files_train, files_test, Y_train, Y_test = train_test_split(dataset.data, dataset.target, test_size=0.1, random_state=None)

    #Create the pipeline for the Vectorizer and Classifier
    text_clf = Pipeline([
                ('vect', TfidfVectorizer(min_df=3, max_df=0.95)),
                ('clf', LinearSVC(C=1110)),
    ])

    #Parameters for the GridSearch
    parameters = {'vect__ngram_range' : [(1, 1), (1, 2)],
    }

    #Create and fit the GridSearch
    gs_clf = GridSearchCV(text_clf, parameters, n_jobs=-1)
    gs_clf.fit(files_train, Y_train)
    return gs_clf

def predict_on(gs_clf, filename):
    #Run on a sample file
    f = open(filename)
    data = f.read()
    f.close()
    return gs_clf.predict([data,])
