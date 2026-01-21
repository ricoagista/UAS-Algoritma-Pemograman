# Program Binary Search Tree & Binary Traversal

Project ini dibuat untuk memenuhi tugas **Ujian Akhir Semester (UAS)**  
mata kuliah **Algoritma Pemrograman**.

Program mengimplementasikan dua studi kasus:
1. **Binary Search Tree (BST)**
2. **Binary Traversal** (InOrder, PreOrder, dan PostOrder)

Aplikasi bersifat **interaktif** dan dibuat menggunakan bahasa **Python** dengan antarmuka sederhana berbasis **Tkinter**.

---

## 👥 Anggota Kelompok
- Mohammad akbar noviandi – 388
- Figa Brilliant Daffa – 424
- Dicky Ihsan Novanda – 426  
- Rico Shandika Jovial Agista – 433  

---

## 📌 Deskripsi Singkat Program
Binary Search Tree adalah struktur data berbentuk pohon biner dengan aturan:
- Nilai lebih kecil dari root berada di subtree kiri
- Nilai lebih besar dari root berada di subtree kanan

Program ini memungkinkan pengguna untuk:
- Memasukkan data numerik ke dalam BST
- Menampilkan hasil traversal pohon menggunakan:
  - InOrder
  - PreOrder
  - PostOrder

Traversal digunakan untuk mengunjungi seluruh node dalam urutan tertentu sesuai algoritma yang dipilih.

---

## ⚙️ Fitur Program
- Input data angka oleh user
- Insert node ke Binary Search Tree
- Traversal InOrder (Left – Root – Right)
- Traversal PreOrder (Root – Left – Right)
- Traversal PostOrder (Left – Right – Root)
- Antarmuka interaktif menggunakan Tkinter

---

## 🧠 Penjelasan Algoritma

### 1. Binary Search Tree (BST)
BST menyimpan data secara terstruktur dengan aturan kiri dan kanan.  
Proses insert dilakukan secara **rekursif** hingga menemukan posisi yang sesuai.

Keunggulan BST:
- Data tersimpan terurut secara logis
- Proses pencarian lebih efisien dibanding struktur linear

### 2. Binary Traversal
Traversal adalah proses mengunjungi seluruh node dalam pohon.

- **InOrder Traversal**  
  Mengunjungi subtree kiri, root, lalu subtree kanan.  
  Pada BST, traversal ini menghasilkan data **terurut menaik (ascending)**.

- **PreOrder Traversal**  
  Mengunjungi root terlebih dahulu, lalu subtree kiri dan kanan.  
  Cocok untuk menyalin struktur pohon.

- **PostOrder Traversal**  
  Mengunjungi subtree kiri dan kanan terlebih dahulu, lalu root.  
  Sering digunakan untuk penghapusan struktur pohon.

---

## ▶️ Cara Menjalankan Program
Pastikan Python sudah terinstall (versi 3.x).

1. Clone repository ini:
   ```bash
   git clone https://github.com/ricoagista/UAS-Algoritma-Pemograman.git