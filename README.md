# ToxBlocker
Technica 2021 Hackathon project
Devpost link: [https://devpost.com/software/toxicitydetector]

Social media can be a breeding ground for nefarious actors promoting hate and toxicity at the expense of other users, who are sadly subjected to this content. For users who want to avoid toxic content online,  we need a mechanism for identifying such content and alerting users to its presence. That's where ToxBlocker comes in.

## Usage
- Download this dataset of social media comments and toxicity labels from Kaggle: [https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/overview]
- Run the notebook ToxBlocker.ipynb to pull in the data, perform Natural Language Processing, and train save the LSTM model
- Run the app.py file using Flask
- Open the HTML file in a browser (only tested with Google Chrome) to launch the Web App and interact with it

## About the Project
- The model is built in Python, using Keras and the training data came from Kaggle.
- The model architecture is an LSTM, which is a type of Recurrent Neural Network that captures spatial patterns in sequences (in this case sequences of words embedded as vectors).
- The front end is built in JavaScript, Flask, and HTML.

### Related Resources and References
- https://blog.insightdatascience.com/how-to-solve-90-of-nlp-problems-a-step-by-step-guide-fda605278e4e
- https://www.jitsejan.com/python-and-javascript-in-flask
- https://towardsdatascience.com/talking-to-python-from-javascript-flask-and-the-fetch-api-e0ef3573c451
- https://towardsdatascience.com/classifying-toxicity-in-online-comment-forums-end-to-end-project-57720af39d0b
