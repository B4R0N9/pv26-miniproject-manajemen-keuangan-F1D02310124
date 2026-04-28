import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from ui_main import MainWindow
from dialog_form import FormDialog
import database

class App(MainWindow):
    def __init__(self):
        super().__init__()

        database.create_table()
        self.load_data()

        self.btn_tambah.clicked.connect(self.tambah)
        self.btn_edit.clicked.connect(self.edit)
        self.btn_hapus.clicked.connect(self.hapus)
        self.about_action.triggered.connect(self.tentang)

    def load_data(self):
        data = database.get_data()
        self.table.setRowCount(len(data))

        for row_idx, row in enumerate(data):
            for col_idx, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row_idx, col_idx, item)

        self.update_total()

    def update_total(self):
        pemasukan, pengeluaran = database.get_total()
        pemasukan = pemasukan or 0
        pengeluaran = pengeluaran or 0

        self.label_total.setText(
            f"Pemasukan: {pemasukan} | Pengeluaran: {pengeluaran}"
        )

    def tambah(self):
        dialog = FormDialog()
        if dialog.exec():
            database.tambah_data(dialog.get_data())
            self.load_data()

    def edit(self):
        row = self.table.currentRow()

        if row < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data dulu!")
            return

        try:
            id = int(self.table.item(row, 0).text())
            nama = self.table.item(row, 1).text()
            tanggal = self.table.item(row, 2).text()
            jenis = self.table.item(row, 3).text()
            jumlah = int(self.table.item(row, 4).text())
            keterangan = self.table.item(row, 5).text()
        except:
            QMessageBox.warning(self, "Error", "Data tidak valid!")
            return

        data = (id, nama, tanggal, jenis, jumlah, keterangan)
        dialog = FormDialog(data)

        if dialog.exec():
            database.update_data(id, dialog.get_data())
            self.load_data()
            QMessageBox.information(self, "Sukses", "Data berhasil diupdate!")

    def hapus(self):
        row = self.table.currentRow()

        if row < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data dulu!")
            return

        id = int(self.table.item(row, 0).text())

        confirm = QMessageBox.question(
            self, "Konfirmasi", "Yakin hapus data?"
        )

        if confirm == QMessageBox.Yes:
            database.hapus_data(id)
            self.load_data()

    def tentang(self):
        QMessageBox.information(
            self,
            "Tentang",
            "Aplikasi Manajemen Keuangan\n\nNama: Danuarta Wiraguna\nNIM: F1D02310124"
        )

app = QApplication(sys.argv)

with open("style.qss", "r", encoding="utf-8") as f:
    app.setStyleSheet(f.read())

window = App()
window.show()
sys.exit(app.exec())