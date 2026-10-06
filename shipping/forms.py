from django import forms

from .models import Product


class OrderRecommendationForm(forms.Form):
    customer_name = forms.CharField(max_length=120, label='Customer name')
    product_1 = forms.ModelChoiceField(queryset=Product.objects.none(), required=False, label='Product 1')
    quantity_1 = forms.IntegerField(min_value=1, required=False, label='Quantity 1')
    product_2 = forms.ModelChoiceField(queryset=Product.objects.none(), required=False, label='Product 2')
    quantity_2 = forms.IntegerField(min_value=1, required=False, label='Quantity 2')
    product_3 = forms.ModelChoiceField(queryset=Product.objects.none(), required=False, label='Product 3')
    quantity_3 = forms.IntegerField(min_value=1, required=False, label='Quantity 3')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        products = Product.objects.all()
        for field_name in ['product_1', 'product_2', 'product_3']:
            self.fields[field_name].queryset = products

    def clean(self):
        cleaned_data = super().clean()
        selected = []
        for index in [1, 2, 3]:
            product = cleaned_data.get(f'product_{index}')
            quantity = cleaned_data.get(f'quantity_{index}')
            if product and quantity:
                selected.append((product, quantity))

        if not selected:
            raise forms.ValidationError('Please select at least one product and a quantity.')

        return cleaned_data

    def selected_products(self):
        products = {}
        for index in [1, 2, 3]:
            product = self.cleaned_data.get(f'product_{index}')
            quantity = self.cleaned_data.get(f'quantity_{index}')
            if product and quantity:
                if product.pk in products:
                    products[product.pk][1] += quantity
                else:
                    products[product.pk] = [product, quantity]
        return list(products.values())
