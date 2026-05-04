import random

print("Chào mừng bạn đến với Trò Chơi Đoán Số!")
print("Mình đã chọn một số bí mật từ 1 đến 100. Bạn hãy thử đoán xem đó là số mấy nhé!")
print("-" * 50)

# Máy tính chọn một số ngẫu nhiên từ 1 đến 100
so_bi_mat = random.randint(1, 100)
so_lan_doan = 0
doan_dung = False

# Vòng lặp tiếp tục cho đến khi người chơi đoán đúng
while not doan_dung:
    try:
        # Lấy số dự đoán từ người chơi
        du_doan_cua_ban = int(input("Nhập số bạn đoán: "))
        so_lan_doan += 1

        # Kiểm tra kết quả
        if du_doan_cua_ban < so_bi_mat:
            print("Hơi thấp rồi! Bạn thử số lớn hơn xem.")
        elif du_doan_cua_ban > so_bi_mat:
            print("Hơi cao rồi! Bạn thử số nhỏ hơn xem.")
        else:
            doan_dung = True
            print("-" * 50)
            print(f"CHÚC MỪNG! Bạn đã đoán chính xác số {so_bi_mat}.")
            print(f"Bạn đã mất {so_lan_doan} lần đoán để tìm ra kết quả.")
            
    except ValueError:
        # Xử lý lỗi nếu người chơi nhập chữ thay vì số
        print("Lỗi: Vui lòng nhập một con số hợp lệ (ví dụ: 10, 42).")