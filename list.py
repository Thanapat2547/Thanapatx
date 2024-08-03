#  Letters = ("A", "B", "C", "D",)   
#  A = Letters [0]
#  D = Letters [3]
#  Letters[0] = D
#  Letters[3] = A
# print(Letters[0:4])


# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)
# numbers.remove(5)
# numbers.insert(0, -1)

# print(numbers)

fruits = ['มะนาว', 'มะม่วง', 'ลำใย', 'ส้ม', 'แก้วมังกร']

fruits.insert(3, 'มะเขือเทศ')
fruits.insert(0, 'shinchan') 
fruits.remove('มะม่วง')
fruits.insert(2, 'ultraman')

ultraman = fruits [2]
ลำใย = fruits [4]
fruits[2] = ลำใย
fruits[4] = ultraman

print(fruits)

