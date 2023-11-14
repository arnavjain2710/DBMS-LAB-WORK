import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Data Preprocessing
train_spam_files = [open(os.path.join("train_spam", filename), "r").read() for filename in os.listdir("train_spam")]
train_not_spam_files = [open(os.path.join("train_not_spam", filename), "r").read() for filename in os.listdir("train_not_spam")]
test_spam_files = [open(os.path.join("test_spam", filename), "r").read() for filename in os.listdir("test_spam")]
test_not_spam_files = [open(os.path.join("test_not_spam", filename), "r").read() for filename in os.listdir("test_not_spam")]

# Create labels for spam and not spam
train_spam_labels = [1] * len(train_spam_files)
train_not_spam_labels = [0] * len(train_not_spam_files)
test_spam_labels = [1] * len(test_spam_files)
test_not_spam_labels = [0] * len(test_not_spam_files)

# Combine the data and labels for training and testing sets
train_data = train_spam_files + train_not_spam_files
train_labels = train_spam_labels + train_not_spam_labels
test_data = test_spam_files + test_not_spam_files
test_labels = test_spam_labels + test_not_spam_labels

# Step 2: Feature Extraction
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(train_data)
X_test = vectorizer.transform(test_data)

# Step 3: Naive Bayes Model
clf = MultinomialNB()
clf.fit(X_train, train_labels)

# Step 4: Model Evaluation
y_pred = clf.predict(X_test)
accuracy = accuracy_score(test_labels, y_pred)
report = classification_report(test_labels, y_pred)

print("Naive Bayes Model")
print("Accuracy: {:.2f}%".format(accuracy * 100))
print("Classification Report:\n", report)



from sklearn.svm import SVC

clf = SVC(kernel='linear')  # You can choose different kernel functions, e.g., 'linear', 'rbf', 'poly', etc.

clf.fit(X_train, train_labels)


# Model Evaluation
y_pred = clf.predict(X_test)
accuracy = accuracy_score(test_labels, y_pred)
report = classification_report(test_labels, y_pred)

print("SVC Model")
print("Accuracy: {:.2f}%".format(accuracy * 100))
print("Classification Report:\n", report)


from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=100, random_state=42)  # You can adjust the number of estimators as needed.

clf.fit(X_train, train_labels)

# Model Evaluation
y_pred = clf.predict(X_test)
accuracy = accuracy_score(test_labels, y_pred)
report = classification_report(test_labels, y_pred)

print("RandomForestClassifier Model")
print("Accuracy: {:.2f}%".format(accuracy * 100))
print("Classification Report:\n", report)


from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors=5)  # You can adjust the number of neighbors as needed.

clf.fit(X_train, train_labels)

# Model Evaluation
y_pred = clf.predict(X_test)
accuracy = accuracy_score(test_labels, y_pred)
report = classification_report(test_labels, y_pred)


print("KNN Model")
print("Accuracy: {:.2f}%".format(accuracy * 100))
print("Classification Report:\n", report)


from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(solver='liblinear', max_iter=1000)  # You can adjust solver and other hyperparameters as needed.

clf.fit(X_train, train_labels)

# Model Evaluation
y_pred = clf.predict(X_test)
accuracy = accuracy_score(test_labels, y_pred)
report = classification_report(test_labels, y_pred)


print("LogisticRegression Model")
print("Accuracy: {:.2f}%".format(accuracy * 100))
print("Classification Report:\n", report)