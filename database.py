import sqlite3

conn = sqlite3.connect("keuangan.db")
cursor = conn.cursor()

def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transaksi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        tanggal TEXT,
        jenis TEXT,
        jumlah INTEGER,
        keterangan TEXT
    )
    """)
    conn.commit()

def tambah_data(data):
    cursor.execute("""
    INSERT INTO transaksi (nama, tanggal, jenis, jumlah, keterangan)
    VALUES (?, ?, ?, ?, ?)
    """, data)
    conn.commit()

def get_data():
    cursor.execute("SELECT * FROM transaksi")
    return cursor.fetchall()

def hapus_data(id):
    cursor.execute("DELETE FROM transaksi WHERE id=?", (id,))
    conn.commit()

def update_data(id, data):
    cursor.execute("""
    UPDATE transaksi 
    SET nama=?, tanggal=?, jenis=?, jumlah=?, keterangan=?
    WHERE id=?
    """, (*data, id))
    conn.commit()

def get_total():
    cursor.execute("""
    SELECT 
        SUM(CASE WHEN jenis='Pemasukan' THEN jumlah ELSE 0 END),
        SUM(CASE WHEN jenis='Pengeluaran' THEN jumlah ELSE 0 END)
    FROM transaksi
    """)
    return cursor.fetchone()