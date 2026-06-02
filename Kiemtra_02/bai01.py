id = 100
employees = [

]
while True:
    print("===================================")
    print("  QUẢN LÝ NHÂN SỰ - STAFF MANAGER ")
    print("===================================")
    print("1. Thêm nhân viên mới")
    print("2. Danh sách nhân viên")
    print("3. Tìm kiếm nhân viên (Theo mã)")
    print("4. Xóa nhân viên khỏi hệ thống")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn: ")
    if choice != "1" and choice != "2" and choice != "3" and choice != '4' and choice != "5":
        print("Lựa chọn không hợp lệ ! Vui lòng chọn lại.")
    elif choice == "1":
        input_name = input("Nhập tên nhân viên: ").strip()
        id += 1
        while True:
                input_salary = float(input("Nhập lương của nhân viên: ")) 
                if input_salary <= 0:
                    print("Không hợp lệ ! Vui lòng nhập lại.")
                else:
                    new_employ = {'id':id,
                        'name': input_name,
                        'salary': input_salary,
                        }    
                employees.append(new_employ)
                print(f"Thêm nhân viên thành công! ID:{id}")
                break
    elif choice == "2":
        print("-----DANH SÁCH NHÂN VIÊN-----")
        print("ID      | TÊN NHÂN VIÊN         | MỨC LƯƠNG")
        if not employees:
            print("Danh sách trống!")
        else:
            for employee in employees:
                print(f"{employee['id']} | {employee['name']} | {employee['salary']}")

    elif choice == "3":
        search_id = int(input("Nhập ID nhân viên cần tìm: "))
        found = False
        for employee in employees:
            if employee["id"] == search_id:
                print("Thông tin nhân viên:")
                print(employee)
                found = True
                break
        if not found:
                print(f"Không tìm thấy nhân viên có ID {search_id}!")  

    elif choice == 5:
        print("Đã thoát chương trình !")

    


                            



       



