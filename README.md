🐐 KambingKu - E-commerce Jual Beli Kambing 🐐
http://malvin-muhammad-kambingku.pbp.cs.ui.ac.id/
Selamat datang di KambingKu, tempat di mana kambing-kambing terbaik di Indonesia berkumpul untuk dijual (dan dibeli, tentu saja). Dari kambing sehat, gemuk, lucu, sampai kambing yang pandai selfie — semua ada di sini!

Ini adalah langkah besar untuk dunia per-kambing-an digital! 🚀

Apa itu KambingKu? 🤔
KambingKu adalah platform e-commerce khusus untuk kambing. Ya, benar sekali! Di sini, kamu bisa menemukan berbagai jenis kambing dari seluruh pelosok nusantara. Baik untuk kurban, ternak, atau sekadar ingin pelihara kambing imut, KambingKu adalah tempat yang tepat!

Apakah kamu sedang mencari kambing yang bisa merumput sendiri? Atau kambing yang hobi jogging? Kami punya semuanya. Di KambingKu, setiap kambing punya cerita, dan kami yakin ada satu kambing yang pas untukmu. 😉


Note Terakhir:
Di KambingKu, setiap kambing adalah spesial. Jadi ingat, kambing juga butuh cinta, perhatian, dan rumput berkualitas!

Happy shopping! 🛒🎉 :

1. Membuat Proyek Django Baru:

- Buat direktori dengan nama kambing-ku.

- Buat virtual environment dengan menjalankan python -m venv env di dalam direktori kambing-ku.

- Aktifkan virtual environment tersebut, kemudian jalankan django-admin startproject kambing-ku untuk memulai proyek Django.

- Pindah ke direktori proyek yang baru dibuat: cd kambing-ku.

2. Membuat Main dan Mengatur Routing:

- Di dalam direktori kambing-ku, buat file baru dengan nama main menggunakan perintah python manage.py startapp main.

- Tambahkan 'main' ke dalam daftar INSTALLED_APPS di berkas settings.py.

- Pada berkas urls.py proyek, tambahkan routing untuk menghubungkan urls.py dari main.

3. Membuat Model Product:

Di dalam berkas main/models.py, buat model Product dengan atribut name, price, dan description seperti berikut:

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()

Jalankan perintah python manage.py makemigrations dan python manage.py migrate untuk memigrasi model ke database.

4. Membuat Fungsi pada views.py:

Di dalam main/views.py, buat fungsi yang mengembalikan template HTML:


5. Membuat Template HTML:

Di dalam direktori main, buat folder templates, dan di dalamnya buat berkas HTML dengan nama main.html.


6. Mengatur Routing di urls.py:

- Di dalam berkas main/urls.py, petakan fungsi dari views.py

- Di berkas urls.py proyek, tambahkan routing untuk menghubungkan main



7. Melakukan Deployment ke PWS:

- Masuk ke halaman PWS dan buat proyek baru dengan nama kambing-ku.

- Tambahkan URL PWS ke daftar ALLOWED_HOSTS di settings.py.

- Jalankan perintah deployment dari PWS, dan gunakan perintah git push pws main:master untuk perubahan selanjutnya.


![alt text](image.png)

Fungsi Git Dalam Pengembangan Perangkat Lunak

Git sangat membantu dalam proyek besar dan kolaborasi antara beberapa pengembang yang bekerja pada proyek yang sama secara bersamaan. Dengan Git, kita bisa menggunakan git branch untuk membuat fitur yang berbeda, kemudian kita gabungkan kembali ke proyek utama. Kita juga bisa menggunakan git clone untuk mengerjakan proyek tanpa koneksi internet. Selain itu, karena kita melakukan git push ke dalam repositori, kita tidak perlu khawatir kehilangan kode karena kita selalu memiliki cadangan di repositori GitHub kita. Terakhir, Git memungkinkan kolaborator untuk meninjau kode melalui git pull requests sebelum kode tersebut digabungkan, memastikan kualitas yang lebih baik.


Framework Django Sebagai Permulaan Pembelajaran Pengembangan Perangkat Lunak

Menurut saya, framework Django dipilih sebagai permulaan pembelajaran pengembangan perangkat lunak karena kemudahan penggunaannya.

Django dibangun di atas Python, salah satu bahasa pemrograman yang paling mudah dipahami, terutama bagi pemula. Python memiliki sintaks yang sederhana, dan Django memanfaatkan keunggulan ini dengan menawarkan kemudahan dalam pengaturan awal. Hal ini memungkinkan pengembang untuk segera fokus pada pengembangan fitur aplikasi tanpa harus melakukan konfigurasi teknis yang rumit. Dengan Django, pemula dapat lebih cepat memahami konsep dasar pengembangan web dan langsung menerapkannya dalam proyek nyata.



Mengapa kita perlu pengiriman data dalam membuat sebuah platform

Alasan utama kita butuh pengiriman data dalam membuat sebuah platform adalah untuk memastikan semua proses berjalan berdasarkan data. Platform perlu berinteraksi dengan berbagai bagian seperti basis data, pengguna, dan elemen lainnya (seperti yang digambarkan di Tugas Individu 2). Agar interaksi ini berhasil, data harus bisa dipindahkan atau dikirim antar bagian sistem. Dengan adanya pengiriman data, kita bisa memastikan:

- Permintaan pengguna seperti mengisi formulir ditangani dengan benar
- Data di berbagai bagian sistem tetap sinkron atau terhubung dengan baik
- Laporan atau data yang diambil dari basis data bisa berjalan dengan lancar

Mana yang lebih baik, XML atau JSON? Mengapa JSON lebih populer?

Menurut saya, JSON lebih baik karena saat kita melihat respons Postman dari URL yang diambil, JSON lebih sederhana dan mudah dibaca dibandingkan XML. Alasan mengapa JSON lebih populer adalah karena kesederhanaannya, yang sangat penting terutama dalam pengembangan web ketika harus menangani banyak data.

Fungsi dari metode is_valid() di form Django

Di Django, metode **is_valid()** digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form sudah sesuai dengan aturan yang ditentukan dan untuk memastikan tidak ada kesalahan. Dengan menggunakan **is_valid()**, kita bisa memastikan bahwa:

- Semua kolom yang harus diisi di form sudah terisi
- Tipe data yang dimasukkan sesuai dengan tipe data yang diharapkan
- Jika data valid, **is_valid()** akan mengembalikan nilai *True*, yang berarti data tersebut bisa diproses lebih lanjut (misalnya, disimpan ke dalam basis data). Jika tidak valid, akan mengembalikan *False*, dan biasanya kesalahan akan ditampilkan kepada pengguna.

Metode ini penting untuk mencegah data yang salah atau tidak sesuai diproses, sehingga menjaga keamanan dan integritas aplikasi.

Mengapa kita perlu csrf_token di form Django

Django menggunakan **csrf_token** (Cross-Site Request Forgery token) untuk melindungi form dari serangan CSRF. Serangan CSRF terjadi ketika ada situs jahat yang menipu pengguna untuk mengirim permintaan ke situs lain di mana mereka sudah login. Jika tidak ada **csrf_token**:

- Penyerang bisa melakukan tindakan yang tidak sah, seperti mengirim form atas nama pengguna tanpa sepengetahuannya
- Data dan keamanan sistem bisa terganggu, bahkan bisa menyebabkan pencurian data atau peretasan
- Tanpa **csrf_token**, semua ini lebih mudah dimanfaatkan oleh penyerang. **Csrf_token** memastikan bahwa permintaan form benar-benar datang dari pengguna yang sudah terverifikasi, dengan membuat token unik yang diverifikasi baik di sisi pengguna maupun server.

Implement Checklist Step by Step

1. Buatlah file bernama forms.py di direktori main dengan isi sebagai berikut:

from django.forms import ModelForm
from main.models import KambingEntry

class KambingEntryForm(ModelForm):
    class Meta:
        model = KambingEntry
        fields = ["name", "price", "description"]

2. Buka file views.py di direktori main.
   Tambahkan import statement berikut di bagian paling atas file:

   from django.shortcuts import render, redirect
   from main.forms import KambingEntryForm
   from main.models import KambingEntry

3. Buat fungsi untuk menambahkan entri ke database di dalam file    views.py di direktori main dengan isi sebagai berikut:
 
def create_kambing_entry(request):
    form = KambingEntryForm(request.POST or None)
    

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_kambing_entry.html", context)

4. Ubah fungsi show_main di dalam file views.py untuk menangani produk sebagai berikut:

def show_main(request):
    kambing_entries = KambingEntry.objects.all()

    context = {
        'Nama_Aplikasi': 'KambingKu',
        'Name': 'Malvin Muhammad Raqin',
        'Class': 'PBP D',
        'kambing_entries': kambing_entries
    }

    return render(request, "main.html", context)

5. Buat direktori bernama templates di dalam direktori main dan buat file HTML dengan nama base.html yang berfungsi sebagai kerangka untuk tampilan. Isi file tersebut dengan:

{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>

6. Tambahkan folder templates dengan mengedit file settings.py di direktori proyek, misalnya KambingKu, seperti berikut:

... 

        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
...

7. Mengimplementasikan basis data ke halaman utama `main.html` sehingga menggunakan `base.html` sebagai template utama dan juga memperluas `base.html` di dalam direktori `main`.

{% extends 'base.html' %}
{% block content %}
<h1>KambingKu</h1>
<h5>Nama Aplikasi: </h5>
<p>{{ Nama_Aplikasi }}<p>
<h5>Name: </h5>
<p>{{ Name }}<p>
<h5>Class: </h5>
<p>{{ Class }}<p>
    {% if not kambing_entries %}
    <p>Belum ada data kambing pada KambingKu.</p>
    {% else %}
    <table>
      <tr>
        <th>Kambing Name</th>
        <th>Time</th>
        <th>Kambing Price</th>
        <th>Description</th>
      </tr>
    
      {% comment %} Berikut cara memperlihatkan data kambing di bawah baris ini 
      {% endcomment %} 
      {% for kambing_entry in kambing_entries %}
      <tr>
        <td>{{kambing_entry.name}}</td>
        <td>{{kambing_entry.time}}</td>
        <td>{{kambing_entry.price}}</td>
        <td>{{kambing_entry.description}}</td>
      </tr>
      {% endfor %}
    </table>
    {% endif %}
    
    <br />
    
    <a href="{% url 'main:create_kambing_entry' %}">
      <button>Add New Kambing Entry</button>
    </a>
{% endblock content %}

Karena kita ingin menampilkan data berdasarkan ID, kita perlu mengubah primary key menjadi UUID untuk membuat aplikasi kita lebih aman. Berikut caranya:

1. Pada file models.py di direktori main, tambahkan baris-baris berikut :

import uuid # add this at the top (import statements)
...
class ...
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ...

2. Tambahkan impor berikut ke file views.py di direktori main pada bagian atas file:

from django.http import HttpResponse
from django.core import serializers

3. Berikut adalah cara untuk membuat fungsi di dalam views.py di direktori main agar dapat menampilkan data dalam format JSON dan XML, baik secara keseluruhan maupun berdasarkan ID dari setiap entri basis data:

def show_xml(request):
    data = KambingEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = KambingEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = KambingEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = KambingEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

Buat routing URL untuk semua fungsi di dalam views.py

Impor semua fungsi yang telah kita buat di views.py ke dalam file urls.py di direktori main pada bagian atas file sebagai berikut:

from main.views import show_main, create_kambing_entry, show_xml  show_json, show_xml_by_id, show_json_by_id

Di dalam file urls.py di direktori main, tambahkan semua URL yang sesuai dari modifikasi yang telah kita buat di views.py sebagai berikut:

...
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-kambing-entry', create_kambing_entry, name='create_kambing_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
...

Untuk menguji aplikasi di localhost, Anda bisa menjalankan perintah berikut di terminal:

python manage.py runserver

lalu buka http://localhost:8000/ di browser anda






Screenshot Postman

1. XML

![alt text](image-1.png)

2. JSON

![alt text](image-2.png)

3. XML by id

![alt text](image-5.png)

4. JSON by id

![alt text](image-4.png)

.

## Tugas Individiual 4

1. **Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`?**

    Kedua fungsi ini digunakan untuk melakukan pengalihan (redirection), tetapi perbedaannya adalah `HttpResponseRedirect` memerlukan URL secara eksplisit atau menggunakan `reverse()` untuk mencari URL, sedangkan `redirect` adalah shortcut yang lebih mudah karena bisa secara otomatis menghubungkan URL dari nama view atau objek model, seperti yang kita lakukan di fungsi `logout_user`.

2. **Bagaimana model `KambingEntry` dihubungkan dengan `User`?**

    Sama seperti implementasi di atas, kita bisa menghubungkan model dengan menggunakan hubungan `ForeignKey`. Hal ini memungkinkan satu pengguna memiliki banyak entri kambing, tetapi setiap entri hanya terkait dengan satu pengguna, yaitu hubungan One-To-Many.

3. **Perbedaan antara *authentication* dan *authorization*, serta apa yang terjadi saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep ini.**

    *Authentication* adalah proses untuk memverifikasi identitas pengguna (misalnya, memeriksa username dan password). Django mengelola ini menggunakan fungsi seperti `authenticate()` dan `login()`:
    ```bash
    from django.contrib.auth import authenticate, login

    def user_login(request):
        user = authenticate(username='john', password='secret')
        if user is not None:
            login(request, user)
    ```

    *Authorization* adalah proses untuk menentukan tindakan apa yang diizinkan dilakukan oleh pengguna yang telah diautentikasi. Django menggunakan decorator seperti `@login_required` dan `@permission_required` untuk mengelola otorisasi:
    ```bash
    from django.contrib.auth.decorators import login_required

    @login_required
    def my_view(request):
        ...
    ```

    Saat pengguna login, Django melakukan hal berikut:

    - **Autentikasi**: Memeriksa kredensial pengguna (dengan `authenticate()`).
    - **Membuat sesi**: Setelah berhasil, Django membuat sesi dan menyimpan ID sesi di cookies.
    - **Mengasosiasikan sesi**: Django melacak status autentikasi pengguna menggunakan sesi ini.

4. **Bagaimana Django mengingat pengguna yang sudah login? Jelaskan penggunaan lain dari *cookies* dan apakah semua cookies aman digunakan.**

    Django menggunakan **session** dan **cookies** untuk mengingat pengguna yang sudah login:

    - **Sessions**: Django menyimpan data sesi di sisi server dan mengaitkannya dengan ID sesi unik yang dikirim ke browser pengguna sebagai cookie.
    - **Cookies**: Cookie adalah file kecil yang disimpan di sisi klien. ID sesi disimpan dalam cookie (biasanya bernama `sessionid`), yang dikirim dengan setiap permintaan berikutnya.

    Penggunaan lain dari cookies:

    - **Menyimpan preferensi**: Cookies bisa digunakan untuk menyimpan preferensi pengguna, seperti pengaturan bahasa.
    - **Melacak aktivitas**: Cookies dapat digunakan untuk melacak perilaku pengguna untuk analitik atau personalisasi.
    - **Mengingat input form**: Cookies dapat menyimpan nilai input form yang pernah dimasukkan sebelumnya.

    Apakah semua cookies aman?
    Tidak semua cookies aman. Beberapa pertimbangan keamanan:

    - **Secure flag**: Cookies dengan flag "Secure" hanya dikirim melalui HTTPS, membuatnya lebih aman.
    - **HttpOnly flag**: Cookies dengan flag "HttpOnly" tidak bisa diakses oleh JavaScript di sisi klien, mencegah serangan XSS.
    - **Session Hijacking**: Jika cookie sesi disadap, penyerang dapat menyamar sebagai pengguna.

5.  **Bagaimana cara mengimplementasikan checklist di atas langkah demi langkah?**

#### Implementasi Fungsi Register, Login, dan Logout

##### **Register**

1. Untuk mengimplementasikan fungsi register, kita bisa menggunakan fungsi bawaan `UserCreationForm` dari Django. Tambahkan import berikut di `views.py` dalam direktori `main` sebagai berikut:
    ```bash
    ...
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages
    ```

2. Kita bisa mengimplementasikan fungsi register dan menambahkannya ke `views.py` sebagai berikut:
    ```bash
    def register(request):
        form = UserCreationForm()
    
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Akun baru Anda berhasil ditambahkan!')
                return redirect('main:login')
        context = {
            'form':form
            }
        return render(request, 'register.html', context)
    ```
    Seperti yang dapat dilihat, akun akan dibuat jika `is_valid()` mengembalikan nilai True. Setelah itu, akan diarahkan kembali ke halaman login.

3. Buat file HTML baru bernama `register.html` di dalam subdirektori `templates` di direktori `main` sebagai berikut:
    ```bash
    {% extends 'base.html' %}

    {% block meta %}
    <title>Register</title>
    {% endblock meta %}

    {% block content %}

    <div class="login">
    <h1>Register</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input type="submit" name="submit" value="Register" /></td>
        </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}
    </div>

    {% endblock content %}
    ```

4. Jangan lupa untuk mengimplementasikannya ke dalam `urlpatters` agar fungsi dapat diakses. Pada `urls.py` di direktori `main`, impor fungsi sebagai berikut:
    ```bash
    from main.views import ..., register
    ```

    Tambahkan path URL:
    ```bash
    urlpatterns = [
        ...
        path('register/', register, name='register')
        ]
    ```

##### **Login**

5. Untuk mengimplementasikan fungsi login, kita bisa menggunakan fungsi bawaan `authenticate`, `login`, dan `AuthenticationForm` dari Django. Tambahkan import berikut di `views.py` dalam direktori `main` sebagai berikut:
    ```bash
    ...
    from django.contrib.auth.forms import ..., AuthenticationForm
    from django.contrib.auth import authenticate, login
    ```

6. Kita bisa mengimplementasikan fungsi login dan menambahkannya ke `views.py` sebagai berikut:
    ```bash
    def login_user(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
    
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
    
        else:
            form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)
    ```

7. Buat file HTML baru bernama `login.html` untuk menampilkan fungsi login di dalam subdirektori `templates` di direktori `main` sebagai berikut:
    ```bash
    {% extends 'base.html' %}

    {% block meta %}
    <title>Login</title>
    {% endblock meta %}

    {% block content %}
    <div class="login">
    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Login" /></td>
        </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %} Belum punya akun?
    <a href="{% url 'main:register' %}">Daftar Sekarang</a>
    </div>

    {% endblock content %}
    ```

8. Tambahkan fungsi ke `urls.py` untuk mengakses login. Pada `urls.py` di direktori `main`, impor fungsi sebagai berikut:
    ```bash
    from main.views import ..., login_user
    ```

    Tambahkan path URL:
    ```bash
    urlpatterns = [
        ...
        path('login/', login_user, name='login')
        ]
    ```

##### **Logout**

9. Untuk mengimplementasikan fungsi logout, kita bisa menggunakan fungsi bawaan `logout` dari Django. Tambahkan import ini di `views.py` di direktori `main`:
    ```bash
    ...
    from django.contrib.auth import ..., logout
    ```

10. Kita bisa mengimplementasikan fungsi logout dan menambahkannya ke `views.py` sebagai berikut:
    ```bash
    def logout_user(request):
        logout(request)
        return redirect('main:login')
    ```

11. Tambahkan tombol logout ke `main.html` untuk mengarahkan pengguna ke logout. Tambahkan kode berikut di subdirektori `templates` di direktori `main`:
    ```bash
    ...
    <a href="{% url 'main:logout' %}">
        <button>Logout</button>
    </a>
    ```

12. Tambahkan path ke `urls.py` untuk logout. Pada `urls.py` di direktori `main`, impor fungsi sebagai berikut:
    
    ```bash
    from main.views import ..., logout_user
    ```

    Tambahkan path URL:
    ```bash
    urlpatterns = [
        ...
        path('logout/', logout_user, name='logout')
        ]
    ```

    Sekarang semua fungsi Register, Login, dan Logout sudah diimplementasikan.

#### Menampilkan Detail Pengguna yang Login (Username) dan Menggunakan Cookies (Last Login)

##### **Implementasi Cookies**

1. Untuk mengimplementasikan `last_login`, kita butuh waktu dan tanggal serta redirect setelah form dikirim. Kita bisa menggunakan fungsi bawaan Django dan Python. Tambahkan import berikut ke `views.py` di direktori `main`:
    ```bash
    ...
    from django.http import ..., HttpResponseRedirect
    from django.urls import reverse
    import datetime
    ```

2. Ubah kode di fungsi `login_user` dari:
    ```bash
    ...
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('main:show_main')
    ...
    ```

    Menjadi:
    ```bash
    ...
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ...
    ```

3. Ubah fungsi `show_main` di `views.py` untuk menangani `last_login`:
    ```bash
    ...
    context = {
        'name': "malvin muhammad raqin",
        'products': products,
        'last_login': request.COOKIES.get('last_login')
    }
    ```

4. Ubah fungsi `logout_user` agar cookies dihapus saat pengguna logout:
    ```bash
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```

5. Tampilkan `last_login` di file `main.html` dengan menambahkan baris berikut:
    ```bash
    ...
    <h5>Last login session: {{ last_login }}</h5>
    ...
    ```

##### **Menampilkan Nama Pengguna yang Sedang Login**

6. Ubah fungsi `show_main` di `views.py` untuk menampilkan nama pengguna yang sedang login:
    ```bash
    ...
    context = {
        'name': request.user.username,
        'products': products,
    ...
    }
    ```

7. Gunakan `login_required` untuk memastikan pengguna harus login sebelum melanjutkan. Tambahkan import berikut ke `views.py`:
    ```bash
    ...
    from django.contrib.auth.decorators import login_required
    ```

    Tambahkan decorator ke fungsi `show_main`:

    ```bash
    ...
    @login_required(login_url='/login')
    def show_main(request):
        ...
    ```

#### Dua Akun dengan Tiga Data Dummy Masing-masing

1. Akun dengan nama `rakabima` memiliki data sebagai berikut:
![alt text](image-7.png)


2. Akun dengan nama `mlvn.raqin` memiliki tiga data
![alt text](image-3.png)

    

#### Menghubungkan Model `Product` dan `User`

Kita perlu membuat hubungan antara model `Product` dan `User` dengan menggunakan `ForeignKey`. Berikut langkah-langkahnya:

1. Pada `models.py` di direktori `main`, impor model `User`:
    ```bash
    ...
    from django.contrib.auth.models import User
    ```

2. Tambahkan `user` ke model `Product`:
    ```bash
    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ...
    ```

3. Edit fungsi form untuk menyimpan data berdasarkan pengguna. Ubah fungsi `create_product` di `views.py`:
    ```bash
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == 'POST':
            products = form.save(commit=False)
            products.user = request.user
            products.save()
            return redirect('main:show_main')

        context = {
            'form': form
        }

        return render(request, "create_product.html", context)
    ```

4. Filter data produk berdasarkan pengguna di fungsi `show_main`:
    ```bash
    def show_main(request):
        products = Product.objects.filter(user=request.user)
        context = {
            'name': request.user.username,
            'products': products,
            ...
    ```

5. Lakukan migrasi model setelah mengubah `models.py`:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Pilih nilai default untuk `user` ketika diminta saat migrasi:
    ```bash
    It is impossible to add a non-nullable field 'user' to product without specifying a default. 
    Please select a fix:
    1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
    2) Quit and manually define a default value in models.py.
    Select an option: 1
    >>> 1
    ```

7. Pastikan proyek siap untuk lingkungan produksi dengan menambahkan import berikut di `settings.py`:
    ```bash
    import os
    ```

    Ubah pengaturan DEBUG di `settings.py`:
    ```bash
    PRODUCTION = os.getenv("PRODUCTION", False)
    DEBUG = not PRODUCTION
    ```