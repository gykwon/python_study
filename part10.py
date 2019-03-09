my_list = list()
idx = 0
def print_element(arg, index):
    print("{0}번째 데이터가 추출 됩니다.".format(idx))
    print(arg.pop(int(idx)-1))





print("몇개의 숫자를 입력하시겠어요??")
num = input()

print("Enter로 구분하여 숫자를 입력하세요")

for i in range(int(num)):
    input_num = input()
    my_list.append(int(input_num))


print("입력한 데이터는 {0} 입니다.".format(my_list))
print("몇번째 데이터를 추출할까요??")
idx = input()

print_element(my_list,idx)
