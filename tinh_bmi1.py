# Nhập vào giá trị cân nặng, đơn vị kg
a = float(input("Nhập vào cân nặng tính theo đơn vị kg: "))

# Nhập vào giá trị chiều cao, đơn vị m
b = float(input("Nhập vào chiều cao tính theo đơn vị m: "))

# Tính chỉ số BMI
BMI = a/b**2

# Xếp loại dựa theo chỉ số BMI
if(BMI > 40):
    print("Béo phì cấp độ 3 rồi bạn tôi ơi")
elif(35 <= BMI <= 40):
    print("Béo phì cấp độ 2 rồi bạn tôi ơi")
elif(30 <= BMI < 35):
    print("Béo phì cấp độ 1 rồi bạn tôi ơi")
elif(25 <= BMI < 30):
    print("Thừa cân rồi bạn tôi ơi")
elif(18.5 <= BMI < 25):
    print("Bình thường nha bạn tôi ơi")
elif(17 <= BMI < 18.5):
    print("Gầy cấp độ 1 rồi bạn ạ")
elif(16 <= BMI < 17):
    print("Gầy cấp độ 2 rồi bạn ạ")
else:
    print("Gầy cấp độ 3 rồi bạn ạ")