from django import template

register = template.Library()

CATEGORY_DESCRIPTIONS = {
    1: "(0-50) Air quality is satisfactory, and air pollution poses little or no risk.",
    2: "(51-100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.",
    3: "(101-150) Members of sensitive groups may experience health effects. The general public is less likely to be affected.",
    4: "(151-200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.",
    5: "(201-300) Health alert: The risk of health effects is increased for everyone.",
    6: "(301 and higher) Health warning of emergency conditions: everyone is more likely to be affected.",
}


@register.filter(name='get_aqi_description')
def get_aqi_description(category_number):
    return CATEGORY_DESCRIPTIONS.get(category_number, "No data available.")
