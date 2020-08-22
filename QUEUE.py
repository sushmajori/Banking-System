class Node(object):
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Queue(object):
    def __init__(self,front=None,rear=None):
        self.front=None
        self.rear=None

    def enqueue(self,data):
        NewNode=Node(data)
        
        if self.front==None and self.rear==None:
            self.front=self.rear=NewNode
            return
        self.rear.next=NewNode
        self.rear=NewNode

    def dequeue(self):
        current=self.front
        if self.front==None:
            print("\nQueue is Empty")
            return
        if self.front==self.rear:
            self.front=self.rear=None
            print("\nEntry Successfully Deleted")
        else:
            self.front=self.front.next
            print("\nEntry Successfully Deleted")

    def showelements(self):
        
        front1 = self.front
 
        if ((front1 == None) and (self.rear == None)):
        
            print("\nQueue is empty")
            return
        print("\nName of Depositor\t  Account Number\t Type of Account\t Balance\tDate")
    
        while (front1 != self.rear):
        
            print(front1.data[0],"\t",front1.data[1],"\t",front1.data[2],"\t\t",front1.data[3],\
            "\t\t",front1.data[4])
                
            front1 = front1.next
        
        if (front1 == self.rear):
            
            print(front1.data[0],"\t",front1.data[1],"\t",front1.data[2],"\t\t",front1.data[3],\
            "\t\t",front1.data[4])
            
    def empty(self):

        if ((self.front == None) and (self.rear == None)):
            print("\n Queue empty")
        else:
            print("\nQueue not empty")

    def size(self):
        front1 = self.front
        size=0
        if ((front1 == None) and (self.rear == None)):
        
            
            return(0)
        
        while (front1 != self.rear):
            size=size+1
            front1 = front1.next
        
        if (front1 == self.rear):

            size=size+1

        return(size)

    def displaybydate(self):
        date1=input("\nEnter Date :")
        while True:
            if len(date1)==10 and date1!=None: # VALIDTION OF INPUT
                date1 = date1
                break
                
            else:
                date1 = input("\nEnter valid DOB like dd/mm-yyyy or dd-mm-yyyy : ")
                continue          
        
            
        front1 = self.front
 
        if ((front1 == None) and (self.rear == None)):
        
            print("\nQueue is empty")
            return
        print("\nName of Depositor\t  Account Number\t Type of Account\t Balance\tDate")
        
        while (front1 != self.rear):
            if date1==front1.data[4]:
                print(front1.data[0],"\t",front1.data[1],"\t",front1.data[2],"\t\t",front1.data[3],\
                "\t\t",front1.data[4])
                
            front1 = front1.next
        
        if (front1 == self.rear):
            if date1==front1.data[4]:
                
                print(front1.data[0],"\t",front1.data[1],"\t",front1.data[2],"\t\t",front1.data[3],\
                "\t\t",front1.data[4])
            
    def linear(self,key):
        current=self.front
        while current is not None:
            if current.data[1]==key:
                return True
            current=current.next
        return False

            


while True:
    try:
        print("\n1.Create Queue")
        print("\n2.EnQueue")
        print("\n3.DeQueue")
        print("\n4.Display ")
        print("\n5.Size of Queue")
        print("\n6.Display by Date")
        print("\n7.Linear Search")
        print("\n8.Exit\n")
        ch=int(input())
        if ch==1:
            q=Queue()
        elif ch==2:
            Depositor_Name=input("\nEnter Name of Depositor : \n")
            while True:
                try:
                    if len(Depositor_Name)>4 and Depositor_Name!=None and type((Depositor_Name))==str:
                        Depositor_Name=Depositor_Name
                        break
                    else:
                        raise Exception("\nError Occured : Please Eneter Valid Depositor Name : \n")
                except Exception as e:
                    Depositor_Name=input(e)
                    continue
            
            Account_number=input("\nEnter Account Number : \n")
            while True:
                try:
                    if len(Account_number)==15 and Account_number!=None and type(int(Account_number))==int:
                        Account_number=Account_number
                        break
                    else:
                        raise Exception("\nError Occured : Please Eneter Valid 15 Digit Account Number : \n")
                except Exception as e:
                    Account_number=input(e)
                    continue
            
            Type_Account=input("\nEnter Type Of Account : \n")
            while True:
                try:
                    if (len(Type_Account)==6 or len(Type_Account)==7) and (Type_Account=="Saving" or Type_Account=="Current" ) and Type_Account!=None and type(Type_Account)==str:
                        Type_Account=Type_Account
                        break
                    else:
                        raise Exception("\nError Occured : Please Eneter Valid Account Type (Saving or Current) : \n")
                except Exception as e:
                    Type_Account=input(e)
                    continue
            Balance=int(input("\nEnter Balance : \n"))
            while True:
                try:
                    if (Balance)>=500 and Balance!=None and type((Balance))==int:
                        Balance=Balance
                        break
                    else:
                        raise Exception("\nError Occured : Please Eneter Valid Amount i.e. (>=500) : \n")
                except Exception as e:
                    Balance=input(e)    
                    if len(date1)==10 and date1!=None: # VALIDTION OF INPUT
                        date1 = date1
                        break
                        
                    else:
                        date1 = input("\nEnter valid DOB like dd/mm-yyyy or dd-mm-yyyy : ")
                        continue          
        
                    continue



            date1=input("\nEnter Date : \n")
            while True:
                if len(date1)==10 and date1!=None: # VALIDTION OF INPUT
                    date1 = date1
                    break
                    
                else:
                    date1 = input("\nEnter valid DOB like dd/mm-yyyy or dd-mm-yyyy : ")
                    continue          
            

            q.enqueue([Depositor_Name,Account_number,Type_Account,Balance,date1])

        elif ch==3:
            q.dequeue()

        elif ch==4:
            print("\nElements of Queue : ")
            q.showelements()
        elif ch==5:
            size=q.size()
            print("\nSize of Queue is ",size)
        elif ch==6:
            q.displaybydate()
        elif ch==8:
            break
        elif ch==7:
            print("\nEnter Account Number for Searching : ")
            Account_number=(input())
            
            while True:
                try:
                    if len(Account_number)==15 and Account_number!=None and type(int(Account_number))==int:
                        Account_number=Account_number
                        break
                    else:
                        raise Exception("\nError Occured : Please Eneter Valid 15 Digit Account Number : \n")
                except Exception as e:
                    Account_number=intput(e)
                    continue
            
            if q.linear(Account_number):
                print("\nEntry is found")
            else:
                print("\nEntry is not found")

        else:
            print("\nWrong Choice")

    except:
        continue


