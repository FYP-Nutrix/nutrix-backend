from pyexpat import model
from django import forms

from food_label.models import FoodLabel, FoodType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

# class FoodTypeForm(forms.ModelForm):
#     class Meta:
#         model = FoodType
#         fields = ('food_type',)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.layout = Layout(
#             'food_type'
#         )
#         self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary float-right'))

class FoodTypeForm(forms.ModelForm):
    class Meta:
        model = FoodLabel
        fields = ('food_image_path',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'food_image_path'
        )
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary float-right'))

class FoodLabelForm(forms.ModelForm):
    food = [(a.food_id, a.food_type) for a in FoodType.objects.all()]# loop food type from queryset
    food_type = forms.ChoiceField(choices=food, widget=forms.Select())
    class Meta:
        model = FoodType
        fields = ('food_type',)