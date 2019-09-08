import random

control_main = True
while control_main == True:
    print('''
     _________________________________
    |                                 |
    |               MATHLAB           |  
    |_________________________________|
    ''')
    print(" Chúng tôi có 3 chế độ chơi như sau:")
    print('''
         ____________________________________________________________________
        |       Chế độ 1: TOÁN HỌC THẬT DỄ
        |       Chế độ 2: MÁY TÍNH HỖ TRỢ TÍNH TOÁN
        |       Chế độ 3:
        |----------------------
        |   Nhấn phím 1,2,3 để chọn chế độ 1,2,3. Nhấn phím 0 để thoát game.
        |____________________________________________________________________
    ''')
    option = str(input("Chế độ chơi mà bạn chọn: "))

# __________Chế độ chơi thứ nhất__________    

    if option == "1" :
        print('''
         _______________________________________________________ 
        |                                                       | 
        |                   TOÁN HỌC THẬT DỄ.                   |
        |_______________________________________________________|
        ''')
        print(" Có tất cả 10 câu hỏi với mỗi level và sẽ có 3 level.  ")
        point = 0
        while point <=5:
            print("PHẦN 1: CÂU HỎI DỄ (hãy trả lời đúng 5/10 câu để vượt qua) ")
# Câu hỏi 1 : câu hỏi về toán học: phép cộng
            print(" Câu 1: hãy điền số còn thiểu để hoàn thành dãy: ")
            a = random.randint(0,100)
            b = random.randint(0,100)
            c = a+b
            print("Ta có: ", a , "+", " ___  = ", c)
            answer_q1=int(input("Đáp án của bạn là: "))
            if answer_q1 == b:
                print('___Chúc mừng, bạn đã đúng___')
                point+=1
            else:
                print("SAI RỒI!!!")
# Câu 2: Câu hỏi về toán học
# Câu 3:
# Câu 4:
# Câu 5:
# Câu 6:
# Câu 7:
# Câu 8:
# Câu 9:
# Câu 10:
# Control: 
            print(f'Chúc mừng bạn đã hoàn thành các câu hỏi, tổng điểm của bạn là  {point}' )
            if point <=4:
                control_o1_lv1= str(input("Bạn đã không vượt qua bài kiểm tra level 1. Nhập REDO để làm lại,CHANGE để đổi chế độ chơi hoặc QUIT để thoát "))
                if control_o1_lv1.upper()  == "QUIT":
                    print(" Bạn sẽ thoát chương trình này!")
                    decision_1=str(input("Bạn có chắc chắn thoát chương trình không: [yes] or [no]"))
                    if decision_1.lower() =="yes":
                        point=6     
                        option=0
                        control_main=False
                    else: 
                        print("Bạn đã từ chối thoát.")
                        print("Bạn sẽ được đưa đến màn hình chính")
                        point = 6
                        option = 0
                elif control_o1_lv1.upper() == "CHANGE":
                    print("___Bạn đã chọn đổi chế độ chơi___")
                    point = 6
                    option = 0
                else: 
                    print("Bạn đã chọn làm lại!")
                    point = 0
            else:
                print("Bạn đã được lên Level 2")
                
                    
    elif option == "2" :
        print("Chào mừng bạn đến với chế độ chơi 2: ")
    elif option == "3" :
        print("Chào mừng bạn đến với chế độ chơi 3:")
    elif option == "0" :
        control_main = False
    else :
        print(" Sai cú pháp, Mời bạn nhập lại chế độ chơi.")