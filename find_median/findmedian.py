



class FindMedian:
    def __init__(self):
        self.arr = []

    def add_num(self, data):
        self.arr.append(data)

    def print_data(self):
        # for i in self.arr:
        #     print(i)
        print(self.arr)

    def find_median(self):
        if self.is_even(len(self.arr)):
            median = (self.arr[len(self.arr)//2 ] + self.arr[len(self.arr)//2 - 1]) / 2 
        else:
            median = self.arr[len(self.arr) //2] 
    
        return median


    def is_even(self, data):
        return (data % 2 == 0)

fm = FindMedian()

fm.add_num(1)
fm.add_num(2)
print(fm.find_median())
fm.add_num(3)
print(fm.find_median())
fm.add_num(4)
fm.add_num(5)
fm.add_num(6)
fm.add_num(7)
print(fm.find_median())



fm.print_data()



# def is_even(data):
#     return (data % 2 == 0)

# print(is_even(1)) #False
# print(is_even(2)) #True
# print(is_even(3)) #False
# print(is_even(4)) #True
# print(is_even(5)) #False
# print(is_even(6)) #True
# print(is_even(32)) #True
# print(is_even(43)) #False


