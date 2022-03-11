import textblob


def calculate_sentiment(hostel, reviews):
    sentiment = 0.0
    for review in reviews:
        sentiment += textblob.TextBlob(review.comment).sentiment.polarity
    hostel.sentiment = sentiment
    hostel.save()