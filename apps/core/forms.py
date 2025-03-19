from django import forms
from .models import Item, Category

class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'category', 'image']
        widgets = {
            'name':forms.TextInput({'class':'form-control'}),
            'price':forms.NumberInput({'class':'form-control'}),
            'category':forms.Select({'class':'form-control'}),
            'description': forms.Textarea(attrs={'rows': 2, 'class':'form-contro'}),
            'image': forms.FileInput(attrs={'class':'form-control last img'}),
        }
        labels = {
            'name': 'Item Name',
            'description': 'Item Description',
            'price': 'Item Price',
            'category': 'Item Category',
            'image': 'Item Image',
        }
        error_messages = {
            'name': {'required': 'Please enter the name of the item'},
            'description': {'required': 'Please enter the description of the item'},
            'price': {'required': 'Please enter the price of the item'},
            'category': {'required': 'Please select the category of the item'},
            'image': {'required': 'Please upload an image of the item'},
        }
        
        
class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Category Name',
        }
        help_texts = {
            'name': 'Enter the name of the category',
        }
        error_messages = {
            'name': {'required': 'Please enter the name of the category'},
        }
