from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import ProductScraper


class FlaskApp:
    """Encapsulates the Flask application and routes."""

    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)  # Enable CORS for cross-origin requests
        self.scraper = ProductScraper()  # Initialize 

        # Define routes
        self.app.route('/recommend', methods=['POST'])(self.recommend)

    def recommend(self):
        """Handle POST requests to provide product recommendations."""
        data = request.json
        category = data.get('category', 'all')
        budget = data.get('budget', 'medium')

        # Get recommendations 
        recommendations = self.scraper.filter_products(category, budget)
        return jsonify({"recommendations": recommendations})

    def run(self):
        """Run the Flask app."""
        self.app.run(debug=True)


# Run Flask
if __name__ == '__main__':
    FlaskApp().run()
