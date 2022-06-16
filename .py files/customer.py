from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class customerClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Chemical Manufacturing System")
        self.root.config(bg="white")
        self.root.focus_force()
        #======
        #=ALL VARIABLES=====
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        
        self.var_c_id=StringVar()
        self.var_contact=StringVar()
        self.var_customer_name=StringVar()
        
        
        #======SEARCH GFRAME======
        SearchFrame=LabelFrame(self.root,text="Search Customer",bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)
        
        #======options====
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state="readonly",justify=CENTER,font=("goudy old style ",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
         
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)
        
        #=======title======

        title=Label(self.root,text="Customer Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)              
                          
        #=====content=====
        
        #===row1======
        lbl_cid=Label(self.root,text="Customer ID",font=("goudy old style",15),bg="white").place(x=40,y=150)              
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=250)              
        txt_cid=Entry(self.root,textvariable=self.var_c_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)              
        
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=150,y=250,width=180)              
         
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=200)              

        txt_name=Entry(self.root,textvariable=self.var_customer_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=200,width=180)              
        lbl_Product=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=200)              

 
    #====button======
        btn_add=Button(self.root,text="Save",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=30,y=405,width=110,height=28)
        btn_update=Button(self.root,text="Update",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=150,y=405,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=270,y=405,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=400,y=405,width=110,height=28)
    
    # =====Employee  Detail=======
        customer_frame=Frame(self.root,bd=3,relief=RIDGE)
        customer_frame.place(x=550,y=130,width=500,height=350)
        
    
        scrolly=Scrollbar(customer_frame,orient=VERTICAL)
        scrollx=Scrollbar(customer_frame,orient=HORIZONTAL)
        
        self.CustomerTable=ttk.Treeview(customer_frame,columns=("Cid","name",'contact',"product","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CustomerTable.xview)
        scrolly.config(command=self.CustomerTable.yview)

        self.CustomerTable.heading("Cid",text="C ID")
        self.CustomerTable.heading("name",text="Name")
        self.CustomerTable.heading("contact",text="Contact")
        self.CustomerTable.heading("product",text="Product")
        self.CustomerTable.heading("price",text="Price")
        self.CustomerTable.heading("qty",text="Quantity")

        
        self.CustomerTable["show"]="headings"
        
        self.CustomerTable.column("Cid",width=90)
        self.CustomerTable.column("name",width=100)
        self.CustomerTable.column("contact",width=100)
        self.CustomerTable.column("product",width=100)
        self.CustomerTable.column("price",width=100)
        self.CustomerTable.column("qty",width=100)
        
        self.CustomerTable.pack(fill=BOTH,expand=1)
        
        # self.CustomerTable.bind("<ButtonRelease-1>",self.get_data)
        # self.show() 
#   # add  
#     def add(self):
#         con=sqlite3.connect(database=r'CMS.db')
#         cur=con.cursor()
#         try:
#             if self.var_c_id.get()=="":
#                 messagebox.showerror("Error","Customer ID Must be required",parent=self.root)
#             else:
#                 cur.execute("Select * from customer where Cid=?",(self.var_c_id.get(),))
#                 row=cur.fetchone()
#                 if row!=None:
#                     messagebox.showerror("Error", "This Customer ID already assigned, try different",parent=self.root)
#                 else:
#                     cur.execute("Insert into customer (Cid,name,contact,) values(?,?,?,?,?,?,?,?,?)",(
#                                     self.var_c_id.get(),
#                                     self.var_customer_name.get(),
#                                     self.var_email.get(),
#                                     self.var_gender.get(),
#                                     self.var_contact.get(),
                                    
#                                     self.var_dob.get(),
#                                     self.var_doj.get(),
                                    
#                                     self.var_utype.get(),
#                                     self.txt_address.get('1.0',END),
                        
                        
#                     ))
#                     con.commit()
#                     messagebox.showinfo('Success','Customer Added Successfully',parent=self.root)

#                     self.show()  #show function
#         except Exception as ex:
#             messagebox.showerror("Error",f'Error due to : {str(ex)}',parent=self.root)

# #==================================================================================
# # fetching data 

#     def show(self):
#         con=sqlite3.connect(database=r'CMS.db')
#         cur=con.cursor()
#         try:
#             cur.execute("Select * from customer")
#             rows=cur.fetchall()
#             self.CustomerTable.delete(*self.CustomerTable.get_children())
#             for row in rows:
#                 self.CustomerTable.insert('',END,values=row)
                                
#         except Exception as ex:
#             messagebox.showerror("Error",f'Error due to : {str(ex)}',parent=self.root)

# #================getting==========
#     def get_data(self,ev):
#         f=self.CustomerTable.focus()
#         content=(self.CustomerTable.item(f))
#         row=content['values']
#         self.var_c_id.set(row[0])
#         self.var_customer_name.set(row[1])
#         self.var_contact.set(row[4])
        
        
#         self.txt_address.delete('1.0',END)
#         self.txt_address.insert(END,row[8])



# #============update=================
   
#     def update(self):
#         con=sqlite3.connect(database=r'CMS.db')
#         cur=con.cursor()
#         try:
#             if self.var_c_id.get()=="":
#                 messagebox.showerror("Error","Customer ID Must be required",parent=self.root)
#             else:
#                 cur.execute("Select * from customer where Cid=?",(self.var_c_id.get(),))
#                 row=cur.fetchone()
#                 if row==None:
#                     messagebox.showerror("Error", "Invalid Customer ID",parent=self.root)
#                 else:
#                     cur.execute("Update customer set name=?,email=?,gender=?,contact=?,dob=?,doj=?,utype=?,address=? where Cid=?",(
#                                     self.var_customer_name.get(),
#                                     self.var_email.get(),
#                                     self.var_gender.get(),
#                                     self.var_contact.get(),
                                    
#                                     self.var_dob.get(),
#                                     self.var_doj.get(),
                                    
#                                     self.var_utype.get(),
#                                     self.txt_address.get('1.0',END),
#                                     self.var_c_id.get(),

                        
#                     ))
#                     con.commit()
#                     messagebox.showinfo('Success','Updated Successfully',parent=self.root)

#                     self.show()  #show function
#         except Exception as ex:
#             messagebox.showerror("Error",f'Error due to : {str(ex)}',parent=self.root)

# #================delete==============
#     def delete(self):
#         con=sqlite3.connect(database=r'CMS.db')
#         cur=con.cursor()
#         try:
#             if self.var_c_id.get()=="":
#                 messagebox.showerror("Error","Customer ID Must be required",parent=self.root)
#             else:
#                 cur.execute("Select * from customer where Cid=?",(self.var_c_id.get(),))
#                 row=cur.fetchone()
#                 if row==None:
#                     messagebox.showerror("Error", "Invalid Customer ID",parent=self.root)
#                 else:
#                     op=messagebox.askyesno("Confirm","Do you really want to delete?",parent= self.root)
#                     if op==True:
#                         cur.execute("delete from customer where Cid=?",(self.var_c_id.get(),))
#                         con.commit()
#                         messagebox.showinfo("Delete","Customer Delete Successfully",parent=self.root)
#                         self.clear()
                        
                                        
#         except Exception as ex:
#             messagebox.showerror("Error",f'Error due to : {str(ex)}',parent=self.root)
            
# #==============CLEAR===================

#     def clear(self):      
#         self.var_c_id.set("")
#         self.var_customer_name.set("")
#         self.var_email.set("")
#         self.var_gender.set("")
#         self.var_contact.set("")
        
#         self.var_dob.set("")
#         self.var_doj.set("")
        
#         self.var_utype.set("Regular")
#         self.txt_address.delete("1.0",END)
        
#         self.var_searchtxt.set("")
#         self.var_searchby.set("Select")
        
#         self.show()
        
        
# #===================SEARCH====================
#     def search(self):
#         con=sqlite3.connect(database=r'CMS.db')
#         cur=con.cursor()
#         try:
#             if self.var_searchby.get()=="Select":
#                 messagebox.showerror("Error","Select Search by option",parent=self.root)
#             elif self.var_searchtxt.get()=="":
#                 messagebox.showerror("Error","Select input should be required",parent=self.root)
                
#             else:
    
#                 cur.execute("Select * from customer where "+ self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
#                 rows=cur.fetchall()
#                 if len(rows)!=0:
                    
#                     self.CustomerTable.delete(*self.CustomerTable.get_children())
#                     for row in rows:
#                         self.CustomerTable.insert('',END,values=row)
#                 else:
#                     messagebox.showerror("Error","No record found!!",parent=self.root)
                                
#         except Exception as ex:
#             messagebox.showerror("Error",f'Error due to : {str(ex)}',parent=self.root)

        
# #=====================================================================================


        
        
        
if __name__=="__main__":         
    root=Tk() 
    obj=customerClass(root)
    root.mainloop()