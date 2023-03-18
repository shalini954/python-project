from tkinter import *
from tkinter import ttk
class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title('Library Management System')
        self.root.geometry("1550x800+0+0")


        lbltitle = Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

        #===========================DataFramesLeft===========================================================

        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember = ttk.Combobox(DataFrameLeft,font=("times new roman",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,font=("arial",12,"bold"),text="PRN Number",padx=2,bg="powder blue")
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("arial",13,"bold"),width=27)
        txtPRN_No.grid(row=1,column=1)

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        #===========================Button Frames===========================================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        #===========================Information Frames===========================================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1530,height=195)


 



if __name__=="__main__":
    root = Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
