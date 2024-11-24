from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def weather():
    area = "Mumbai" #default

    if request.method == "POST":
        area = request.form.get("location", area).strip()

    url = f"https://www.google.com/search?q=weather+{area}"

    # Set up the Selenium WebDriver
    service = Service('path to chromedriver')  # Replace with your path
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(5)

        # Fetch current weather details
        temperature = driver.find_element(By.ID, "wob_tm").text.strip()
        time_date = driver.find_element(By.ID, "wob_dts").text.strip()
        condition = driver.find_element(By.ID, "wob_dc").text.strip()

        # Fetch hourly forecast
        target_classes = [
            "wob_t wob_gs_l3",
            "wob_t wob_gs_l6",
            "wob_t wob_gs_l9",
            "wob_t wob_gs_l12",
            "wob_t wob_gs_l15",
            "wob_t wob_gs_l18",
            "wob_t wob_gs_l21"
        ]

        forecast = []
        for target_class in target_classes:
            elements = driver.find_elements(By.CLASS_NAME, target_class.split()[-1])  # Match last class name
            for element in elements:
                if element.get_attribute("class") == target_class:
                    aria_label = element.get_attribute("aria-label")
                    if aria_label and "Celsius" in aria_label:  # Filter Celsius values
                        temp = aria_label.split("Celsius")[0].strip()
                        time_label = aria_label.split(",")[1].strip()
                        forecast.append({"temp": temp, "time": time_label})

    finally:
        driver.quit()

    return render_template("weather.html", area=area, temperature=temperature, time_date=time_date, condition=condition, forecast=forecast)

if __name__ == "__main__":
    app.run(debug=True)

