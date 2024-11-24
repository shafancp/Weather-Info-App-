# Weather Info App

This project is a Flask-based web application that retrieves and displays current weather information and hourly forecasts for a specified location. It uses **Selenium WebDriver** to scrape data from Google.

---

## Features

- Displays **current temperature**, **time**, **date**, and **weather condition** for a given location.
- Provides an **hourly forecast** with temperature and time details.
- Includes a **search feature** to find weather information for any city.
- **Headless browser** operation using Selenium for smooth data scraping.

---

## Prerequisites

### System Requirements

- Python 3.8 or higher
- Google Chrome browser installed
- Compatible ChromeDriver for your system

### Python Libraries

- Flask
- Selenium

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shafancp/weather-info-app.git
   cd weather-info-app
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download ChromeDriver:**
   - Visit the [ChromeDriver downloads page] (https://developer.chrome.com/docs/chromedriver/downloads) and download the version compatible with your Chrome browser.
   - Place the ChromeDriver in an accessible directory and update its path in the script (`Service` object in `app.py`).

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Access the app:**
   Open `http://127.0.0.1:5000/` in your browser.

---

## File Structure

```
weather-info-app/
│
├── app.py                # Main Flask application
├── templates/
│   └── weather.html       # HTML template for weather display
├── static/
│   ├── styles.css         # CSS for styling the application
│   └── icon/search.png    # Icon for the search button
└── README.md              # Documentation
```

---

## Usage

1. Open the app in your browser.
2. By default, the weather for **Mumbai** is displayed.
3. Enter a location in the search box and click the **search button** to view weather information for that city.

---

## Troubleshooting

1. **ChromeDriver Error:** Ensure the ChromeDriver path in `app.py` matches the actual location of your ChromeDriver binary.
2. **Weather Elements Not Found:** Google may update its structure. Update the `By.ID` and `By.CLASS_NAME` selectors in the script if necessary.
3. **Timeout Error:** Increase `time.sleep(5)` to allow the page to load completely.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

### Notes

- **Disclaimer:** This project scrapes data from Google. Ensure usage complies with the website's terms of service.
- **Future Improvements:**
  - Add support for multiple languages.
  - Integrate a weather API (e.g., OpenWeatherMap) to replace web scraping.

---

Feel free to customize this README to suit your project!
