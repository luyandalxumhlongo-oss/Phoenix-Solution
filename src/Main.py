
import random

def render() :
    print("Hy I am Thuma Mina your friendly chat bot"
          "\n Description"
          )

    iD_no = input("\n Enter your ID number: ")

    while(True):

        if(iD_no):#if ID_no not in Database
            res2 = input("\n would you like to join?\n 1.Yes \n 2.No ")

            if (res2 == 2) :
                print("Okay Thank you")

            else:
                name = input("your name: ")
                surname = input("your surname: ")
                cell_num = input("enter your Cell phone number: ")
                user_name = name + iD_no[6:]
                person = user(user_name , name, surname, iD_no, cell_num )
                #database.addUser(person)
                choice = input("You have successfuly made your Thuma mina Account")
                continue
        else:
            # person = dataBase.getPerson(iD_no)
            choice1 = input("1.check balance 2.load credits 3.Send credits 4.view profile 5.help")
            match choice1:
                case 1:
                    person.check_Bal()
                case 2:
                    vou = input("enter voucher: ")
                    if (vou in person.vouchers):
                        person.num_credits += person.vouchers(vou)
                        person.vouchers.pop(vou)
                case 3:
                    while(True):
                        u_name = input("enter user name")
                        if u_name in data base:
                            amount = input("enter amount")
                            person.transfer(u_name,amount)
                            break
                        else:
                            print("invalid username")
                            continue
                case 4:
                    print(f"User Name :{person.user_name}"
                          f"\n Name : {person.name}"
                          f"\n ID Number : {person.iD_number}"     
                    )
                case 5:
                    print("For help contact : 10111")

class voucher:
    value
    status
    price

    def init(self, val,pri):
        self.value = val
        self.price = pri
        self.status = True


def make_Voucher(user_ID,amount): # voucher with first 4 digits = 4 unique ID digits,  last 3 digits = amount of voucher
        if(user_ID): # if user ID is in dataBase
            #person = database.find(user_ID)
            suf = f"{amount:03}" 
            mfix = ''.join(str(random.randint(0, 9)) for _ in range(7))
            prefix = person.iD_number[6:10]
            vo_num = prefix + mfix + suf
            vo = voucher(vo_num,False)
            person.vouchers.update({vo.value,amount})   # add eligible voucher to person's account
            return vo_num
        

class merchant:
    user_name
    name
    surname
    iD_number
    num_credits
    vouchers = {}
    transactions=[]

    def __init__(self, user_name="", name="", surname="", iD_number="", cell_number=""):
        self.user_name = user_name
        self.name= name
        self.surname= surname
        self.iD_number= iD_number
        self.num_credits = 0

    def check_Bal(self):
        print("Balance: "+self.num_credits)

    def transfer(username, amount):
        #vo = make_voucher(username,amount)
        #print(vo)


class Transaction :
    from_acc
    to_acc
    typee
    amount


    def init(from_acc,to_acc,typee,amount):
        self.from_acc=from_acc
        self.to_acc=to_acc
        self.typee=typee
        self.amount=amount

    def display_trans():
        print(f"Transaction type :{typee}"
              f"\nFrom :{from_acc}"
              f"\nTo :{to_acc}"
              )



class user:
    user_name
    name
    surname
    iD_number
    cell_number
    num_credits
    vouchers = {}
    transactions= []

    

    def __init__(self, user_name="", name="", surname="", iD_number="", cell_number=""):
        self.user_name = user_name
        self.name= name
        self.surname= surname
        self.iD_number= iD_number
        self.cell_number = cell_number
        self.num_credits = 0

    def transfer(to_Account,num_Credits):
       # to_person = data find to_Account
       # to_person.addCredits(num_Credits)
       # self.num_credits = self.num_credits - num_Credits

    def add_Credits(num_Credits):
        # self.num_credits += num_credits

    def check_Bal(self):
        print("Balance: "+self.num_credits)
