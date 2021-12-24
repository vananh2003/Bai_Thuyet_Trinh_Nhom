def NhapThongTin(Thongtin): # Hàm nhập thông tin
    User = []
    name = str(input("Họ và tên: ")) # Nhập tên
    try:
        age = int(input("Tuổi: ")) # Nhập tuổi
        sex = str.upper(input("Giới tính (NAM/NỮ): ")) #Nhập giới tính
        if (sex != 'NAM') and (sex != 'NỮ'): # Nếu nhập khác giới tính --> Lỗi
            raise Exception
        height = float(input("Chiều cao (cm): ")) # Nhập chiều cao
        weight = float(input("Cân nặng (kg): ")) # Nhập cân nặng
        print('''Tần suất tập thể thao của bạn: 
                    [1] Không có hoặc ít
                    [2] 1-3 ngày/tuần
                    [3] 3-5 ngày/tuần
                    [4] 6-7 ngày/tuần
                    [5] 2 lần/ngày''') # Nhập tần suất tập thể dục
        frequency = int(input("Câu trả lời của bạn là: "))
        if (frequency < 1) or (frequency > 5): # Nếu nhập ngoài giá trị liệt kê --> Lỗi
            raise Exception
        # Đưa giá trị đã nhập vô hàm
        User.append(name)
        User.append(age)
        User.append(sex)
        User.append(height)
        User.append(weight)
        User.append(frequency)
    except (ValueError, Exception): # Nhắc nhở và sửa lỗi
        print('Bạn đã nhập sai, vui lòng nhập lại thông tin')
    return User

def ChisoBMI(User, Thongtin): # Hàm tính chỉ số cân nặng
    BMI = ((User[Thongtin.index('Weight')])/(((User[Thongtin.index('Height')])/100))**2)
    return BMI

def NhanXet(BMI): #Đưa ra nhận xét dựa trên chỉ số BMI
    thin2 = 'Bạn đang bị suy dinh dưỡng, thiếu cân nghiêm trọng. Bạn cần đến bác sĩ ngay để điều trị thôi'
    thin1 = 'Bạn đang bị gầy. Bạn cần tăng cường bổ sung dưỡng chất trong chế độ ăn uống hàng ngày.'
    normal = 'Chỉ số lý tưởng. Bạn hãy tiếp tục chế độ sinh hoạt như hiện tại để duy trì chỉ số này.'
    fat1 = 'Bạn đang bị thừa cân. Bạn cần thay đổi chế độ ăn uống bằng cách giảm chất béo, đồ ngọt, tinh bột.'
    fat2 = '''Bạn đang bị tình trạng béo phì. Bạn cần ngay lập tức có kế hạch giảm cân khoa học và đến gặp 
    bác sĩ để được tư vấn chuyên môn về nguyên nhân.'''
    fat3 = 'Bạn đang gặp tình trạng béo phì nghiêm trọng. Bạn cần gặp bác sĩ ngay để điều trị kịp thời.'
    if BMI <= 16 : print(thin2)
    elif (BMI > 16) and (BMI < 18.5): print(thin1)
    elif (BMI >= 18.5) and (BMI < 23): print(normal)
    elif (BMI >= 23) and (BMI < 25): print(fat1)
    elif (BMI >= 25) and (BMI < 30): print(fat2)
    elif (BMI > 30): print(fat3)

def ChisoTDEE(User, Thongtin):
    #Tính Calo dựa trên giới tính
    if User[Thongtin.index('Sex')] == 'NAM':
        TDEE = float(10 * User[Thongtin.index('Height')] + 6.25 * User[Thongtin.index('Weight')] - 5 * User[Thongtin.index('Age')] + 5)
    else:
        TDEE = float(10 * User[Thongtin.index('Height')] + 6.25 * User[Thongtin.index('Weight')] - 5 * User[Thongtin.index('Age')] - 161)
    #Tính Calo dựa trên tần suất hoạt động (N)
    if User[Thongtin.index('Frequency')] == 1:
        TDEE = float(TDEE * 1.2)
    elif User[Thongtin.index('Frequency')] == 2:
        TDEE = float(TDEE * 1.375)
    elif User[Thongtin.index('Frequency')] == 3:
        TDEE = float(TDEE * 1.55)
    elif User[Thongtin.index('Frequency')] == 4:
        TDEE = float(TDEE * 1.725)
    else:
        TDEE = float(TDEE * 1.9)
    return TDEE

def TinhCaloMoiNgay(tongcalo): #Tính tổng calo đã bổ sung mỗi ngày
    calo = pandas.read_excel('Book1.xlsx') #Đọc file Excel
    calo_monan= calo['Món ăn'] #Gọi cột có Header "Món ăn"
    print('Hãy thực đơn trong ngày của bạn')
    while True:
        monan = str.upper(input('Nhập món ăn của bạn: '))
        j = 0
        for i in calo_monan:
            if i == monan:
                h= calo.iloc[j] #Cho h chạy ứng từng giá trị trong "Món ăn"
                print(h)
                soluong = int(input('Số lượng bạn đã dùng: '))
                print()
                tongcalo = tongcalo + soluong * calo['Calo'][j] #Tính tổng Calo đã dùng trong một ngày
            j += 1
        if monan == 'END.': break #Dừng tính toán
    return tongcalo

import pandas
Thongtin = ['Name', 'Age', 'Sex', 'Height', 'Weight', 'Frequency'] #List tiêu đề
User = NhapThongTin(Thongtin) #Lưu thông tin
BMI = ChisoBMI(User, Thongtin) #Tính chỉ số sức khỏe
TDEE = ChisoTDEE(User, Thongtin) #Tính chỉ số Calo
NhanXet(BMI) #Đưa ra tư vấn
print('Lượng calo cần bổ sung mỗi ngày của bạn là:', round(TDEE, 2), '\n')
TongCalo = TinhCaloMoiNgay(tongcalo=0) #Tính lượng Calo đã dùng
print('Tổng calo hôm nay của bạn là: ', TongCalo)
if TDEE > TongCalo: print('Bạn nên ăn nhiều hơn.') #So sánh xem đã dùng đủ Calo hay chưa
elif TDEE == TongCalo:
    print('Hãy duy trì chế độ ăn này nhé.')
else:
    print('Bạn nên giảm chế độ ăn của mình.')
print('Kết thúc ngày')





