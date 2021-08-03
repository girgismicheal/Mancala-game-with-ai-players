 ML All Algorithms
## Naive Bayes
def train_NB(Dataset, Classes):
vocab = set(Dataset.extract_words())
for c_i in Classes:
docs_i = Examples.docs_with_class(c_i)
Priors[c_i] = len(docs_i) / len(Examples)
text_i = concat_strings(docs_i)
n = len(text_i)
for word_k in vocab: #for each word in vocabulary
n_k = count_word(word_k, text_i)
Probs[word_k, c_i] = (n_k + 1) / (n + len(vocab))
return Priors, Probs
def predict_NB(doc, Classes):
words = doc.extract_words()
return argmin([Priors[c_i] * prod([Probs[w_k, c_i] for w_k in words])
for c_i in Classes])
## Linear and Logistic Regression
def Batch_GD(Dataset, num_epochs, learning_rate, cost_gradient):
weights = init_random_weights()
for t in range(num_epochs):
grad_J = 0
for x_i, y_i in Dataset:
grad_J += cost_gradient(x_i, y_i, weights)
weights -= learning_rate * grad_J
return weights
def stochastic_GD(Dataset, num_epochs, learning_rate, cost_gradient):
weights = init_random_weights()
for t in range(num_epochs):
for x_i, y_i in Dataset:
grad_J = cost_gradient(x_i, y_i, weights)
weights -= learning_rate * grad_J
return weights
## KNN
def predict_KNN(Dataset, x_new, k):
y_preds = get_closest_k(x_new, Dataset, dist_fn, k)
return mode(y_preds)