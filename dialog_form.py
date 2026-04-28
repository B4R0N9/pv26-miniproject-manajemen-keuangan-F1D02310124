from PySide6.QtWidgets import *

class FormDialog(QDialog):
    def __init__(self, data=None):
        super().__init__()

        self.setWindowTitle("Form Transaksi")

        self.nama = QLineEdit()
        self.tanggal = QLineEdit()
        self.jenis = QComboBox()
        self.jenis.addItems(["Pemasukan", "Pengeluaran"])
        self.jumlah = QLineEdit()
        self.keterangan = QLineEdit()

        # isi data kalau edit
        if data:
            self.nama.setText(str(data[1]))
            self.tanggal.setText(str(data[2]))
            self.jenis.setCurrentText(str(data[3]))
            self.jumlah.setText(str(data[4]))
            self.keterangan.setText(str(data[5]))

        form = QFormLayout()
        form.addRow("Nama", self.nama)
        form.addRow("Tanggal", self.tanggal)
        form.addRow("Jenis", self.jenis)
        form.addRow("Jumlah", self.jumlah)
        form.addRow("Keterangan", self.keterangan)

        btn = QPushButton("Simpan")
        btn.clicked.connect(self.simpan)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(btn)

        self.setLayout(layout)

    def simpan(self):
        if not self.nama.text() or not self.jumlah.text():
            QMessageBox.warning(self, "Error", "Data wajib diisi!")
            return

        try:
            int(self.jumlah.text())
        except:
            QMessageBox.warning(self, "Error", "Jumlah harus angka!")
            return

        self.accept()

    def get_data(self):
        return (
            self.nama.text(),
            self.tanggal.text(),
            self.jenis.currentText(),
            int(self.jumlah.text()),
            self.keterangan.text()
        )