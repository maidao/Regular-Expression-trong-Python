import re

"""
re.sub(pattern, repl, string, max=0)

---> Phương thức này thay thế tất cả sự xuất hiện của pattern trong string với repl. 
---> Phương thức này sẽ thay thế tất cả sự xuất hiện trừ khi bạn cung cấp tham số max. 
---> Phương thức này trả về chuỗi đã được sửa đổi.
"""
phone = "01633-810-628 # Day la so dien thoai"

# Xoa cac comment
num = re.sub(r'#.*$', "", phone) # ---> r là viet tat cua: 'raw string'
print("So dien thoai : ", num)

# Xoa cac ky tu khong phai ky so
num = re.sub(r'\D', "", phone)
print("So dien thoai : ", num)