def all_sum(*args):
    for num in args:
        print(num)
total = all_sum(1,2,3,4,5,5,6,7)
print(total)


def Person(**kwargs):
      	for key, value in kwargs.items():
               	print(f'{key} : {value}')
Person(name='Snajit', roll='10028', age='27 ')