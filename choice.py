class Bank:
    acbal=10000
    def deposite(self):
        amount=int(input("enter your deposite amount"))
        if amount%100==0:
            if amount<=50000:
                self.acbal=self.acbal+amount
            else:
                print("Depositlimit is 50k only")
        else:
            print("Please enter multiples of 100 only")
        print("Avaliable bal is:",self.acbal)

        
    def validate(self):
        pin=1234
        print("WELCOME TO RKCE BANK")
        upin=int(input("enter your pin:"))


        if upin == pin:                                                                                                      
            print("1.Deposit")
            print("2.Withdraw")
            print("3.Bal enquiry")
            print("0.Exit")
            option=int(input("enter your choice"))
            if option==1:
                obj.deposite()
                obj.confirm()
            elif option==2:
                obj.withdraw()
                obj.confirm()
            else:
            print("Invalid pin")

            
obj=Bank()
obj.validate()
