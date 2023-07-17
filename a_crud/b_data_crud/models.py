from django.db import models
import joblib
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier

# Create your models here.

# create a class data_1 model with id , name , descriptions
class data_1(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class data_2(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class data_mahasiwa(models.Model):

    jk = (
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan'),
    )
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length = 150, choices=jk)
    nim = models.CharField(max_length=100)
    fakultas = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    nilai_sikap = models.IntegerField()
    nilai_uts   = models.IntegerField()
    nilai_uas   = models.IntegerField()

    # sum nilai_sikap, nilai_uts
    def nilai_akhir(self):
        return self.nilai_sikap + self.nilai_uts + self.nilai_uas
    # nilai akhir / jumlah mata kuliah
    def nilai_akhir_per_mata_kuliah(self):
        return self.nilai_akhir() / 3
    def __str__(self):
        return self.nama

# Create your models here.
GENDER = (
    (0, 'Terlentang'),
    (1, 'Berdiri'),
)
 
class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)], null=True)
    height = models.PositiveIntegerField(null=True)
    sex = models.PositiveIntegerField(choices=GENDER, null=True)
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/ml_sport_model.joblib')
        self.predictions = ml_model.predict(
            [[self.age, self.height, self.sex]])
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name


