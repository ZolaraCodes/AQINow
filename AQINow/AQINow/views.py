import requests
from django.shortcuts import render

# Dictionary to map category names to descriptions
category_descriptions = {
    "Good": "(0-50) This air quality reading is satisfactory and poses little or no risk! Enjoy you day!",
    "Moderate": "(51-100) Due to the risk of respiratory illness symptoms, sensitive groups should greatly reduce outdoor exercise. Avoid ventilating indoor spaces with outdoor air. Air purifiers should be turned on.",
    "Unhealthy for Sensitive Groups": "(101-150) Everyone is at risk for eye, skin, and throat irritation as well as respiratory problems. greatly reduce or avoid outdoor exercise. Avoid ventilating indoor spaces with outdoor air.",
    "Unhealthy": "(151-200) Increased likelihood of heart and lung aggravation as well as health impacts for everyone. Avoid and wear a pollution mask outdoors. Ventilation is discouraged. Air purifiers should be turned on.",
    "Very Unhealthy": "(201-300) Everyone will be noticably affected. Avoid outdoor exercise and wear a pollution mask outdoors. Ventilation is discouraged. Air purifiers should be turned on.",
    "Hazardous": "(301 and higher) Everyone is at high risk of experiencing strong irritation and negative health effects that could trigger cardiovascular and respiratory illnesses. Avoid exercise and remain indoors. wear a pollution mask outdoors. Air purifiers should be turned on."
}

def home(request):
    if request.method == 'POST':
        zip_code = request.POST.get('zip_code')
        api_url = f'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_code}&API_KEY=43FA6E0C-1842-4566-8555-CDF2722E4FEC'
        response = requests.get(api_url)
        data = response.json()
        aqi_data = []

        if data:
            # Loop through the data to find ozone and PM2.5 AQI readings
            for entry in data:
                if entry['ParameterName'] == 'O3' or entry['ParameterName'] == 'PM2.5':
                    aqi_data.append({
                        'ReportingArea': entry['ReportingArea'],
                        'StateCode': entry['StateCode'],
                        'CategoryName': entry['Category']['Name'],
                        'AQI': entry['AQI'],
                        'Description': category_descriptions.get(entry['Category']['Name'], 'No description available')
        
            
                    })

    else:
        aqi_data = None

    return render(request, 'home.html', {'api': aqi_data})

def about(request):
    return render(request, 'about.html')

def base(request):
    return render(request, 'base.html')
