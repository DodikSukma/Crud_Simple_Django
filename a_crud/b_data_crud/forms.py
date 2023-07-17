# =========================== MEMBUAT FORM UNTUK LOGIN ==================

# Module dalam melakukan memanggilan form

from django import forms

from .models import data_1, data_2, Data       # Memanggil models yang sudah dibuat

# Membuat class untuk menentukan form mahasisa

class Data_1Form(forms.ModelForm):
    class Meta :
        model = data_1
        fields = ('name','description')


class Data_2Form(forms.ModelForm):
    class Meta :
        model = data_2
        fields = ('name','description','email')

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name', 'age', 'height', 'sex']