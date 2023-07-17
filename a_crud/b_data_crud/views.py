from django.shortcuts import render, redirect

# import messages
from django.contrib import messages

# Create your views here.

# Membuat Fungsi Menampilkan Menu Data
def menu_data(request):
    context = {
        'data' : 'Menu Data'
    }
    return render(request, 'b_data_crud/menu_data.html', context)

# Mengambil Table Data_1 dari models
from .models import data_1
def table_data_1(request):
    data_tampil_1 = data_1.objects.all()
    context = {
        'data_1' : data_tampil_1
        }
    return render(request, 'b_data_crud/data_1.html', context)

from .models import data_2
def table_data_2(request):
    data_tampil_2 = data_2.objects.all()
    context = {
        'data_2' : data_tampil_2
        }
    return render(request, 'b_data_crud/data_2.html', context)

def delete_data_2(request, id):
    delete_data_2= data_2.objects.get(id=id).delete()
    messages.success(request, 'Data 2 berhasil dihapus')
    return redirect('data-2-page')


# Membuat Fungsi Delete berdasarkan id
def delete_data(request, id):
    delete_data = data_1.objects.get(id=id).delete()
    # create a messages
    messages.success(request, 'Data berhasil dihapus')
    return redirect('data-1-page')



# Membuat tambah Data dari forms
from .forms import Data_1Form
def add_data(request):
    form = Data_1Form()
    if request.method == 'POST':
        form = Data_1Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('data-1-page')
    else :
        form = Data_1Form()
    context = {
        'form' : form
        }
    return render(request, 'b_data_crud/tambah_data_1.html', context)

from .forms import Data_2Form
def add_data_2(request):
    form = Data_2Form()
    if request.method == 'POST':
        form = Data_2Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('data-2-page')
    else :
        form = Data_2Form()
    context = {
        'form' : form
        }
    return render(request, 'b_data_crud/tambah_data_2.html', context)



# Membuat Edit data
from .forms import Data_1Form
def edit_data(request, id): 
    data_1_edit = data_1.objects.get(id=id)
    form = Data_1Form(instance=data_1_edit)
    if request.method == 'POST':
        form = Data_1Form(request.POST, instance=data_1_edit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diedit')
            return redirect('data-1-page')
    context = {
        'form' : form,
        'data_1_edit' : data_1_edit
        }
    return render(request, 'b_data_crud/edit_data_1.html', context)

# Membuat Edit data
from .forms import Data_2Form
def edit_data_2(request, id): 
    data_2_edit = data_2.objects.get(id=id)
    form = Data_2Form(instance=data_2_edit)
    if request.method == 'POST':
        form = Data_2Form(request.POST, instance=data_2_edit)
        if form.is_valid():
            data_2 = form.save(commit=False)
            data_2.save()
            messages.success(request, 'Data berhasil diedit')
            return redirect('data-2-page')
    context = {
        'form' : form,
        'data_2_edit' : data_2_edit
        }
    return render(request, 'b_data_crud/edit_data_2.html', context)


# Membuat fungsi data 
from . models import data_mahasiwa
def data_print(request):
    data_print = data_mahasiwa.objects.all()

    for dataku in data_print:
        dataku.rata_rata = dataku.nilai_akhir_per_mata_kuliah()
    context = {
        'dataku' : data_print,
    }
    return render(request, 'b_data_crud/data_print.html', context)


from .forms import DataForm
from .models import Data
from django.shortcuts import render, redirect
import joblib
import pickle
import json

def data_create(request):
    if request.method == 'POST':
        # Proses pengisian form dan prediksi
        # ...

        # Load model dari joblib
        ml_model = joblib.load('ml_model/ml_sport_model.joblib')

        # Konversi model menjadi format JSON
        json_model = json.dumps(ml_model, cls=JoblibEncoder)

        # Simpan data ke database
        form.save()

        return redirect('data_list')  # Ganti 'data_list' dengan URL yang sesuai
    else:
        form = DataForm()
    
    return render(request, 'b_data_crud/data_create.html', {'form': form})

class JoblibEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return {'__class__': 'bytes', '__value__': list(obj)}
        return super().default(obj)


def data_list(request):
    data = Data.objects.all().order_by('-date')
    return render(request, 'b_data_crud/data_list.html', {'data': data})