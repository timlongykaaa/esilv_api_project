import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def get_data():
    url = "https://blog-ia.com/blog/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles_data = []
    articles = soup.find_all('article')

    for article in articles:
        title_element = article.find('h2')
        title = title_element.get_text(strip=True) if title_element else "Titre non trouvé"
        link_element = title_element.find('a')
        link = link_element['href'] if link_element else "Lien non trouvé"

        articles_data.append({
            'title': title,
            'link': link
        })

    return articles_data

def get_article_content(article_number):
    articles_data = get_data()
    if 0 <= article_number < len(articles_data):
        article_url = articles_data[article_number]['link']

        if not article_url.startswith(('http://', 'https://')):
            raise ValueError(f"URL invalide pour l'article: {article_url}")

        response = requests.get(article_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        content_element = soup.find('main')
        article_content = content_element.get_text(strip=True) if content_element else "Contenu non trouvé"

        return article_content
    else:
        return "Numéro d'article invalide ou hors limites."

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)

    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        sentiment_summary = 'positif'
    elif compound_score <= -0.05:
        sentiment_summary = 'négatif'
    else:
        sentiment_summary = 'neutre'


    return {
        'scores': sentiment_scores,
        'summary': sentiment_summary
    }


