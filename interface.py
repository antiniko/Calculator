from tabulate import tabulate
# table = [["4",5,6],["7",8,9],[" ",0,"."]]
# headers = ["1", "2", "3"]
# print(tabulate(table, headers, tablefmt="grid"))

# table = [["+", "сложение"],["-","вычитание"],["*","умножение"],["/","деление"], ["**","возведение в степень"],[".","для рациональных чисел"]]
# headers = ["символ", "функция"]
# print(tabulate(table, headers, tablefmt="grid"))

test_table1 = str(tabulate([[1, 2, 3], [4, 5, 6], [7, 8, 9], [" ", 0, "."]])).splitlines()
test_table2 = str(tabulate([["+", "сложение"],["-","вычитание"],["*","умножение"],["/","деление"], ["**","возведение в степень"],[".","для рациональных чисел"]])).splitlines()
master_headers = ["символы", "функции"]
master_table = tabulate([list(item) for item in zip(test_table1,test_table2)],
                        master_headers, tablefmt="grid")
print(master_table)