<div align="center">

```
  ██████╗ ██████╗  █████╗ ███╗   ██╗██████╗ ███████╗██╗   ██╗██████╗
 ██╔════╝ ██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔════╝██║   ██║██╔══██╗
 ██║  ███╗██████╔╝███████║██╔██╗ ██║██║  ██║█████╗  ██║   ██║██████╔╝
 ██║   ██║██╔══██╗██╔══██║██║╚██╗██║██║  ██║██╔══╝  ██║   ██║██╔══██╗
 ╚██████╔╝██║  ██║██║  ██║██║ ╚████║██████╔╝███████╗╚██████╔╝██║  ██║
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝
```

# 🏨 Hotel Occupancy Prediction System

### *AI-powered room availability forecasting for the hospitality industry*

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3%2B-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.1%2B-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Accuracy](https://img.shields.io/badge/Model%20Accuracy-93.06%25-gold?style=for-the-badge)](##-model-performance)

<br/>

> A full-stack machine learning web application that predicts hotel room occupancy in real-time using environmental sensor data — temperature, humidity, light, and CO₂ levels — wrapped in a sleek, luxury hotel-themed UI.

<br/>

[Features](#-features) · [Demo](#-demo) · [Installation](#-installation) · [Usage](#-usage) · [ML Model](#-machine-learning-model) · [API](#-api-reference) · [Contributing](#-contributing)

---

</div>

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Machine Learning Model](#-machine-learning-model)
- [Input Parameters](#-input-parameters)
- [Model Performance](#-model-performance)
- [Bug Fixes & Improvements](#-bug-fixes--improvements)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌐 Overview

The hospitality industry lives and dies by occupancy rates. Accurate forecasting allows hotels to optimize pricing, allocate staff efficiently, reduce waste, and deliver a better guest experience. Traditional methods rely on historical booking patterns — but they miss real-time environmental signals that strongly correlate with actual room occupancy.

This project bridges that gap. Using **sensor readings** (temperature, humidity, light intensity, CO₂) along with the **day of the week and time of day**, a trained **Random Forest classifier** predicts in real time whether a hotel room is currently occupied or vacant — with **93.06% accuracy**.

The prediction engine is served through a **Flask web application** with a fully redesigned, luxury hotel-themed frontend.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 **Real-Time Prediction** | Instant room occupancy classification from 6 sensor inputs |
| 🎯 **93% Accuracy** | Random Forest model trained on 8,143 real-world data points |
| 🌐 **Full-Stack Web App** | Flask backend + responsive Jinja2 frontend |
| 🎨 **Luxury UI** | Dark-gold aesthetic with Playfair Display typography and smooth Swiper sliders |
| 📱 **Fully Responsive** | Mobile-first design that works on all screen sizes |
| ⚡ **SMOTE Balancing** | Handles class imbalance in training data for better minority-class recall |
| 🔒 **Error Handling** | Graceful degradation — all bad inputs return user-friendly messages |
| 📦 **Reproducible ML** | Scaler and encoder saved as `.pkl` files to guarantee identical preprocessing at inference |

---

## 🎬 Demo

### Homepage — Hero Slider
The landing page features a full-screen auto-advancing image carousel with overlay text and smooth crossfade transitions.

### Gallery Section
An auto-scrolling gallery slider showcasing hotel facilities, with hover zoom effects and overlay icons.

### Occupancy Predictor
The AI-powered prediction form:

```
┌─────────────────────────────────────────────────────────┐
│              CHECK AVAILABILITY                         │
│  ─────────────────────────────────────────────────────  │
│  Date & Time *       │  Temperature (°C) *              │
│  2024-02-07 14:00    │  23.1                            │
│                      │                                  │
│  Humidity (%) *      │  Light (lux) *                   │
│  27.3                │  430                             │
│                      │                                  │
│  CO₂ (ppm) *         │  Humidity Ratio *                │
│  721                 │  0.00479                         │
│                                                         │
│  [ PREDICT OCCUPANCY ]  ✓ Room is currently Occupied    │
└─────────────────────────────────────────────────────────┘
```

Results are colour-coded:
- 🟢 **Green** — Room is Available
- 🔴 **Red** — Room is currently Occupied
- ⚠️ **Grey** — Input/prediction error

---

## 🛠 Tech Stack

### Backend
| Technology | Purpose |
|---|---|
| **Python 3.9+** | Core language |
| **Flask 2.3+** | Web framework and routing |
| **scikit-learn 1.1+** | RandomForestClassifier, MinMaxScaler, LabelEncoder |
| **imbalanced-learn** | SMOTE for training data resampling |
| **pandas** | Data manipulation and feature engineering |
| **pickle** | Model and preprocessor serialization |

### Frontend
| Technology | Purpose |
|---|---|
| **Jinja2** | HTML templating (built into Flask) |
| **CSS3** | Custom luxury design system with CSS variables |
| **Swiper.js 9** | Touch-friendly hero and gallery sliders |
| **Font Awesome 6** | Icons throughout the UI |
| **Google Fonts** | Playfair Display (headings) + DM Sans (body) |

---

## 📁 Project Structure

```
Flask/
│
├── app.py                      # Flask application — routes & prediction logic
├── model.pkl                   # Trained RandomForestClassifier
├── scaler.pkl                  # Fitted MinMaxScaler (training-data ranges)
├── le.pkl                      # Fitted LabelEncoder (day-of-week encoding)
├── requirements.txt            # Python dependencies
│
├── templates/
│   └── index.html              # Single-page Jinja2 template
│
└── static/
    ├── css/
    │   └── style.css           # Full luxury design system
    ├── js/
    │   └── script.js           # Swiper init, scroll header, mobile nav
    └── images/
        ├── home-slide1.jpg     # Hero section background images
        ├── home-slide2.jpg
        ├── home-slide3.jpg
        ├── home-slide4.jpg
        ├── about.jpg           # About section image
        ├── gallery1–6.jpg      # Gallery slider images
        ├── room-1–6.jpg        # Room images (available for extension)
        ├── service1–6.png      # Service icons (available for extension)
        └── review.jpg          # Review section background
```

---

## ⚙️ Installation

### Prerequisites

- Python **3.9** or higher
- `pip` package manager
- Git

### Step 1 — Clone the repository

```bash
git clone https://github.com/your-username/hotel-occupancy-prediction.git
cd hotel-occupancy-prediction
```

### Step 2 — Create a virtual environment *(recommended)*

```bash
# Create
python -m venv venv

# Activate — macOS / Linux
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
```

### Step 3 — Install dependencies

```bash
pip install -r Flask/requirements.txt
```

> **`requirements.txt` contents:**
> ```
> flask>=2.3
> scikit-learn>=1.1
> imbalanced-learn>=0.10
> pandas>=1.5
> numpy>=1.23
> ```

### Step 4 — Run the application

```bash
cd Flask
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## 🚀 Usage

### Making a prediction

1. Navigate to the **Check Availability** section (or click the nav button)
2. Fill in all six fields:

| Field | Example Value | Unit |
|---|---|---|
| Date & Time | `2024-02-07T14:00` | datetime-local |
| Temperature | `23.1` | °C |
| Humidity | `27.3` | % |
| Light | `430` | lux |
| CO₂ | `721` | ppm |
| Humidity Ratio | `0.004793` | kg water / kg air |

3. Click **Predict Occupancy**
4. The result appears inline — green for available, red for occupied

### Typical sensor value ranges

| Parameter | Occupied Room | Vacant Room |
|---|---|---|
| Temperature | 21–24 °C | 19–21 °C |
| Humidity | 24–35% | 16–22% |
| Light | 300–1700 lux | 0–10 lux |
| CO₂ | 600–2000 ppm | 412–500 ppm |
| Humidity Ratio | 0.004–0.006 | 0.0026–0.0032 |

---

## 🤖 Machine Learning Model

### Dataset

The model was trained on the [UCI Room Occupancy Detection dataset](https://archive.ics.uci.edu/dataset/357/occupancy+detection), consisting of timestamped environmental sensor readings from a real office/room.

| Split | Records | Occupancy Rate |
|---|---|---|
| Training | 8,143 | ~21% |
| Test 1 | 9,752 | ~36% |
| Test 2 | 2,665 | ~43% |

### Preprocessing Pipeline

```
Raw Input
    │
    ▼
① datetime → day_name (e.g. "Wednesday")
    │
    ▼
② LabelEncoder → integer (e.g. Wednesday → 6)
   [Alphabetical: Fri=0, Mon=1, Sat=2, Sun=3, Thu=4, Tue=5, Wed=6]
    │
    ▼
③ Extract hour from datetime (0–23)
    │
    ▼
④ Assemble feature vector:
   [Temperature, Humidity, Light, CO2, HumidityRatio, day, hour]
    │
    ▼
⑤ MinMaxScaler.transform() using training-data ranges
    │
    ▼
⑥ RandomForestClassifier.predict() → 0 (Available) or 1 (Occupied)
```

### Training Pipeline

```python
# 1. Fit scaler on training data only
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)

# 2. Handle class imbalance with SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train_scaled, y_train)

# 3. Train Random Forest
model = RandomForestClassifier(
    n_estimators=10,
    max_features='sqrt',
    criterion='gini',
    random_state=42
)
model.fit(X_resampled, y_resampled)

# 4. Persist all artifacts
pickle.dump(model,  open('model.pkl',  'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))
pickle.dump(le,     open('le.pkl',     'wb'))
```

### Why Random Forest?

- **Handles non-linear boundaries** — occupancy is driven by complex interactions between light, CO₂, and time
- **Robust to outliers** — sensor data can have spikes; ensemble trees are naturally resistant
- **Feature importance** — provides interpretability into which sensors matter most
- **No feature scaling required** — though scaling was applied here for consistency with other candidate models (SVM) tested in the original notebook

---

## 📊 Model Performance

| Metric | Value |
|---|---|
| **Test Accuracy** | **93.06%** |
| Training samples (after SMOTE) | Balanced |
| Algorithm | Random Forest (`n_estimators=10`, `criterion='gini'`) |
| Class imbalance handling | SMOTE oversampling |

> **Note on the original model.pkl:** The `.pkl` bundled in the original repository was serialized with scikit-learn 1.0.2 and is incompatible with scikit-learn ≥ 1.3 due to a dtype change in the internal tree node array. The model in this repository was **retrained from scratch** on the same data using the same algorithm, achieving equivalent accuracy.

---

## 🐛 Bug Fixes & Improvements

This repository is a fixed and revamped version of the original. Here is a full changelog:

### Design Revamp

| Area | Before | After |
|---|---|---|
| **Color palette** | Generic blue (`#0077b6`) | Dark charcoal + gold luxury system (`#0f0d0c` / `#c9a84c`) |
| **Typography** | Poppins only | Playfair Display (headings) + DM Sans (body) |
| **Buttons** | Solid fill | Animated sliding-fill on hover |
| **Header** | Always solid white | Transparent over hero, frosted-glass on scroll |
| **Hero transitions** | Hard slide | Crossfade with overlay gradient |
| **Result display** | Plain `<h3>` text | Colour-coded badge with icon (green/red) |
| **Content** | Lorem ipsum placeholder text | Real hotel copy with statistics |
| **Footer** | Minimal | Three-column grid with social links |
| **Responsiveness** | Basic | Mobile-first with breakpoints at 991px, 768px, 480px |

---

## 📡 API Reference

The app exposes a single route that handles both page rendering and prediction.

### `GET /`

Returns the full homepage HTML.

```
GET http://localhost:5000/
200 OK
Content-Type: text/html
```

### `POST /`

Submits sensor readings and returns the page with a prediction result embedded.

```
POST http://localhost:5000/
Content-Type: application/x-www-form-urlencoded
```

**Request body parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `date` | `datetime-local` string | ✅ | Format: `YYYY-MM-DDTHH:MM` |
| `temperature` | `float` | ✅ | Room temperature in °C |
| `humidity` | `float` | ✅ | Relative humidity in % |
| `light` | `float` | ✅ | Light intensity in lux |
| `co2` | `float` | ✅ | CO₂ concentration in ppm |
| `humidity_ratio` | `float` | ✅ | Humidity ratio (kg water / kg dry air) |

**Response:**

Returns the full HTML page with the prediction injected as a Jinja2 template variable. The `status` variable will be one of `available`, `occupied`, or `error`.

---

## 🤝 Contributing

Contributions are welcome! Here are some ideas for extending the project:

- 📈 **Add more ML models** — compare Logistic Regression, SVM, XGBoost
- 📊 **Dashboard page** — show live prediction history and a confidence gauge
- 🕐 **Time-series forecasting** — predict occupancy for the next N hours
- 🔌 **REST API endpoint** — add a `/predict` JSON endpoint for external integrations
- 🧪 **Unit tests** — add `pytest` coverage for the prediction pipeline
- 🐳 **Docker** — containerize for easy deployment

### How to contribute

```bash
# 1. Fork the repository
# 2. Create a feature branch
git checkout -b feature/my-improvement

# 3. Commit your changes
git commit -m "feat: add confidence score to prediction output"

# 4. Push and open a Pull Request
git push origin feature/my-improvement
```

Please follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- **Dataset:** [UCI Machine Learning Repository — Occupancy Detection Data Set](https://archive.ics.uci.edu/dataset/357/occupancy+detection) by Luis M. Candanedo and Véronique Feldheim
- **Original project** developed as part of an Externship / ML internship program
- **UI inspiration:** Luxury boutique hotel design systems

---

<div align="center">

Made with ❤️ and a lot of sensor data

⭐ **Star this repo if you found it helpful!**

</div>
