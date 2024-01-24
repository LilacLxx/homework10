num = int(input("กรุณาป้อนตัวเลข: "))

print(f"ตารางแม่สูตรคูณของ {num} คือ:")
for i in range(1, 13):
    result = num * i
    print(f"{num} x {i} = {result}")
