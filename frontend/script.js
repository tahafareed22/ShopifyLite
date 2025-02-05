document.getElementById('productForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    // User inputs
    const category = document.getElementById('category').value;
    const budget = document.getElementById('budget').value;

    // Submit
    const submitButton = document.querySelector('button');
    const recommendationsDiv = document.getElementById('recommendations');

    // Disable the button to prevent multiple clicks
    submitButton.disabled = true;

    // Loading Messaage
    recommendationsDiv.innerHTML = '<p>Loading recommendations...</p>';

    try {
        // Send request to the backend
        const response = await fetch('http://127.0.0.1:5000/recommend', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ category, budget }),
        });

        // Check if response is okay
        if (!response.ok) throw new Error('Network response was not ok');

        const data = await response.json();


        // Update the recommendations
        updateRecommendationsUI(data.recommendations, recommendationsDiv);
    } catch (error) {
        console.error('Error:', error);
        recommendationsDiv.innerHTML = '<p>An error occurred while fetching recommendations. Please try again later.</p>';
    } finally {
        // Re-enable the submit button
        submitButton.disabled = false;
    }
});

/**
 * Update the recommendations section in the UI.
 * @param {Array} recommendations - List of recommended products.
 * @param {HTMLElement} container - Container for displaying recommendations.
 */
function updateRecommendationsUI(recommendations, container) {
    // Check if there are no recommendations or if the first recommendation indicates "No results found."
    if (recommendations.length === 0 || recommendations[0].name === 'No results found.') {
         // Display no results found
        container.innerHTML = '<p>No results found.</p>';
        return;
    }

    // Build the HTML recommendations
    let html = '<h2>Recommended Products:</h2><ul>';
    recommendations.forEach(product => {
        // add a list item with its name, price, and an image for each product
        html += `
            <li>
                <strong>${product.name}</strong> - $${product.price}
                <br>
                <img src="${product.image}" alt="${product.name}" style="max-width: 100px; margin-top: 10px;">
            </li>
        `;
    });
    html += '</ul>';

    container.innerHTML = html;
}
