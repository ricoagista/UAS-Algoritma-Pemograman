import tkinter as tk
from tkinter import messagebox

# ==================================================
# KELAS NODE
# Merepresentasikan satu simpul (node) pada BST
# Setiap node memiliki:
# - data  : nilai integer
# - left  : anak kiri
# - right : anak kanan
# ==================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ==================================================
# KELAS BINARY SEARCH TREE
# Mengatur operasi utama pada BST:
# - insert data
# - traversal (InOrder, PreOrder, PostOrder)
#
# Aturan BST:
# - Nilai lebih kecil dari root -> ke kiri
# - Nilai lebih besar dari root -> ke kanan
# ==================================================
class BinarySearchTree:
    def __init__(self):
        # Root adalah node awal BST
        self.root = None

    # ------------------------------------------------
    # Fungsi insert (dipanggil dari luar)
    # ------------------------------------------------
    def insert(self, data):
        self.root = self._insert(self.root, data)

    # ------------------------------------------------
    # Fungsi insert rekursif
    # ------------------------------------------------
    def _insert(self, root, data):
        # Jika tree kosong, buat node baru
        if root is None:
            return Node(data)

        # Jika data lebih kecil, masuk ke subtree kiri
        if data < root.data:
            root.left = self._insert(root.left, data)

        # Jika data lebih besar, masuk ke subtree kanan
        elif data > root.data:
            root.right = self._insert(root.right, data)

        # Jika data sama, diabaikan (hindari duplikat)
        return root

    # ==================================================
    # TRAVERSAL INORDER
    # Urutan: Left -> Root -> Right
    # Pada BST, hasil traversal InOrder akan terurut
    # ==================================================
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append(root.data)
            self._inorder(root.right, result)

    # ==================================================
    # TRAVERSAL PREORDER
    # Urutan: Root -> Left -> Right
    # Biasanya digunakan untuk menyalin struktur tree
    # ==================================================
    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, root, result):
        if root:
            result.append(root.data)
            self._preorder(root.left, result)
            self._preorder(root.right, result)

    # ==================================================
    # TRAVERSAL POSTORDER
    # Urutan: Left -> Right -> Root
    # Sering dipakai untuk proses penghapusan tree
    # ==================================================
    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, root, result):
        if root:
            self._postorder(root.left, result)
            self._postorder(root.right, result)
            result.append(root.data)


# ==================================================
# BAGIAN UI (INTERAKTIF)
# Menggunakan Tkinter sebagai antarmuka sederhana
# ==================================================
bst = BinarySearchTree()

# --------------------------------------------------
# Fungsi untuk memasukkan nilai ke BST
# --------------------------------------------------
def insert_value():
    try:
        # Ambil input user dan ubah ke integer
        value = int(entry.get())
        bst.insert(value)
        entry.delete(0, tk.END)
        output_label.config(
            text=f"Nilai {value} berhasil dimasukkan ke Binary Search Tree"
        )
    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka!")

# --------------------------------------------------
# Menampilkan hasil traversal InOrder
# --------------------------------------------------
def show_inorder():
    result = bst.inorder()
    output_label.config(
        text="Traversal InOrder (Left - Root - Right):\n" +
        " ".join(map(str, result))
    )

# --------------------------------------------------
# Menampilkan hasil traversal PreOrder
# --------------------------------------------------
def show_preorder():
    result = bst.preorder()
    output_label.config(
        text="Traversal PreOrder (Root - Left - Right):\n" +
        " ".join(map(str, result))
    )

# --------------------------------------------------
# Menampilkan hasil traversal PostOrder
# --------------------------------------------------
def show_postorder():
    result = bst.postorder()
    output_label.config(
        text="Traversal PostOrder (Left - Right - Root):\n" +
        " ".join(map(str, result))
    )


# ==================================================
# SETUP WINDOW
# ==================================================
root = tk.Tk()
root.title("Implementasi Binary Search Tree")
root.geometry("420x420")

title = tk.Label(
    root,
    text="Program Binary Search Tree & Traversal",
    font=("Arial", 13, "bold")
)
title.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

btn_insert = tk.Button(root, text="Insert Node", command=insert_value)
btn_insert.pack(pady=5)

btn_inorder = tk.Button(root, text="InOrder Traversal", command=show_inorder)
btn_inorder.pack(pady=5)

btn_preorder = tk.Button(root, text="PreOrder Traversal", command=show_preorder)
btn_preorder.pack(pady=5)

btn_postorder = tk.Button(root, text="PostOrder Traversal", command=show_postorder)
btn_postorder.pack(pady=5)

output_label = tk.Label(
    root,
    text="",
    wraplength=380,
    justify="center"
)
output_label.pack(pady=20)

root.mainloop()
