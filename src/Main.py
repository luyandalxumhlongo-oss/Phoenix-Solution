import random

class DataBase:
    users={}
    def _init_(self):
        self.users = {}

    def add_user(self, person):
        self.users[person.iD_number] = person

    def get_user(self, iD_number):
        return self.users.get(iD_number)

database = DataBase()



def render() :
    print("Hy I am Thuma Mina your friendly chat bot"
          "\n Description"
          )

    

    while(True):
        iD_no = input("\n Enter your ID number: ").strip()

        if database.users:
            person = database.get_user(iD_no)

        if not database.get_user(iD_no): #ID_no not in Database
            res2 = input("\n would you like to join?\n 1.Yes \n 2.No ").strip()

            if (res2 == "2") :
                print("Okay Thank you")
                continue

            else:
                name = input("your name: ").strip()
                surname = input("your surname: ").strip()
                cell_num = input("enter your Cell phone number: ").strip()
                user_name = name + iD_no[6:]
                person = user(user_name , name, surname, iD_no, cell_num )
                database.add_user(person)
                print("You have successfuly made your Thuma mina Account")
                continue

        while(True):
            choice = input(
                "\n1.Check balance  2.Load credits  3.Send credits "
                "4.View profile   5.Help   6.Log out\nChoose: "
            ).strip()

            if choice == "1":
                person.check_Bal()

            elif choice == "2":
                vou = input("Enter voucher number: ").strip()
                if vou in person.vouchers:
                    person.add_credits(person.vouchers[vou])
                    person.vouchers.pop(vou)
                    print("Voucher loaded.")
                else:
                    print("Invalid voucher.")

            elif choice == "3":
                u_name = input("Enter recipient username: ").strip()
                amt = int(input("Enter amount: "))
                person.transfer(u_name, amt)

            elif choice == "4":
                print(f"User Name : {person.user_name}"
                      f"\nName      : {person.name}"
                      f"\nID Number : {person.iD_number}")

            elif choice == "5":
                print("For help contact: 10111")

            elif choice == "6":
                print("Logging out...")
                break

            else:
                print("Invalid choice.")
           

class voucher:
    def __init__(self, val,pri):
        self.value = val
        self.price = pri
        self.status = True

'''def make_Voucher(user_ID,amount): # voucher with first 4 digits = 4 unique ID digits,  last 3 digits = amount of voucher
        if(user_ID): # if user ID is in dataBase
            #person = database.find(user_ID)
            suf = f"{amount:03}" 
            mfix = ''.join(str(random.randint(0, 9)) for _ in range(7))
            prefix = person.iD_number[6:10]
            vo_num = prefix + mfix + suf
            vo = voucher(vo_num,False)
            person.vouchers.update({vo.value,amount})   # add eligible voucher to person's account
            return vo_num '''

def make_voucher(person, amount):
    suf = f"{amount:03}"
    mfix = ''.join(str(random.randint(0, 9)) for _ in range(7))
    prefix = person.iD_number[6:9]
    vo_num = prefix + mfix + suf
    person.vouchers[vo_num] = amount
    return vo_num            

class merchant:
    def __init__(self, user_name="", name="", surname="", iD_number="", cell_number=""):
        self.user_name = user_name
        self.name= name
        self.surname= surname
        self.iD_number= iD_number
        self.num_credits = 0

    def check_Bal(self):
        print("Balance: "+self.num_credits)

    def transfer(username, amount):
        vo = make_voucher(username,amount)
        print(vo)


class Transaction :
    def __init__(self,from_acc,to_acc,typee,amount):
        self.from_acc=from_acc
        self.to_acc=to_acc
        self.typee=typee
        self.amount=amount

    def display_trans(self):
        print(f"Transaction type :{self.typee}"
              f"\nFrom :{self.from_acc}"
              f"\nTo :{self.to_acc}"
              f"\nAmount :{self.amount}"
              )



class user:
    def __init__(self, user_name="", name="", surname="", iD_number="", cell_number=""):
        self.user_name = user_name
        self.name= name
        self.surname= surname
        self.iD_number= iD_number
        self.cell_number = cell_number
        self.num_credits = 20
        self.vouchers = {}
        self.transactions = []


    def transfer(self,to_username,amount):
       # to_person = data find to_Account
       # to_person.addCredits(num_Credits)
       # self.num_credits = self.num_credits - num_Credits
       for u in database.users.values():
            if u.user_name == to_username:
                if self.num_credits >= amount:
                    self.num_credits -= amount
                    u.num_credits += amount
                    t = Transaction(self.user_name, to_username, "Transfer", amount)
                    self.transactions.append(t)
                    u.transactions.append(t)
                    print("Transfer complete.")
                else:
                    print("Not enough credits.")
                return
            print("Recipient not found.")

    def add_Credits(self,num_Credits):
        self.num_credits += num_Credits

    def check_Bal(self):
        print("Balance: ",self.num_credits)


render()

