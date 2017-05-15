import os
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn import linear_model
from sklearn.metrics import classification_report

if __name__ == '__main__':

    if len(sys.argv) < 1:
        sys.exit(1)

    data_dir = sys.argv[1]
    classes = ['pos', 'neg']

    train_data = []
    test_data = []
    train_labels = []
    test_labels = []

    for current_class in classes:
        current_path = os.path.join(data_dir, current_class)
        for current_file in os.listdir(current_path):
            with open(os.path.join(current_path, current_file), 'r') as open_file:
                content = open_file.read()
                if current_file.startswith('cv9'):
                    test_data.append(content)
                    test_labels.append(current_class)
                else:
                    train_data.append(content)
                    train_labels.append(current_class)

    vectorizer = TfidfVectorizer(min_df=5, max_df=0.8, sublinear_tf=True, use_idf=True)
    train_vectors = vectorizer.fit_transform(train_data)
    test_vectors = vectorizer.transform(test_data)
    print test_vectors

    # Linear Support Vector Machines
    classifier_svm = svm.LinearSVC()
    classifier_svm.fit(train_vectors, train_labels)
    prediction_svm = classifier_svm.predict(test_vectors)
    print(classification_report(test_labels, prediction_svm))

    # Logistic Regression
    classifier_reg = linear_model.LogisticRegression()
    classifier_reg.fit(train_vectors, train_labels)
    prediction_reg = classifier_reg.predict(test_vectors)
    print(classification_report(test_labels, prediction_reg))

    from Tkinter import *

    master = Tk()

    Label(master, text="Enter your movie review:").grid(row=0)

    review = Entry(master)
    review.grid(row=1, column=0)

    prediction = Label(master)
    prediction.grid(row=5)

    def predict_sentiment():
        review_vectors = vectorizer.transform([review.get()])
        review_sentiment = classifier_svm.predict(review_vectors)
        print (review_sentiment)
        if classes.index(review_sentiment) == 0:
            prediction.configure(text="You enjoyed the movie! :)")
        else:
            prediction.configure(text="You did not enjoy the movie... :(")
        review.delete(0, END)

    Button(master, text='Submit', command=predict_sentiment).grid(row=3, column=0, sticky=W, pady=4)

    mainloop()
