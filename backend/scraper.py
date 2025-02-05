import requests


class ProductScraper:
    """Handles fetching products from the Fake Store API."""

    API_URL = "https://fakestoreapi.com/products"

    def __init__(self):
        self.products = self.fetch_products()

    def fetch_products(self):
        """Fetch all products from the API."""
        try:
            response = requests.get(self.API_URL)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching products: {e}")
            return []

    def filter_products(self, category, budget):
        """Filter products based on category and budget."""
        recommendations = []

        for product in self.products:
            try:
                name = product.get('title')
                price = float(product.get('price'))
                product_category = product.get('category')
                image = product.get('image')

                # Filter by category
                if category != "all" and product_category != category:
                    continue

                # Filter by budget
                if budget == "low" and price < 50:
                    recommendations.append({"name": name, "price": price, "image": image})
                elif budget == "medium" and 50 <= price <= 100:
                    recommendations.append({"name": name, "price": price, "image": image})
                elif budget == "high" and price > 100:
                    recommendations.append({"name": name, "price": price, "image": image})
            except Exception as e:
                print(f"Error processing product: {e}")
                continue

        # Return recommendations or a fallback
        if not recommendations:
            return [{"name": "No results found.", "price": "", "image": ""}]
        return recommendations[:5]  # Return top 5 recommendations
