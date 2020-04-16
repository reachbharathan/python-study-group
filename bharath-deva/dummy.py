def Sumofthenumber(Num):
        #Num = self.num
        sum =0
        while (Num>0):
            remainder = Num%10
            sum = sum+int(remainder)
            Num = Num/10
        return sum