from asyncio.windows_events import NULL
from errno import EFAULT
from msilib.schema import ListView
from tkinter.ttk import LabeledScale
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from food_label.forms import FoodLabelForm, FoodTypeForm
from food_label.models import FoodLabel, FoodType
from django.contrib import messages

# Create your views here.
class CreateFoodTypeView(View, LoginRequiredMixin):
    def post(self, request, *args, **kwargs):
        form = FoodTypeForm(request.POST, request.FILES) #request.FILES
        if form.is_valid():
            form.save()
            messages.success(request, "New Food Type added")
            return redirect("viewLabelFood")
        else:
            messages.warning(request, "Test")
            context = {
                "form": form,
            }
            return render(request, "new_food_type.html", context)
    
    def get(self, request, *args, **kwargs):
        form = FoodTypeForm()
        context = {
            "form": form,
        }
        return render(request, "new_food_type.html", context)

class ViewFoodLabel(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        unlabelled_food = FoodLabel.objects.all().filter(food__isnull=True) # show food image that not label
        form = FoodLabelForm()
        context = {
            "unlabelled_list": unlabelled_food,
            "form": form
        }
        return render(request, "food_label_list.html", context)

    def post(self, request, *args, **kwargs):
        form = FoodLabelForm(request.POST)   
        unlabelled_food = FoodLabel.objects.all().filter(food__isnull=True) # show food image that not label
        label_id = request.POST.get('id_foodlabel')
        if form.is_valid():
            label = form.save(commit=False)
            type_model = FoodType.objects.get(food_id=label.food_type)
            label_model = FoodLabel.objects.get(food_label_id=label_id)
            label_model.food_id = type_model
            label_model.save()
            messages.success(request, "Food has been labelled")
            context = {
                "unlabelled_list": unlabelled_food,
                "form": form
            }
            return render(request, "food_label_list.html", context)
        else:
            context = {
                "form": form
            }
            return render(request, "food_label_list.html", context)
