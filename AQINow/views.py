import requests
from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        zip_code = request.POST.get('zip_code')
        api_url = f'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_code}&API_KEY=43FA6E0C-1842-4566-8555-CDF2722E4FEC'
        response = requests.get(api_url)
        data = response.json()
        aqi_data = None

        if data:
            ozone_aqi_data = None
            pm25_aqi_data = None

            # Dictionary to map category names to descriptions
            category_descriptions = {
                "Good": "(0-50) Air quality is satisfactory, and air pollution poses little or no risk.",
                "Moderate": "(51-100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.",
                "Unhealthy for Sensitive Groups": "(101-150) Members of sensitive groups may experience health effects. The general public is less likely to be affected.",
                "Unhealthy": "(151-200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.",
                ".Very Unhealthy": "(201-300) Health alert: The risk of health effects is increased for everyone.",
                ".Hazardous": "(301 and higher) Health warning of emergency conditions: everyone is more likely to be affected."
            }

            # Loop through the data to find ozone and PM2.5 AQI readings
            for entry in data:
                if entry['ParameterName'] == 'O3':
                    ozone_aqi_data = {
                        'AQI': entry['AQI'],
                        'Category': entry['Category']['Name'],
                        'Description': category_descriptions.get(entry['Category']['Name'], 'No description available')
                    }
                elif entry['ParameterName'] == 'PM2.5':
                    pm25_aqi_data = {
                        'AQI': entry['AQI'],
                        'Category': entry['Category']['Name'],
                        'Description': category_descriptions.get(entry['Category']['Name'], 'No description available')
                    }

            # Check if both ozone and PM2.5 AQI readings were found
            if ozone_aqi_data and pm25_aqi_data:
                aqi_data = {
                    'ozone': ozone_aqi_data,
                    'pm25': pm25_aqi_data,
                }
            elif ozone_aqi_data:
                aqi_data = {
                    'ozone': ozone_aqi_data,
                }
            elif pm25_aqi_data:
                aqi_data = {
                    'pm25': pm25_aqi_data,
                }

    else:
        aqi_data = None

    return render(request, 'home.html', {'api': aqi_data})

def about(request):
    return render(request, 'about.html')

def base(request):
    return render(request, 'base.html')
