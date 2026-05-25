# print(' HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ');
# name_patient = input('Nhập tên bệnh nhân: ');
# age = int(input('Mời bạn nhập tuổi: '));
# symptom = input('Mời bạn nhập triệu chứng bênh: ');
# -print(' PHIẾU KHÁM BỆNH ');
# print ('Tên bệnh nhân:', symptom);
# print('Tuổi:', name_patient);
# print ('Triệu chứng:', age);

# đoạn code này vì sao chương trình không bị crash nhưng dữ liệu in ra sai
# vì ở các dòng print đang bị sai thứ tự biến để in ra
# do đó dẫn đến lỗi logic và dữ liệu in ra sai 

print(' HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ');
name_patient = input('Nhập tên bệnh nhân: ');
age = int(input('Mời bạn nhập tuổi: '));
symptom = input('Mời bạn nhập triệu chứng bênh: ');
print(' PHIẾU KHÁM BỆNH ');
print ('Tên bệnh nhân:', name_patient);
print('Tuổi:', age);
print ('Triệu chứng:', symptom);