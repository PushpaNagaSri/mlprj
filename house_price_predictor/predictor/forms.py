# house_price_predictor/forms.py
from django import forms

class HousePriceForm(forms.Form):
    bedrooms = forms.IntegerField(label="Number of Bedrooms", min_value=1)
    bathrooms = forms.IntegerField(label="Number of Bathrooms", min_value=1)
    sqft = forms.IntegerField(label="Square Footage", min_value=1)
