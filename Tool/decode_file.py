from Crypto.Cipher import ARC4
import binascii

def decrypt_rc4_file(input_file, output_file, key):
    try:
        # Đọc dữ liệu từ file input
        with open(input_file, 'r') as file:
            hex_data = file.read().strip()
        
        # Chuyển chuỗi hex về dạng bytes
        encrypted_data = binascii.unhexlify(hex_data)
        
        # Tạo đối tượng giải mã RC4
        cipher = ARC4.new(key.encode('utf-8'))
        
        # Giải mã dữ liệu
        decrypted_data = cipher.decrypt(encrypted_data)
        
        # Ghi dữ liệu đã giải mã ra file output
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(decrypted_data.decode('utf-8', errors='replace'))
        
        print(f"Đã giải mã thành công! Dữ liệu được lưu tại: {output_file}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Đường dẫn file input, file output, và khóa giải mã
input_file = "input/exitsign.lrc"    # Thay bằng đường dẫn file input
output_file = "py/lrc/exitsign.lrc"  # Thay bằng đường dẫn file output
key = "Lyr1cjust4nct"       # Khóa giải mã

# Gọi hàm để giải mã
decrypt_rc4_file(input_file, output_file, key)
#lấy file input ở nhaccuatui.com 