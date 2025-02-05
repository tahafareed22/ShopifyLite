class RecommendationService:
    """Filters products based on category and budget."""

    def __init__(self, products):
        self.products = products

    def filter_products(self, category, budget):
        """Filter products by category and budget."""
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

        return recommendations[:5] if recommendations else [{"name": "No results found.", "price": 0, "image": ""}]
