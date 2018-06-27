class test(list):
    def update(self):
        self[:] = test(['a','b','c','d'])

x = test([1,2,3])
print(x)
x.update()
print(x)
print(type(x))