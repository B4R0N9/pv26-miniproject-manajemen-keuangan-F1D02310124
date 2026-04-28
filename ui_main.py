from PySide6.QtWidgets import *
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Manajemen Keuangan")

        # MENU
        menubar = self.menuBar()
        menu = menubar.addMenu("Tentang")

        self.about_action = QAction("Tentang Aplikasi", self)
        menu.addAction(self.about_action)

        # TABLE
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "ID", "Nama", "Tanggal", "Jenis", "Jumlah", "Keterangan"
        ])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setAlternatingRowColors(True)

        # LABEL
        self.label_user = QLabel("Nama: Danuarta Wiraguna | NIM: F1D02310124")
        self.label_total = QLabel("Total: 0")

        # BUTTON
        self.btn_tambah = QPushButton("Tambah")
        self.btn_edit = QPushButton("Edit")
        self.btn_hapus = QPushButton("Hapus")

        self.btn_edit.setObjectName("edit")
        self.btn_hapus.setObjectName("hapus")

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_tambah)
        btn_layout.addWidget(self.btn_edit)
        btn_layout.addWidget(self.btn_hapus)

        layout = QVBoxLayout()
        layout.addWidget(self.label_user)
        layout.addWidget(self.table)
        layout.addLayout(btn_layout)
        layout.addWidget(self.label_total)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)