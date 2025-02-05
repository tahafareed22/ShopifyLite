# # **ShopifyLite**

ShopifyLite is a web application that recommends products from the **Fake Store API** based on user preferences such as category and budget. 

---

## **Features**
- Fetches real-time product data from the **Fake Store API**.
- Filters recommendations by:
  - **Category** (e.g., Electronics, Jewelry, Men's Clothing, Women's Clothing).
  - **Budget** (Low: under $50, Medium: $50-$100, High: over $100).

---

## **Technologies Used**
### **Frontend:**
- HTML
- CSS
- JavaScript

### **Backend:**
- Python

---

## **Project Structure**
```
ShopifyLite/
│── frontend/
│   ├── index.html      
│   ├── style.css       
│   ├── script.js       
│
│── backend/
│   ├── app.py          
│   ├── scraper.py
│   ├── recommendation.py   
│
└── README.md           
```

---

## **How to Run**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/ShopifyLite.git
cd ShopifyLite
```

### **2. Install Dependencies**
Navigate to the `backend` folder and install Python dependencies:
```bash
cd backend
pip install flask flask-cors requests
```

### **3. Run the Backend**
Start the Flask server from the `backend` directory:
```bash
python app.py
```
The backend will run at: `http://127.0.0.1:5000`.

### **4. Open the Frontend**
Navigate to the `frontend` directory and open `index.html` in your browser:
```bash
file:///<path-to-your-project>/ShopifyLite/frontend/index.html
```

---

## **Usage**
1. Open the application in your browser.
2. Select:
   - A **category** (e.g., Electronics).
   - A **budget range** (e.g., Over $100).
3. Click **Get Recommendations**.
4. Scroll through the recommended products.

---
