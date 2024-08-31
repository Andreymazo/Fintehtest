from django.forms.widgets import Select
from django.forms import ModelForm

from fintehtest.models import Item

# class GetCategorySerializer(serializers.Serializer):
#     queryset = Category.objects.all()
#     choices = [(f"{i}", i) for i in queryset]
#     choose_category = serializers.ChoiceField(choices=choices)

# class StripIdForm(ModelForm):

#     class Meta:
#         CHOICES = Item.objects.all()
#         model=Item
#         # fields = "__all__"
#         fields = ('name',)
#         widgets = {
#             'name': Select(choices=( (x.id, x.name) for x in CHOICES )),
#         }
