my_list = list()
idx = int()
num = int()
def print_element(arg, index):
    print(arg.pop(int(idx)-1))



try:
    print("몇개의 숫자를 입력하시겠어요??")
    num = input()
    int(num)

    print("Enter로 구분하여 숫자를 입력하세요")

    for i in range(int(num)):
        input_num = input()
        my_list.append(int(input_num))


    print("입력한 데이터는 {0} 입니다.".format(my_list))
    print("몇번째 데이터를 추출할까요??")
    idx = input()

    print_element(my_list,idx)



except ValueError:
    print("Error : 숫자를 입력하세요")


except IndexError:
    print("index를 초과 하였습니다.")
