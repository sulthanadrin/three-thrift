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


![image](https://drive.google.com/uc?export=view&id=1y_lcjwvPQrYxBirCz6I5LQjLT8BBP55A)

*fungsi git dalam pengembangan perangkat lunak*

  1. Melakukan version control, dengan riwayat commit yang telah dilakukan kita dapat melihat tiap perubahan yang terjadi, kapan perubahan terjadi, apa yang berubah, dan siapa yang melakukan perubahan.

  2. Penyimpanan yang terdistribusi, dengan tiap pengembang memiliki salinan penuh terhadap repository yang ada di git sangat mempermudah pekerjaan pengembang dengan bekerja secara offline dan dimana saja.

  3. Kerja kolaboratif, dengan git pengembang dapat bekerja sama dengan pengembang lain untuk membangun program bersama-sama yang hasilnya dapat disatukan di repository yang sama.

*mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?*

  Django adalah framework yang cocok untuk membangun situs web Python, terutama jika membutuhkan kecepatan dan fleksibilitas. Beberapa alasan mengapa memilih Django antara lain

Fitur Lengkap (Batteries-included)
  -> Django sudah menyediakan semua komponen yang dibutuhkan seperti ORM, autentikasi, templating, dan routing, sehingga memudahkan pengembangan web cepat dan efisien.

Keamanan Terjamin
  -> Django secara otomatis melindungi dari ancaman keamanan umum seperti SQL injection dan cross-site scripting, serta sering diperbarui untuk menjaga keamanan.

Skalabilitas
  -> Django mendukung pengembangan web yang dapat berkembang sesuai kebutuhan, dengan lingkungan pengembangan yang fleksibel dan mudah disesuaikan.

  Selain itu, Django memiliki komunitas besar dan dokumentasi lengkap untuk memudahkan pengembang.


*Mengapa model pada Django disebut ORM*
  -> Model  Django disebut ORM (Object-Relational Mapping) karena memetakan objek Python ke tabel database.
 Dengan menggunakan ORM, developer dapat melakukan manipulasi data database sebagai objek Python tanpa harus menggunakan SQL sebagai bahasa yang digunakan untuk mengakses database.


