import sqlite3


def create_database():
    conn = sqlite3.connect('quan_ly_ban_hang.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        stock INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT,
        address TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        order_date TEXT NOT NULL,
        status TEXT NOT NULL,
        total REAL NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS order_items (
        order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        FOREIGN KEY (order_id) REFERENCES orders (order_id),
        FOREIGN KEY (product_id) REFERENCES products (product_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS feedback (
        feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        feedback_text TEXT NOT NULL,
        response_text TEXT,
        status TEXT NOT NULL DEFAULT 'pending',
        created_at TEXT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
    )
    ''')

    # Thêm tài khoản người dùng mặc định
    cursor.execute('''
    INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)
    ''', ('admin', 'password', 'admin'))

    conn.commit()
    conn.close()


create_database()
Bước
2: Tạo
form
đăng
nhập
Form
đăng
nhập
bằng
Tkinter
python
Sao
chép
mã
import sqlite3
from tkinter import *
from tkinter import messagebox


def dang_nhap():
    conn = sqlite3.connect('quan_ly_ban_hang.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                   (entry_ten_dang_nhap.get(), entry_mat_khau.get()))
    user = cursor.fetchone()
    if user:
        messagebox.showinfo("Đăng nhập", "Đăng nhập thành công!")
        root.destroy()
        mo_cua_so_chinh()
    else:
        messagebox.showerror("Đăng nhập", "Tên đăng nhập hoặc mật khẩu không đúng")
    conn.close()


def mo_cua_so_chinh():
    cua_so_chinh = Tk()
    cua_so_chinh.title("Hệ thống quản lý bán hàng")

    Button(cua_so_chinh, text="Quản lý sản phẩm", command=quan_ly_san_pham).pack(pady=10)
    Button(cua_so_chinh, text="Quản lý khách hàng", command=quan_ly_khach_hang).pack(pady=10)
    Button(cua_so_chinh, text="Quản lý đơn hàng", command=quan_ly_don_hang).pack(pady=10)
    Button(cua_so_chinh, text="Xem báo cáo", command=xem_bao_cao).pack(pady=10)
    Button(cua_so_chinh, text="Phản hồi", command=quan_ly_phan_hoi).pack(pady=10)

    cua_so_chinh.mainloop()


def quan_ly_san_pham():
    cua_so_san_pham = Toplevel()
    cua_so_san_pham.title("Quản lý sản phẩm")

    def them_san_pham():
        conn = sqlite3.connect('quan_ly_ban_hang.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, description, price, stock) VALUES (?, ?, ?, ?)",
                       (entry_ten_san_pham.get(), entry_mo_ta.get(), entry_gia.get(), entry_so_luong.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Thêm sản phẩm thành công")
        cua_so_san_pham.destroy()

    Label(cua_so_san_pham, text="Tên sản phẩm").grid(row=0, column=0)
    entry_ten_san_pham = Entry(cua_so_san_pham)
    entry_ten_san_pham.grid(row=0, column=1)

    Label(cua_so_san_pham, text="Mô tả").grid(row=1, column=0)
    entry_mo_ta = Entry(cua_so_san_pham)
    entry_mo_ta.grid(row=1, column=1)

    Label(cua_so_san_pham, text="Giá").grid(row=2, column=0)
    entry_gia = Entry(cua_so_san_pham)
    entry_gia.grid(row=2, column=1)

    Label(cua_so_san_pham, text="Số lượng").grid(row=3, column=0)
    entry_so_luong = Entry(cua_so_san_pham)
    entry_so_luong.grid(row=3, column=1)

    Button(cua_so_san_pham, text="Thêm sản phẩm", command=them_san_pham).grid(row=4, column=0, columnspan=2)

    cua_so_san_pham.mainloop()


def quan_ly_khach_hang():
    cua_so_khach_hang = Toplevel()
    cua_so_khach_hang.title("Quản lý khách hàng")

    def them_khach_hang():
        conn = sqlite3.connect('quan_ly_ban_hang.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customers (name, email, phone, address) VALUES (?, ?, ?, ?)",
                       (entry_ten.get(), entry_email.get(), entry_dien_thoai.get(), entry_dia_chi.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Thêm khách hàng thành công")
        cua_so_khach_hang.destroy()

    Label(cua_so_khach_hang, text="Tên khách hàng").grid(row=0, column=0)
    entry_ten = Entry(cua_so_khach_hang)
    entry_ten.grid(row=0, column=1)

    Label(cua_so_khach_hang, text="Email").grid(row=1, column=0)
    entry_email = Entry(cua_so_khach_hang)
    entry_email.grid(row=1, column=1)

    Label(cua_so_khach_hang, text="Điện thoại").grid(row=2, column=0)
    entry_dien_thoai = Entry(cua_so_khach_hang)
    entry_dien_thoai.grid(row=2, column=1)

    Label(cua_so_khach_hang, text="Địa chỉ").grid(row=3, column=0)
    entry_dia_chi = Entry(cua_so_khach_hang)
    entry_dia_chi.grid(row=3, column=1)

    Button(cua_so_khach_hang, text="Thêm khách hàng", command=them_khach_hang).grid(row=4, column=0, columnspan=2)

    cua_so_khach_hang.mainloop()


def quan_ly_don_hang():
    cua_so_don_hang = Toplevel()
    cua_so_don_hang.title("Quản lý đơn hàng")

    def them_don_hang():
        conn = sqlite3.connect('quan_ly_ban_hang.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders (customer_id, order_date, status, total) VALUES (?, ?, ?, ?)",
                       (entry_ma_khach_hang.get(), entry_ngay_dat.get(), entry_trang_thai.get(), entry_tong_tien.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Thêm đơn hàng thành công")
        cua_so_don_hang.destroy()

    Label(cua_so_don_hang, text="Mã khách hàng").grid(row=0, column=0)
    entry_ma_khach_hang = Entry(cua_so_don_hang)
    entry_ma_khach_hang.grid(row=0, column=1)

    Label(cua_so_don_hang, text="Ngày đặt hàng").grid(row=1, column=0)
    entry_ngay_dat = Entry(cua_so_don_hang)
    entry_ngay_dat.grid(row=1, column=1)

    Label(cua_so_don_hang, text="Trạng thái").grid(row=2, column=0)


tiep
di

ChatGPT
Cảm
ơn! Tiếp
tục
từ
phần
còn
thiếu
của
form
quản
lý
đơn
hàng
và
các
phần
tiếp
theo:

python
Sao
chép
mã
entry_trang_thai = Entry(cua_so_don_hang)
entry_trang_thai.grid(row=2, column=1)

Label(cua_so_don_hang, text="Tổng tiền").grid(row=3, column=0)
entry_tong_tien = Entry(cua_so_don_hang)
entry_tong_tien.grid(row=3, column=1)

Button(cua_so_don_hang, text="Thêm đơn hàng", command=them_don_hang).grid(row=4, column=0, columnspan=2)

cua_so_don_hang.mainloop()


def xem_bao_cao():
    cua_so_bao_cao = Toplevel()
    cua_so_bao_cao.title("Xem báo cáo")

    def bao_cao_doanh_thu_thang():
        conn = sqlite3.connect('quan_ly_ban_hang.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT strftime('%Y-%m', order_date) as thang, SUM(total) as doanh_thu FROM orders GROUP BY thang")
        bao_cao = cursor.fetchall()
        text_bao_cao.delete(1.0, END)
        for row in bao_cao:
            text_bao_cao.insert(END, f"Tháng: {row[0]}, Doanh thu: {row[1]}\n")
        conn.close()

    def bao_cao_san_pham_ban_chay():
        conn = sqlite3.connect('quan_ly_ban_hang.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT p.name, SUM(oi.quantity) as so_luong FROM order_items oi JOIN products p ON oi.product_id = p.product_id GROUP BY p.name ORDER BY so_luong DESC")
        bao_cao = cursor.fetchall()
        text_bao_cao.delete(1.0, END)
        for row in bao_cao:
            text_bao_cao.insert(END, f"Sản phẩm: {row[0]}, Số lượng bán: {row[1]}\n")
        conn.close()

    Button(cua_so_bao_cao, text="Báo cáo doanh thu tháng", command=bao_cao_doanh_thu_thang).pack(pady=10)
    Button(cua_so_bao_cao, text="Báo cáo sản phẩm bán chạy", command=bao_cao_san_pham_ban_chay).pack(pady=10)

    text_bao_cao = Text(cua_so_bao_cao, width=50, height=20)
    text_bao_cao.pack(pady=10)

    cua_so_bao_cao.mainloop()


def quan_ly_phan_hoi():
    cua_so_phan_hoi = Toplevel()
    cua_so_phan_hoi.title("Quản lý phản hồi")

    def gui_phan_hoi():
        conn = sqlite3.connect('quan_ly_ban_hang.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback (customer_id, feedback_text, created_at) VALUES (?, ?, ?)",
                       (entry_ma_khach_hang.get(), entry_noi_dung.get("1.0", END), entry_ngay_tao.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Gửi phản hồi thành công")
        cua_so_phan_hoi.destroy()

    Label(cua_so_phan_hoi, text="Mã khách hàng").grid(row=0, column=0)
    entry_ma_khach_hang = Entry(cua_so_phan_hoi)
    entry_ma_khach_hang.grid(row=0, column=1)

    Label(cua_so_phan_hoi, text="Nội dung").grid(row=1, column=0)
    entry_noi_dung = Text(cua_so_phan_hoi, width=40, height=10)
    entry_noi_dung.grid(row=1, column=1)

    Label(cua_so_phan_hoi, text="Ngày tạo").grid(row=2, column=0)
    entry_ngay_tao = Entry(cua_so_phan_hoi)
    entry_ngay_tao.grid(row=2, column=1)

    Button(cua_so_phan_hoi, text="Gửi phản hồi", command=gui_phan_hoi).grid(row=3, column=0, columnspan=2)

    cua_so_phan_hoi.mainloop()


root = Tk()
root.title("Form đăng nhập")

Label(root, text="Tên đăng nhập").grid(row=0, column=0)
entry_ten_dang_nhap = Entry(root)
entry_ten_dang_nhap.grid(row=0, column=1)

Label(root, text="Mật khẩu").grid(row=1, column=0)
entry_mat_khau = Entry(root, show="*")
entry_mat_khau.grid(row=1, column=1)

Button(root, text="Đăng nhập", command=dang_nhap).grid(row=2, column=0, columnspan=2)

root.mainloop()