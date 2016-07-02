from senti_classifier import senti_classifier

sentences = ['The movie was the worst movie', 'It was the worst acting by the actors']
pos_score, neg_score = senti_classifier.polarity_scores(sentences)
print(pos_score, neg_score)
