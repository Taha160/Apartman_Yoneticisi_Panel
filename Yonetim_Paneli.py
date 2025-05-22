import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from Panel_ui import Panel_UI
from PyQt5.QtCore import QTimer


class MainWindow(QtWidgets.QMainWindow, Panel_UI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.create_table()

        self.pb_kayitekle.clicked.connect(self.kayit_ekle)
        self.pb_kayitlistele.clicked.connect(self.kayitlari_listele)
        self.pb_kayitsil.clicked.connect(self.kayit_sil)
        self.pb_sorgu.clicked.connect(self.kayit_sorgula)

        self.table_daireler.setHorizontalHeaderLabels(["Kat", "Daire No", "Ev Sahibi", "Aidat", "Borç"])

    def create_table(self):
        with sqlite3.connect("database_apartmanyoneticsi.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Daireler (
                    kat TEXT,
                    daire_no TEXT PRIMARY KEY,
                    ev_sahibi TEXT,
                    aidat REAL,
                    borc REAL
                )
            """)

    def kayit_ekle(self):
        try:
            kat = self.lne_kat.text().strip()
            daire_no = self.lne_daire.text().strip()
            ev_sahibi = self.lne_evsahibi.text().strip()
            aidat = self.lne_aidat.text().strip()
            borc = self.lne_borc.text().strip()
            

            if not (kat and daire_no and ev_sahibi and aidat and borc):
                QMessageBox.warning(self, "Eksik Bilgi", "Lütfen tüm alanları doldurun.")
                return

            with sqlite3.connect("database_apartmanyoneticsi.db", timeout=1.0) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 1 FROM Daireler WHERE daire_no = ?", (daire_no,))
                if cursor.fetchone():
                    QMessageBox.warning(self, "Uyarı", f"{daire_no} numaralı daire zaten kayıtlı!")
                    return

            cursor.execute("INSERT INTO Daireler VALUES (?, ?, ?, ?, ?)",
                           (kat, daire_no, ev_sahibi, float(aidat), float(borc)))
            conn.commit()

            QMessageBox.information(self, "Başarılı", "Kayıt başarıyla eklendi.")
            QTimer.singleShot(200, self.kayitlari_listele)

        except Exception as e:
            QMessageBox.critical(self, "Hata", str(e))


    def kayitlari_listele(self):
        self.table_daireler.setRowCount(0)
        with sqlite3.connect("database_apartmanyoneticsi.db", timeout=1.0) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Daireler")
            for i, row in enumerate(cursor.fetchall()):
                self.table_daireler.insertRow(i)
                for j, val in enumerate(row):
                    self.table_daireler.setItem(i, j, QTableWidgetItem(str(val)))
    
    def kayit_sil(self):
        secili_satir = self.table_daireler.currentRow()
        if secili_satir < 0:
            QMessageBox.warning(self, "Uyarı", "Lütfen silmek istediğiniz kaydı seçin.")
        
        daire_no = self.table_daireler.item(secili_satir,1).text()
        
        cevap = QMessageBox.question(self, "Onay", f"{daire_no} numaralı kaydı silmek istediğinize emin misiniz?",
                                     QMessageBox.Yes | QMessageBox.No)
        
        if cevap == QMessageBox.Yes:
            try:
                with sqlite3.connect("database_apartmanyoneticsi.db", timeout=1.0) as conn:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM Daireler WHERE daire_no = ?", (daire_no))
                    conn.commit()
                 
                QMessageBox.information(self, "Başarılı", "Kayıt silindi.")
                QTimer.singleShot(200, self.kayitlari_listele)
            except Exception as e:
               QMessageBox.critical(self, "Hata", str(e))    
    def kayit_sorgula(self):
        aranan = self.lne_sorgu.text().strip()
        if not aranan:
            QMessageBox.warning(self, "Uyarı", "Lütfen sorgulamak istediğiniz daire no'yu tuşlayın.")
            return
    
        self.table_daireler.setRowCount(0)
        
        try:
            with sqlite3.connect("database_apartmanyoneticsi.db", timeout=1.0) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Daireler WHERE daire_no = ?", (aranan,))
                sonuc = cursor.fetchone()
                if sonuc:
                    self.table_daireler.insertRow(0)
                    for j, val in enumerate(sonuc):
                        self.table_daireler.setItem(0,j, QTableWidgetItem(str(val)))
                else:
                    QMessageBox.information(self, "Sonuç", f"{aranan} numaralı daire bulunamadı.")
        except Exception as e:
            QMessageBox.critical(self, "Hata", str(e))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
