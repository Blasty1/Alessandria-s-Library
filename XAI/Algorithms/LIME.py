import lime
import lime.lime_text
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
import numpy as np


data = load_files("Algorithms/data/aclImdb/train", categories=["pos", "neg"], encoding="utf-8",
    decode_error="replace")

X = np.array(data.data)
y = data.target # Directly use data.target without further transformation


X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2, random_state=42,stratify=y)

vectorizer = TfidfVectorizer()
classifier = LogisticRegression(random_state=42, max_iter=1000)
pipeline = make_pipeline(vectorizer, classifier)

pipeline.fit(X_train,y_train)

# 5. Initialize the LIME explainer
explainer = lime.lime_text.LimeTextExplainer(class_names=["NEGATIVE", "POSITIVE"])

text_instance = X_test[0]
exp = explainer.explain_instance(text_instance, pipeline.predict_proba,num_features=10)

exp.save_to_file("lime_explanation.html")
print("LIME explanation saved as ’lime_explanation.html’")