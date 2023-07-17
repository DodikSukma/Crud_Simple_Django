

# =========================== MEMBUAT URLS AGAR MUDAH DALAM PEMANGGILAN ==================


from django.urls import path
from . import views                     # Harus di isi 

urlpatterns = [
    path('',views.menu_data, name="menu-data-page"),                 # penulisane name juga harus benar harus inputkan nama htmlnya
    path('data', views.table_data_1, name="data-1-page"),  # penulisane name juga harus benar harus inputkan nama htmlnya
    
    path('data_2', views.table_data_2, name="data-2-page"),  # penulisane name juga harus benar harus inputkan nama htmlnya
    
    
    # get a fungsi add data
    path('tambah', views.add_data, name="add-data-page"),
    path('tambah_2', views.add_data_2, name="add-data-2-page"),
    
    path('delete/<int:id>', views.delete_data, name="delete-data"),  # penulisane name juga harus benar harus inputkan nama htmlnya
    
    path('delete_2/<int:id>', views.delete_data_2, name="delete-data-2"),  # penulisane name juga harus benar harus inputkan nama htmlnya
    
    # get a fungsi edit data
    path('edit/<int:id>', views.edit_data, name="edit-data-page"),
    path('edit_2/<int:id>', views.edit_data_2, name="edit-data-page"),
    #path('edit/<int:id>',views.edit, name="mahasiswa_edit"),   

    # Memanggil fungsi data print
    path('print', views.data_print, name="print-data-page"),

     path('data/create/', views.data_create, name='data_create'),
    path('data/list/', views.data_list, name='data_list'),
]