from django import template

register = template.Library()

CATEGORY_DESCRIPTIONS = {
    1: "(0-50) Air quality is satisfactory and poses little to no risk! Enjoy your day",
    2: "(51-100) Due to the risk of respiratory illness symptoms, sensitive groups should greatly reduce outdoor exercise. Avoid ventilating indoor spaces with outdoor air. Air purifiers should be turned on.",
    3: "(101-150) Everyone is at risk for eye, skin, and throat irritation as well as respiratory problems. greatly reduce or avoid outdoor exercise. Avoid ventilating indoor spaces with outdoor air",
    4: "(151-200) Increased likelihood of heart and lung aggravation as well as health impacts for everyone. Avoid and wear a pollution mask outdoors. Ventilation is discouraged. Air purifiers should be turned on.",
    5: "(201-300) Everyone will be noticably affected. Avoid outdoor exercise and wear a pollution mask outdoors. Ventilation is discouraged. Air purifiers should be turned on.",
    6: "(301 and higher) Everyone is at high risk of experiencing strong irritation and negative health effects that could trigger cardiovascular and respiratory illnesses. Avoid exercise and remain indoors. wear a pollution mask outdoors. Air purifiers should be turned on.",
}


@register.filter(name='get_aqi_description')
def get_aqi_description(category_number):
    return CATEGORY_DESCRIPTIONS.get(category_number, "No data available.")
