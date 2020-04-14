import calc_module


def execute(fun, *args):
    def wrapper(*args):
        print("your answer is:")
        print(fun(*args))
    return wrapper


while(1):
    print("operations available: \n 1.addition \n 2.subraction \n 3.multiplication \n 4.division")
    operations = {
        {1: "addition"},
        {2: "subraction"},
        {3: "multiplication"},
        {4: "division"}
    }
    user_math_choice = input("enter ur choice: ")
    input_1 = input("enter ur 1 input: ");
    input_2 = input("enter ur 2 input: ");
    operation_type = operations[user_math_choice];
    try:
        if(operation_type == "addition" or operation_type == "subraction"):
            user_input = tuple(map(int, input("enter the sequence: ").split()))
            if(operation_type == "addition"):
              math_operation = execute(calc_module.add)
            else:
              math_operation = execute(calc_module.add)
              user_input[1] = -(user_input[1])
            math_operation(user_input)

        elif(operation_type == "multiplication" or operation_type == "division"):
            user_input = tuple(map(int, input("enter the sequence: ").split()))
            if(operation_type == "multiplication"):
              math_operation = execute(calc_module.mul, user_input)
            else:
              math_operation = execute(calc_module.div, user_input)
            math_operation(user_input)
        else:
            print("enter the choice with in the range")

    except TypeError:
        print("use only numbers")
        if(int(input("0 to continue \n1 to stop: "))):
          break
    except :
      print ("Something went wrong");
