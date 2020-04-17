class MyClassRoom:
	"MyClassRoom has many students"
	a =50
	def func(self):
		print('Hello')
        
ob = MyClassRoom()
print(MyClassRoom.func)
print(ob.func)
ob.func()