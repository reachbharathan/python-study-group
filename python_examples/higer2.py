def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)


def p_dummy(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

my_get_text = p_dummy(get_text)

print(my_get_text("John"))
