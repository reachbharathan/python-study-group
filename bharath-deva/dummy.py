def Sumofthenumber(Num):
        #Num = self.num
    try:
        int(Num)
        sum =0
        while (Num>0):
            remainder = Num%10
            sum = sum+int(remainder)
            Num = Num/10
        return sum
    except ValueError as err:
        print("Error value")
        print(type(err))
        print(err)
        return err
