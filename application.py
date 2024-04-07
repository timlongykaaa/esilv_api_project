from flask import Flask, jsonify, render_template
import scraper

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/get_data', methods=['GET'])
def get_data():
    articles = scraper.get_data()
    return jsonify(articles)

@application.route('/articles', methods=['GET'])
def list_articles():
    articles = scraper.get_data()
    summaries = [{'title': article['title'], 'link': article['link'], 'author': article['author'], 'date': article['date']} for article in articles]
    return jsonify(summaries)

@application.route('/article/<int:number>', methods=['GET'])
def article_detail(number):
    content = scraper.get_article_content(number)
    if content != "Numéro d'article invalide ou hors limites.":
        return jsonify({'content': content})
    else:
        return jsonify({'error': content}), 404

@application.route('/ml/<int:number>', methods=['GET'])
def sentiment_analysis(number):
    try:
        content = scraper.get_article_content(number)
        if content == "Numéro d'article invalide ou hors limites.":
            return jsonify({'error': content}), 404
        sentiment = scraper.analyze_sentiment(content)
        return jsonify(sentiment)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    application.run(debug=True)
