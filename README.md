# Crop-Price-Across-Markets-Map-View-

A multilingual application that displays crop prices across different agricultural markets using interactive tables and map-based view.

## 📌 Features

* 🌍 **Multi-language Support**

  * English
  * Hindi
  * Kannada
  * Tamil
  * Telugu

* 📊 **Interactive Market Price Table**

  * Displays crop prices across markets.
  * Automatically translates market and crop names into the selected language.

* 🗺️ **Geographical Market Visualization**

  * Interactive map powered by PyDeck.
  * Market locations displayed as markers.
  * Hover tooltips show:

    * Market Name
    * Crop Name
    * Price per Quintal

* 🔍 **Crop Filtering**

  * Filter markets based on selected crops.
  * View only relevant market data.

---

## 🏗️ Tech Stack

| Technology      | Purpose                   |
| --------------- | ------------------------- |
| Streamlit       | Web Application Framework |
| Pandas          | Data Handling             |
| PyDeck          | Interactive Maps          |
| Deep Translator | Language Translation      |

---

## 📂 Project Structure

```text
crop-market-app/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/crop-market-app.git

cd crop-market-app
```

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

Create a file named `requirements.txt`

```txt
streamlit
pandas
pydeck
deep-translator
```

Install:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

Default URL:

```text
http://localhost:8501
```

---

## 📊 Sample Dataset

| Market           | Crop    | Price/Quintal (₹) |
| ---------------- | ------- | ----------------- |
| Kolar Market     | Rice    | 2200              |
| Mysore Market    | Wheat   | 2400              |
| Bangalore Market | Maize   | 1800              |
| Tumkur Market    | Millets | 2600              |

---

## 🌐 Supported Languages

| Language | Code |
| -------- | ---- |
| English  | en   |
| Hindi    | hi   |
| Kannada  | kn   |
| Tamil    | ta   |
| Telugu   | te   |

---

## 🗺️ Map Visualization

The application uses PyDeck's `ScatterplotLayer` to display market locations.

Each marker represents:

* Market location
* Available crop
* Price per quintal

Interactive tooltips provide additional information when hovering over markers.

---

## 🔍 Crop Filter

Users can:

1. Select a crop from the dropdown.
2. View filtered market information.
3. Analyze prices for a specific crop.

---

## 📸 Application Workflow

```text
Select Language
       │
       ▼
View Translated Market Data
       │
       ▼
Explore Market Locations on Map
       │
       ▼
Filter Data by Crop
       │
       ▼
Analyze Prices
```

---

## 🎯 Future Enhancements

* Real-time market price integration via APIs
* Farmer recommendation.
* Price trend forecasting.
* Nearby market suggestions
* Mobile responsive interface


---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Create a Pull Request

---

## 📜 License

This project is released under the MIT License.

---


