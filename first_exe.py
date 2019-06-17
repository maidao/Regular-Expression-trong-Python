import re

"""
Một Regular Expression là một dãy ký tự đặc biệt 
- giúp so khớp 
- tìm các chuỗi khác 
- tập hợp các chuỗi
 
= sử dụng một cú pháp riêng trong một pattern. 

Regular Expression được sử dụng phổ biến trong thế giới UNIX.

#################################################################

re Module:
- cung cấp sự hỗ trợ đầy đủ các Perl-like Regular Expression trong Python
- Module này tạo Exception là re.error nếu xảy ra một lỗi trong khi biên dịch 
hoặc khi sử dụng một Regular Expression.

##################################################################
1--- Hàm match trong Python: so khớp pattern với string và với các flag tùy ý

re.match(pattern, string, flags=0)

    + pattern: Đây là Regular Expression để được so khớp
    + string: Đây là chuỗi, mà sẽ được tìm kiếm để so khớp pattern tại phần đầu của chuỗi
    + flags: Bạn có thể xác định các flag khác nhau bởi sử dụng toán tử |. 
    
Hàm re.match trả về một đối tượng match nếu thành công và trả về None nếu thất bại. 
Chúng ta sử dụng hàm group(num) hoặc groups() của đối tượng match để lấy biểu thức đã được so khớp 

    + Phương thức group(num=0) trả về toàn bộ kết nối (hoặc num phân nhóm cụ thể).
    + Phương thức groups() trả về tất cả các phân nhóm kết nối trong một Tuple 
    (là trống nếu không có kết nối hay so khớp nào).
    
##################################################################
2--- Hàm search trong Python: tìm kiếm sự xuất hiện đầu tiên của pattern bên trong string với các flags tùy ý

re.search(pattern, string, flags=0)

    + Các tham số được giải thích như trong hàm match.

Hàm re.search trả về một đối tượng match nếu thành công và trả về None nếu thất bại. 
Chúng ta sử dụng hàm group(num) hoặc groups() của đối tượng match để lấy biểu thức đã được so khớp 

##################################################################
3--- Phân biệt match và search trong Python

Python cung cấp hai hoạt động cơ sở dựa trên Reguler Expression, đó là: 
    + match để kiểm tra chỉ một kết nối tại phần đầu của chuỗi
    + search tìm kiếm một kết nối ở bất cứ đâu trong chuỗi

"""

line = "thonpy Hoc py la de hon hoc Java?"

matchObj = re.match(r'(.*) la (.*?) .*', line, re.M|re.I)
searchObj = re.search(r'(.*) la (.*?) .*', line, re.M|re.I)


if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(0) : ", matchObj.group(0))
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
   #print("matchObj.group(3) : ", matchObj.group(3)) ---> loi vi word 'la' chi phan tach cau thanh 2 phan
else:
   print("Khong co ket noi!!")

if searchObj:
   print("searchObj.group() : ", searchObj.group())
   print("searchObj.group(1) : ", searchObj.group(1))
   print("searchObj.group(2) : ", searchObj.group(2))
else:
   print("Khong tim thay!!")

##################################################################
print('-------------------------------------------')
matchObj2 = re.match(r'thon', line, re.M|re.I)
searchObj2 = re.search(r'thon',line,re.M|re.I)

if matchObj2:
   print("matchObj.group() : ", matchObj2.group())
   # print("matchObj.group(1) : ", matchObj2.group(1))
else:
   print("Khong co ket noi voi match!!")

if searchObj2:
   print("searchObj.group() : ", searchObj2.group())
   #print("searchObj.group(1) : ", searchObj2.group(1))
else:
   print("Khong tim thay!!")