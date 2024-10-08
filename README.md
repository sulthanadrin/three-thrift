link ke aplikasi saya : http://sultan-adrin-threethrift.pbp.cs.ui.ac.id/

<details>
<summary>--TUGAS 2--</summary>

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
</details>

<details>
<summary>--TUGAS 3--</summary>

  *Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?*
  -> Data delivery memberikan kemudahan dalam aksesibilitas data. Data delivery juga data delivery memberikan real-time processing yang dapat disajikan secara real time. Selain itu proses data delivery yang memiliki struktur yang baik dapat melindungi data.

  *Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?*
  -> Menurut saya, XML lebih baik ketimbang JSON karena XML karena bisa menspesifikasi data-data dengan tag dan struktur meskipun lebih kompleks dan juga fitur commenting yang mendukung presentasi data hierarkis dan juga kompleks
  -> JSON lebih populer dikarenakan JSON lebih mudah digunakan dan dibaca ketimbang XML dan juga JSON berbasis bahasa javascript.

  *Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?*
  -> Method is_valid() melakukan validasi data apakah data pada form memenuhi semua kriteria validasi yang sudah ditentukan dan juga menangani error ketika data tidak valid.

  *Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?*
  -> Kita membutuhkan csrf_token untuk perlindungan terhadap unwanted request pada aplikasi web yang berarti request hanya bisa dilakukan oleh sumber yang sah, valid, dan aman. Jika kita tidak menambahkan csrf_token aplikasi menjadi rentan terhadap serangan CSRF yang memungkinkan penyerang mengirimkan request-request berbahaya ke aplikasi web seperti pengaksesan data pengguna. Hal tersebut dapat dimanfaatkan oleh penyerang dengan mengirimkan request permintaan data pribadi seperti rekening,identitas,dll. Karena tidak ada csrf_token, web app tidak dapat membedakan permintaan yang sah dan yang tidak sehingga web app akan mengirimkan data tersebut ke penyerang.

  *Implementasi Checklist*

  - Membuat input form
  -> Saya membuat file baru yaitu forms.py pada direktori main yang berisi entry untuk product yang berisi field dari model untuk form. Lalu saya mengimport ProductForm dari forms.py ke views.py agar dapat ditampilkan pada laman web. Setelah itu saya membuat function baru yaitu create_new_product(request) yang berfungsi untuk menyimpan data dari form tersebut. Lalu saya melakukan penambahan sedikit pada show_main di views.py agar objek product yang telah dibuat dan disimpan pada ProductForm dapat diakses. Setelah itu saya menambahkan path url ke url pattern dalam file urls.py pada main. Terakhir, saya membuat file baru di direktori templates di dalam main untuk menampilkan field forms yang telah dibuat sebelumnya.

  - Penambahan 4 Fungsi views
  -> Pertama-tama saya mengimport HttpResponse dan juga Serializers pada views.py lalu saya membuat 4 fungsi yaitu show_xml, show_json,show_xml_by_id,show_json_by_id yang masing-masing di dalamnya terdapat satu variabel untuk mengakses seluruh object yang telah di-entry.
  Lalu setelah itu function akan mengembalikan response kepada user menjadi format XML ataupun JSON

  - Routing URL masing-masing views
  -> pada file urls.py pada direktori main saya menambahkan path url untuk masing-masing function ke dalam url pattern sesuai url yang berlaku.

  *Foto Postman JSON*

  ![image](https://drive.google.com/uc?export=view&id=14KJB0o0a9tvR-_TGTvbcg1Fk6d-DIphF)

  *Foto Postman XML*

  ![image](https://drive.google.com/uc?export=view&id=1EkyjboOkSwAl2owGCsFuz9YeRaVooy4D)

  *Foto Postman JSON with ID*

  ![image](https://drive.google.com/uc?export=view&id=1b2Bh-eq2wJj93mcHBdxzH2qQHdbywF7b)

  *Foto Postman XML with ID*

  ![image](https://drive.google.com/uc?export=view&id=1aKVcYQYZxAXwqdOBaOw45LT4U0osAPbz)
</details>



<details>
<summary>--TUGAS 4--</summary>
  

  *Perbedaan antara HttpResponseRedirect dan redirect
  -> HttpResponseRedirect hanya bisa menerima url sebagai argumen pertamanya yang digunakan untuk mengarahkan user ke url tertentu sedangkan redirect bisa menerima model, view, ataupun url yang berarti redirect bisa mengarahkan pengguna tanpa perlu mengonversi sebagai url

  *Cara penghubungan model Product dengan User*
  -> Pertama-tama kita harus mengimpor model User terlebih dahulu di models.py. Lalu berikutnya pada class Product kita mendefinisikan user = models.ForeignKey(User, on_delete=models.CASCADE) untuk mengindikasikan bahwa produk dimiliki oleh pengguna. Setelah itu kita mendefinisikan  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) untuk memberikan identifikasi yang unik untuk setiap produknya agar bisa dikenali kepemilikan product tersebut. Lalu setelah itu lakukan migration setelah melakukan perubahan tersebut pada models.py

  Penghubungan model Product dengan model User di Django dilakukan dengan mendefinisikan field user dalam class Product sebagai models.ForeignKey(User, on_delete=models.CASCADE). Ini menciptakan relasi satu-ke-banyak, di mana satu user dapat memiliki banyak produk. Dengan menggunakan on_delete=models.CASCADE, jika user dihapus, semua produk yang dimilikinya juga akan dihapus. Selain itu, setiap produk diberikan ID unik menggunakan models.UUIDField yang memungkinkan pengidentifikasian produk secara individual di dalam database.

  Setelah mendefinisikan model, langkah selanjutnya adalah melakukan migrasi untuk menerapkan perubahan ke database. Proses ini dilakukan dengan menjalankan perintah makemigrations dan migrate. Dengan cara ini, ketika user membuat produk baru, field user akan diisi dengan ID user yang aktif. Hal ini memudahkan dalam mengelola dan menampilkan informasi produk beserta pemiliknya, sehingga memberikan struktur data yang terorganisir dalam aplikasi Django.

  *Perbedaan authentication dan authorization apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.*
  -> Authentication adalah suatu proses yang berfungsi untuk memverifikasi identitas pengguna sedangkan authorization adalah proses untuk menentukan hak akses apa saja yang dimiliki oleh pengguna setelah melakukan authentication. Saat proses login, pengguna memasukkan kredensial yang umumnya berupa username dan juga password. Setelah itu sistem melakukan authentication untuk memverifikasi kredensial yang telah diinput tersebut. Jika berhasil, pengguna dapat mengakses aplikasi tetapi authorization akan dilakukan terlebih dahulu untuk menentukan hak akses pengguna. Django menyediakan sistem bawaan untuk authentication dan juga authorization yaitu authenticate, login dan juga logout. Lalu berikutnya kita bisa menambahkan decorator seperti @login_required dan juga @permission_required pada function function pada views.py (umumnya pada show_main)

  *Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?*
  -> Saat user login, Django membuat session baru yang menyimpan informasi user seperti ID dari user dan session tersebut akan disimpan di server dan diidentikasi oleh sebuah session ID. Setelah itu Django mengirimkan session cookie ke browser dari user. Setiap kali user mengunjungi laman web, cookie tersebut akan dikirimkan kembali ke server yang memungkinkan Django untuk mengidentifikasi kembali User. Beberapa kegunaan lain dari cookies diantaranya untuk menyimpan preferensi user pada laman web seperti bahasa dan juga tema. Selain itu cookies juga bisa melacak aktivitas user di situs web dan juga menyimpan token autentikasi agar user tetap login meskipun browser telah ditutup. Lalu apakah semua cookies aman digunakan? jawabannya belum tentu. Cookies dapat rentan terhadap serangan seperti Cross-Site Scripting (XSS) dan Cross-Site Request Forgery (CSRF) jika tidak dikelola dengan baik. Cookie juga dapat melakukan tracking yang mengganggu privasi pengguna oleh karena itu terkadang saat mengunjungi laman web kita diberikan pilihan apakah ingin accept cookies, reject, ataupun manage secara manual.


*Implementasi Checklist*

- Implementasi fungsi registrasi,login dan logout
-> Pertama-tama saya mengaktifkan virtual environment terlebih dahulu, lalu setelah itu pada views.py saya mengimport UserCreationForm dan juga messages yang telah disediakan oleh Django untuk membuat formulir register. Lalu setelah itu saya menambahkan function register dengan parameter request pada views.py dengan UserCreationForm sebagai formnya lalu menambahkan conditional untuk validasi input dari user terhadap form register pada function tersebut dan juga membuat file baru yang bernama register.html pada direktori main/templates untuk template dari form register. Lalu terakhir saya mengimport function register di urls.py dan menambahkan path urlnya ke urlpatterns. Lalu untuk membuat function Login saya mengimport authenticate, AuthenticationForm dan login pada views.py yang telah disediakan oleh Django. Setelah itu saya menambahkan function login_user dengan parameter request. Lalu membuat template baru bernama login.html pada direktori main/templates dan melakukan import function pada urls.py dan menambahkan path urlnya ke dalam urlpatterns. Lalu yang terakhir saya kembali mengimport function logout bawaan Django pada views.py dan menambahkan function logout_user dengan parameter request yang berisi memanggil function logout untuk menghapus session dari pengguna dan mengarahkannya kembali ke laman login. Lalu pada template main.html saya menambahkan button untuk melakukan logout dan kembali melakukan import pada urls.py dan menambahkan path urlnya ke urlpatterns.

- Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
-> Saya melakukan register akun sebanyak dua kali dan melakukan login satu persatu ke dalam tiap akun. Setelah itu saya melakukan input new product sebanyak tiga kali untuk setiap user dengan atribut product yang berbeda-beda.

-Menghubungkan model Product dengan User
-> Pertama-tama saya mengimpor model User terlebih dahulu di models.py. Lalu berikutnya pada class Product saya mendefinisikan user = models.ForeignKey(User, on_delete=models.CASCADE) untuk mengindikasikan bahwa produk dimiliki oleh pengguna. Setelah itu kita mendefinisikan  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) untuk memberikan identifikasi yang unik untuk setiap produknya agar bisa dikenali kepemilikan product tersebut. Lalu setelah itu lakukan migration setelah melakukan perubahan tersebut pada models.py


- Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
-> Pada views.py saya mengimport beberapa function yaitu HttpResponseRedirect untuk directing user ke halaman-halaman pada web, lalu reverse untuk membalikkan proses pencarian URL berdasarkan nama view yang telah didefinisikan dalam urls.py dan juga datetime untuk waktu dan tanggal. Lalu pada function login_user pada views.py saya menambahkan fungsionalitas cookie bernama last_login untuk melihat kapan terakhir kali pengguna melakukan login.
Lalu pada function show_main saya menambahkan 'last_login': request.COOKIES['last_login'] ke dalam context untuk menambahkan informasi cookie last_login pada response yang akan ditampilkan pada halaman web. Lalu pada function logout_user saya menambahkan 
response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

kode diatas berfungsi untuk menghapus cookie last_login saat user melakukan logout. Lalu pada template main.html saya menambahkan header baru pada bagian bawah untuk menampilkan data last login.
</details>

<details>
<summary>--TUGAS 5--</summary>

* Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut*
-> Berdasarkan prioritas:
1. Inline Styles
  -> Gaya yang diterapkan secara langsung pada elemen HTML menggunakan atribut style. Contoh: `<div style="color: red;">`

2. ID Selectors
  -> Selektor ini menggunakan tanda pagar '#' untuk menargetkan elemen berdasarkan ID-nya. Contoh: `#myID { color: blue;}`

3. Class Selectors
  -> Selektor ini menggunakan titik '.' untuk menargetkan elemen berdasarkan class-nya. Contoh: `.myclass { color: green;}`

4. Element Selectors
  -> Selektor ini menargetkan elemen HTML tertentu, seperti div, p atau h1. Contoh: `p { color: black;}`

*Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!*
-> Tujuan utama dari responsive design adalah untuk menghindari resizing, scrolling, zooming ataupun panning yang tidak diperlukan pada situs yang belum dioptimalkan untuk cross-platform.

Responsive design memungkinkan konten web mengalir dengan bebas di semua resolusi dan ukuran layar, serta tampil menarik di semua perangkat. Selain itu responsive design menghilangkan keharusan untuk maintaining versi yang berbeda untuk tiap situs web untuk tiap platformnya.

Contoh aplikasi yang sudah menerapkan responsive design:
1. VS Code
2. Spotify
3. Instagram

*Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!*
-> 
Margin: batasan untuk mengatur area di luar elemen. Misal kita memiliki dua buah pasangan border dan padding. Margin mengatur jarak antara kedua pasangan tersebut agar tidak terlalu dekat atau tidak terlalu jauh.

Border: batasan yang mengelilingi area konten dan padding yang berada di antara padding dan margin yang bisa diatur ketebalan gaya dan juga warnanya

Padding: ruang yang berada di sekitar konten dan bersifat transparan dan juga berupa ruang antara konten dan border.

*Jelaskan konsep flex box dan grid layout beserta kegunaannya!*
-> Flex box adalah wadah yang berisi elemen-elemen berupa flex items yang dapat diatur secara fleksibel dan efisien. Konsep utama dari Flex box adalah Flex Container sebagai wadahnya yang di dalamnya terdapat Flex Items yaitu elemen-elemen yang bisa diatur dalam baris atau kolom (1 dimensi).
Kegunaan: - Memberikan fleksibilitas dan responsivitas dalam mengatur elemen pada Flex Container.
          - Menyediakan kontrol yang unggul terhadap ruang antar elemennya.
          - Dapat mengatur elemen secara otomatis tanpa perlu mengatur posisi secara manual.

Grid Layout adalah suatu modul yang membagi halaman dari web menjadi beberapa area utama untuk elemen-elemen ditempatkan di area-area tersebut dalam baris dan kolom (2 dimensi)
Kegunaan: - Memberikan kedisiplinan dalam penyusunan elemen
          - Memberikan web yang responsif karena penyesuaian untuk berbahai ukuran layar
          - Konten pada web dapat dibagi menjadi beberapa bagian.

*Implementasi Checklist*

- Implementasi fungsi untuk menghapus dan mengedit product
  -> 
    *Fungsi hapus*
    pada views.py, saya membuat function baru bernama delete_product yang menerima parameter request dan id
    yang akan mengambil product berdasarkan id dan menghapusnya. Lalu setelah itu pada urls.py saya mengimport fungsi tersebut dan menambahkannya ke urlpatterns

    *Fungsi edit*
    pada views.py, saya membuat function baru bernama edit_product yang menerima parameter request dan id
    yang akan mengambil product berdasarkan id dan mengeditnya menggunakan form product entry. Setelah itu isi dari form di validasi dan perubahan akan di save jika memenuhi.Lalu setelah itu pada urls.py saya mengimport fungsi tersebut dan menambahkannya ke urlpatterns


- Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma)

  saya menggunakan tailwind untuk kustomisasi website

  *Kustomisasi halaman login,register, dan tambah product*

    |Halaman Login|
    -> pada berkas login.html di templates pada directory main, Halaman ini dimulai dengan mewarisi dari base.html dan mengatur judul halaman menjadi "Login". Struktur utama menggunakan div yang diatur dengan flexbox untuk memusatkan form secara vertikal dan horizontal, dengan latar belakang biru tua (bg-sky-900). Form ini menggunakan metode POST untuk mengirim data, dan mencakup dua input field untuk username dan password, masing-masing dengan label yang disembunyikan untuk aksesibilitas. Tombol "Sign in" dirancang untuk mengirimkan form, dengan efek hover yang jelas.

    Pesan umpan balik ditampilkan di bawah form menggunakan logika conditional, yang memeriksa apakah ada pesan yang harus ditampilkan. Pesan sukses dan kesalahan memiliki styling yang berbeda untuk memudahkan pengguna mengenali status login mereka. Selain itu, terdapat tautan untuk pendaftaran bagi pengguna baru, memudahkan mereka untuk membuat akun.

    |Halaman Register|
    -> Di dalamnya, terdapat div yang mengatur tampilan halaman dengan kelas min-h-screen flex items-center justify-center bg-gray-100, yang memastikan bahwa konten halaman terpusat baik secara horizontal maupun vertikal dengan latar belakang abu-abu muda. Judul halaman "Create your account" ditampilkan dengan ukuran font besar dan tebal menggunakan kelas text-3xl font-extrabold text-black, memberikan visibilitas yang baik kepada pengguna. Formulir pendaftaran diatur dengan margin dan padding yang responsif, serta menggunakan kelas space-y-6 untuk memberikan jarak antara elemen-elemen di dalam formulir.

    Formulir tersebut mencakup loop untuk merender setiap field dari form yang telah didefinisikan, di mana setiap field dilengkapi dengan label dan validasi kesalahan. Kelas Tailwind CSS seperti rounded-md dan shadow-sm diterapkan untuk memberikan tampilan yang bersih dan modern. Jika ada kesalahan pada input, ikon kesalahan ditampilkan dengan menggunakan SVG dan pesan kesalahan ditampilkan di bawah field terkait dengan warna merah (text-red-600). Tombol "Register" dirancang dengan styling yang responsif dan interaktif, dengan efek hover yang meningkatkan warna latar belakang. Selain itu, ada tautan untuk navigasi ke halaman login, yang menggunakan kelas text-indigo-400 dan efek hover untuk memberikan umpan balik visual saat pengguna mengarahkan kursor ke tautan tersebut.

    |Halaman Tambah Product|
    -> Struktur utama halaman diatur dengan div yang memiliki kelas flex flex-col min-h-screen bg-gray-100, yang memastikan tampilan responsif dengan tinggi minimum yang sesuai layar dan latar belakang abu-abu muda. Di dalam kontainer, judul "Add New Product" ditampilkan di tengah dengan kelas text-3xl font-bold text-center mb-8 text-black, memberikan penekanan visual yang jelas. Formulir penambahan produk menggunakan kelas bg-white shadow-md rounded-lg p-6, yang memberikan latar belakang putih bersih dengan bayangan halus dan sudut yang dibulatkan, menciptakan tampilan yang modern dan rapi.

    Setiap field dalam formulir dirender menggunakan loop, di mana label ditampilkan dengan kelas mb-2 font-semibold text-gray-700 untuk memberikan kontras yang baik. Ketika ada teks bantuan atau kesalahan, informasi tersebut ditampilkan di bawah field dengan styling yang sesuai: teks bantuan menggunakan kelas mt-1 text-sm text-gray-500 dan pesan kesalahan menggunakan kelas mt-1 text-sm text-red-600. Tombol "Add Product" di bagian bawah form memiliki desain responsif, dengan kelas bg-indigo-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 transition duration-300 ease-in-out w-full,


  *Kustomisasi halaman daftar product menjadi lebih menarik dan responsive.*
  -> Struktur halaman dimulai dengan mewarisi dari base.html dan memuat navbar untuk navigasi. Konten utama diatur dalam div dengan kelas overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen bg-white flex flex-col, yang memberikan tampilan bersih dengan padding yang sesuai dan memastikan bahwa halaman memenuhi tinggi layar minimum. Informasi pengguna seperti NPM, Nama, dan Kelas ditampilkan dalam grid responsif menggunakan kelas grid grid-cols-1 z-30 md:grid-cols-3 gap-8, sehingga informasi ini teratur dengan baik. Juga terdapat area untuk menampilkan waktu login terakhir dengan styling yang konsisten, menggunakan latar belakang indigo dan teks putih untuk memastikan keterbacaan.

  Kondisi ketika tidak ada produk yang terdaftar ditangani dengan baik menggunakan struktur kondisional {% if not product_entry %}. Jika tidak ada produk, halaman akan menampilkan pesan dengan gambar sedih, menggunakan styling untuk memusatkan konten dan memberikan penjelasan bahwa belum ada produk yang ditambahkan. Pesan ini menggunakan kelas text-center text-gray-600 untuk memastikan keterbacaan. Sebaliknya, jika ada produk yang terdaftar, mereka akan ditampilkan dalam kolom dengan kelas columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full, yang memungkinkan produk ditampilkan dalam format kolom responsif. Setiap produk dirender menggunakan template card_product.html, memberikan konsistensi desain saat menampilkan informasi produk.

*Button untuk mengedit dan dan menghapus product*
-> Struktur utama produk dibungkus dalam div dengan kelas relative dan bg-indigo-100, yang memberikan latar belakang berwarna biru muda, dilengkapi dengan bayangan (shadow-md) dan sudut yang dibulatkan (rounded-lg). Judul produk dan informasi waktu ditampilkan dalam bagian atas kartu, dengan latar belakang gelap (bg-indigo-900) dan teks putih untuk memastikan keterbacaan yang baik. Selain itu, terdapat elemen visual seperti garis-garis kecil yang dibuat dengan div absolute, menambah dimensi dan menarik perhatian pada kartu produk.

Terdapat dua tombol untuk mengedit dan menghapus produk, masing-masing dirancang dengan warna yang mencolok untuk memberikan umpan balik visual yang jelas kepada pengguna. Tombol edit menggunakan warna hijau (bg-emerald-400) dengan ikon pensil, sementara tombol hapus menggunakan warna merah (bg-red-500) dengan ikon tempat sampah. Kedua tombol ini memiliki efek hover yang meningkatkan warna latar belakang dan animate bounce ketika kursor diarahkan.

*Navbar responsive*
->Struktur navbar ditetapkan dengan kelas bg-indigo-950 shadow-lg fixed top-0 left-0 z-40 w-screen, yang memberikan latar belakang biru tua, efek bayangan, dan memastikan bahwa navbar selalu berada di bagian atas halaman. Di dalam navbar, terdapat div dengan kelas max-w-7xl mx-auto px-4 sm:px-6 lg:px-8, yang mengatur lebar maksimum navbar dan memastikan konten berada di tengah layar, dengan padding horizontal yang responsif. Penggunaan kelas flex pada div yang berisi item navbar memungkinkan elemen-elemennya untuk disusun secara horizontal dan memusatkan konten, menjadikan tampilan navbar lebih terorganisir.

Untuk implementasi responsivitas, terdapat dua bagian penting: elemen yang ditampilkan berdasarkan ukuran layar dan tombol menu mobile. Pada tampilan desktop (md:flex), menu dengan tautan untuk login dan logout ditampilkan dengan jelas, sedangkan pada tampilan mobile (md:hidden), hanya ditampilkan tombol menu dengan ikon tiga stak. Kelas mobile-menu juga tersembunyi secara default dan ditampilkan hanya ketika tombol ditekan.

</details>

<details>
<summary>--TUGAS 6--</summary>
*Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!*
->

  1.Interaktivitas pada Sisi Klien 
  -> JavaScript memungkinkan halaman web menjadi interaktif dan responsif tanpa sering menghubungi server, sehingga meningkatkan pengalaman pengguna.

  2.Kompatibilitas dengan Berbagai Browser
  -> JavaScript kompatibel dengan semua browser utama, memastikan pengalaman pengguna yang konsisten di berbagai perangkat.

  3.Ekosistem yang Beragam
  -> Tersedia banyak framework dan pustaka seperti React dan Angular yang mempermudah pengembangan aplikasi web.

  4.Performa 
  -> Eksekusi JavaScript di sisi klien mengurangi beban server dan mempercepat kinerja aplikasi web.

  5.Dukungan Komunitas 
  -> Komunitas JavaScript sangat besar dan aktif, menyediakan banyak sumber daya, solusi, dan dukungan bagi pengembang.

  6.Adaptabilitas untuk Front-End dan Back-End: 
  -> JavaScript dapat digunakan untuk pengembangan baik di sisi depan (front-end) maupun belakang (back-end), misalnya dengan Node.js.

  7.Desain Web Responsif 
  -> JavaScript memungkinkan pembuatan desain web yang dapat menyesuaikan diri dengan berbagai ukuran layar, sehingga cocok untuk perangkat apa pun.

*Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?*
->
  Penggunaan `await` dalam JavaScript saat menggunakan `fetch()` berfungsi untuk menunda eksekusi kode hingga proses pengambilan data dari server selesai. Dengan menggunakan `await`, kita memastikan bahwa program menunggu hasil dari `fetch()` sebelum melanjutkan ke baris kode berikutnya. Ini memungkinkan kita untuk langsung bekerja dengan data yang diterima tanpa perlu menggunakan callback atau chaining `.then()`, sehingga kode menjadi lebih sederhana dan mudah dipahami.

  Jika `await` tidak digunakan, `fetch()` akan segera mengembalikan sebuah `Promise` dan kode berikutnya akan dieksekusi tanpa menunggu hasilnya. Akibatnya, kita tidak dapat langsung mengakses data dari respons karena program belum menyelesaikan proses pengambilan data dari server. Tanpa `await`, kita harus menggunakan metode seperti `.then()` untuk menangani respons setelah `Promise` selesai, yang bisa membuat kode menjadi lebih rumit dan kurang intuitif.


*Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?*
->
  Decorator `csrf_exempt` digunakan pada view yang menerima AJAX POST untuk menonaktifkan pengecekan token CSRF oleh Django. Ini diperlukan karena secara default, Django memerlukan token CSRF pada setiap permintaan POST untuk mencegah serangan CSRF. AJAX POST, terutama yang dibuat dengan JavaScript murni atau dari sumber eksternal, mungkin tidak mengirimkan token ini dengan benar. Dengan menggunakan `csrf_exempt`, kita memastikan bahwa permintaan AJAX dapat diproses tanpa gagal, tetapi harus digunakan dengan hati-hati untuk menghindari risiko keamanan.

*Pada tutorial PBP minggu ini,embersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?*
->
  Pembersihan data input pengguna tetap harus dilakukan di backend karena keamanan dan keandalannya tidak bisa dijamin jika hanya dilakukan di frontend. Validasi dan sanitasi di frontend bisa dilewati atau dimodifikasi oleh pengguna yang berbahaya menggunakan alat seperti browser developer tools atau skrip khusus. Dengan melakukan pembersihan data di backend, kita memastikan bahwa data yang diterima aplikasi benar-benar aman dan valid, terlepas dari bagaimana data tersebut dikirim, sehingga mengurangi risiko serangan seperti SQL Injection, XSS, dan bentuk-bentuk manipulasi data lainnya.


*Implementasi Checklist*
->
  -AJAX GET
    Pertama-tama saya menghapus kode `product_entry = Product.objects.filter(user=request.user)` dan `product_entry = product_entry` pada show_main di views.py. Setelah itu pada main.html saya menghapus block conditional yang menampilkan isi dari product_entry dan menggantinya dengan '`<div id="product_entry_cards"></div>`

    Lalu saya menambahkan block <script> yang berisi sebuah async function yang melakukan fetch API ke data json dengan kode return fetch("{% url 'main:show_json' %}").then((res) => res.json()) lalu di parse menjadi objek JavaScript. Lalu saya juga membuat suatu asyncfunction yang berguna untuk mengecek apakah product_entry memiliki isi atau tidak jika ada maka akan menampilkan card-card yang berisi product-product tersebut menggunakan `document.getElementById("product_entry_cards").className = classNameString;
    document.getElementById("product_entry_cards").innerHTML = htmlString` sesuai dengan id yang sudah saya buat sebelumnya.

  -AJAX POST
    Pertama-tama saya membuat tombol pada halaman utama yang memicu modal untuk menambahkan product baru. Tombol ini didefinisikan sebagai berikut:
    `<button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">`
      `Add New Product by AJAX`
    `</button>`

    Ketika tombol ditekan, fungsi showModal() dipanggil untuk menampilkan modal. Fungsi ini mengubah kelas elemen modal sehingga modal menjadi terlihat. Modal berisi form yang dirancang untuk menerima input product dari pengguna. Setelah pengguna mengisi form, tombol submit digunakan untuk mengirimkan data tersebut.

    Tahapan kedua adalah pembuatan view baru di backend untuk menangani data dari form yang dikirim menggunakan AJAX. View ini terhubung dengan URL yang didefinisikan sebagai /create-ajax/ yaitu function pada views.py sebagai berikut:

    @csrf_exempt
    @require_POST
    def add_product_entry_ajax(request):
    
      name = strip_tags(request.POST.get("name"))
      price = request.POST.get("price")
      description = strip_tags(request.POST.get("description"))
      user = request.user

      new_product = Product(
          name=name, price=price,
          description=description,
          user=user
      )
      new_product.save()

      return HttpResponse(b"CREATED", status=201)
    
    Permintaan AJAX dilakukan menggunakan fungsi fetch() sebagai berikut:   

        fetch("{% url 'main:add_product_entry_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#ProductForm')),
    })
    .then(response => refreshProductEntries())

    Fungsi ini mengirim data dari form ke view backend secara asinkronus tanpa me-refresh halaman. Jika pengiriman data berhasil, fungsi refreshProductEntries() akan dipanggil untuk memperbarui daftar mood.

    Tahapan terakhir melibatkan pembaruan daftar mood secara asinkronus di halaman utama setelah data mood baru berhasil ditambahkan. Fungsi refreshProductEntries() digunakan untuk mengambil daftar mood terbaru dari server menggunakan AJAX dan memperbarui elemen DOM tanpa memuat ulang seluruh halaman. Ini dilakukan dengan mengosongkan elemen HTML yang menampung card product dan menambahkan card baru berdasarkan data yang diperoleh dari server.


</details>


