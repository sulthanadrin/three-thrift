link ke aplikasi saya : http://sultan-adrin-threethrift.pbp.cs.ui.ac.id/


*bagaimana cara saya mengimplementasikan checklist*

    - Membuat sebuah proyek Django baru
      -> Pertama-tama saya membuat direktori bernama threethrift lalu membuat virtual environment di dalamnya. Setelah itu saya menyiapkan dependencies di dalam berkasi requirements.txt di direktori yang sama lalu menginstalnya di terminal. Lalu terakhir saya membuat proyek Django bernama three_thrift m=di terminal.

    - Membuat aplikasi dengan nama main
      -> Pertama-tama saya mengaktifkan virtual environment terlebih dahulu. Setelah itu saya menjalankan python manage.py startapp main untuk membuat aplikasi bernama main.

    - Melakukan routing pada proyek agar dapat menjalankan aplikasi main
      -> Pada file settings.py di dalam folder three_thrift, tambahkan 'main' ke dalam INSTALLED_APPS.

    - Membuat model pada aplikasi main dengan nama Product dan memiliki aitribut name, price, dan description
      -> Pada file models.py pada direktori main, saya membuat class yang bernama Product yang mengambil model.Models dan di dalamnya terdapat atribut name(Charfield), price(Integerfield), description(Textfield). Lalu saya melakukan migration setelah menambah hal-hal tersebut.

    - Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.
      -> Saya melakukan import render terlebih dahulu. Pada fungsi show_main dengan parameter request, saya membuat suatu dictionary yang berisi nama app, nama, dan juga kelas. Setelah itu saya melakukan return render(request, "main.html", context).

    - Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
      -> Saya membuat file urls.py di dalam direktori main, saya melakukan import path dan juga show_main. Lalu saya memberi app_name dengan nilai 'main'. Lalu saya membuat urlpattern yang berisi path('', show_main, name='show_main').

    - Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat
      -> Saya membuat proyek baru melalui akun saya pada https://pbp.cs.ui.ac.id/ yang bernama threethrift. Lalu pada file settings.py yang berada di direktori three_thrift saya menambahkan url deployment pws ke ALLOWED_HOSTS. Setelah itu pada terminal saya menambahkan url pws lalu melakukan git push pws master.

*bagan request client ke web aplikasi berbasis Django*

![gambar bagan](https://drive.google.com/file/d/1y_lcjwvPQrYxBirCz6I5LQjLT8BBP55A/view?usp=sharing)
