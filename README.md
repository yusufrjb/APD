
# 🌤️ Surabaya Air Quality Dashboard

Aplikasi web interaktif berbasis Dash (Plotly) untuk memantau kualitas udara di Surabaya.  
Dashboard ini dilengkapi sidebar filter interaktif yang dapat dibuka/tutup dari sisi kiri (mirip Streamlit sidebar), dua grafik utama, dan tabel data dinamis.



## 🚀 Fitur Utama

✅ **Sidebar Filter Interaktif**
- Dapat dibuka/tutup melalui tombol “⚙️ Filter” di pojok kiri atas.
- Berisi kontrol `DatePickerRange` untuk memfilter data berdasarkan waktu.

✅ **Visualisasi Interaktif**
- Grafik AQI (Air Quality Index) terhadap waktu.
- Grafik suhu dan kelembapan (2 variabel sekaligus).
- Kedua grafik responsif dan dapat di-*hover* untuk melihat detail nilai.

✅ **Tabel Data Dinamis**
- Menampilkan data sesuai filter waktu.
- Dapat diurutkan (`sort_action`) dan difilter (`filter_action`) secara interaktif.

✅ **Desain Profesional dengan Bootstrap**
- Menggunakan `dash-bootstrap-components` dengan tema `Flatly`.
- Header biru elegan, card dengan bayangan lembut, dan layout responsif.

✅ **Arsitektur Modular**
- Data diambil dari file `data/aqi_surabaya.csv`.
- Sidebar terpisah dengan komponen `dbc.Offcanvas` (bisa ditarik masuk/keluar).

---

## 🧠 Arsitektur Sistem

```
📂 Project Directory
│
├── app_dash.py           # Aplikasi utama Dash + Bootstrap
├── data/
│   └── aqi_surabaya.csv  # Dataset kualitas udara (AQI, suhu, kelembapan)
├── requirements.txt      # Daftar dependensi Python
└── README.md             # Dokumentasi proyek
```


Alur sistem:
1. `app_dash.py` membaca data CSV (kolom: `timestamp`, `aqius`, `temp`, `humidity`).
2. Komponen Dash (`dcc.Graph`, `dash_table.DataTable`) menampilkan hasil dalam layout Bootstrap.
3. Sidebar (`dbc.Offcanvas`) menyediakan kontrol filter waktu.
4. Callback Dash memperbarui grafik & tabel secara otomatis sesuai filter.

---

## ⚙️ Framework & Library yang Digunakan

| Library | Fungsi |
|----------|---------|
| **Dash** | Framework utama untuk membangun web app Python. |
| **Plotly Express** | Visualisasi interaktif berbasis Plotly. |
| **Dash Bootstrap Components (dbc)** | Desain layout profesional dan responsif. |
| **Pandas** | Manipulasi data dari CSV. |

---

## 🧩 Instalasi & Menjalankan Aplikasi

1. **Clone atau download proyek ini**
   ```bash
   git clone https://github.com/yourusername/aqi-dashboard
   cd aqi-dashboard

2. **Buat virtual environment (opsional tapi disarankan)**

   ```bash
   python -m venv venv
   venv\Scripts\activate     # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. **Install dependensi**

   ```bash
   pip install -r requirements.txt
   ```

   atau manual:

   ```bash
   pip install dash plotly pandas dash-bootstrap-components
   ```

4. **Jalankan aplikasi**

   ```bash
   python app_dash.py
   ```

5. **Akses di browser**

   ```
   http://localhost:8050
   ```

---

## 📊 Contoh Data (`data/aqi_surabaya.csv`)

| timestamp           | aqius | temp | humidity |
| ------------------- | ----- | ---- | -------- |
| 2025-04-11T03:00:00 | 152   | 32   | 68       |
| 2025-04-11T04:00:00 | 120   | 31   | 70       |
| 2025-04-11T05:00:00 | 98    | 30   | 74       |

---

## 🌈 Tampilan Antarmuka

* **Navbar** biru dengan tombol `⚙️ Filter` di kiri atas.
* **Sidebar** meluncur dari kiri dengan kontrol filter waktu.
* **Dua grafik interaktif** berdampingan (AQI & Suhu/Kelembapan).
* **Tabel data** dengan kemampuan filter dan sort.
* Layout responsif (otomatis menyesuaikan layar laptop/tablet/ponsel).

---

## 📜 Lisensi

Proyek ini dilisensikan di bawah lisensi **MIT** — bebas digunakan untuk keperluan akademik maupun pengembangan pribadi.

---

👨‍💻 **Dibuat oleh:**
*Yusuf Rajabi*



