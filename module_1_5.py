tuple_ = (1,2,[1,2],'a','b') #кортеж данных
print('Immutable tuple:',tuple_) # вывод двнных на экран
tuple_[2][1]=5 # замена в элементе 2, символа 1 на значение 5
print(tuple_) # вывод результата на экран
Mutable = [1,2,'a','b'] # список данных
print('Mutable list:',Mutable) # вывод данных
Mutable.append('Modified') # #добавление в конец списка
print(Mutable) # вывод результата на экран
