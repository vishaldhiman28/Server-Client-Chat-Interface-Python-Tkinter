import socket
import time
import sys
from tkinter import *
from tkinter import messagebox


         
    
def s_t():

    try:
        st=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("\nSocket created succesfully")
    except socket.erro as err:
        print("Socket creation failed ( error: ",err," )")
    #print("\nEnter the server IP address (eg: 127.0.0.1):")
    IP_address=e1.get()
    #print("\nEnter the  Port Number:(8244)")
    Port=int(e2.get())
    #print("\nEnter your Name:")
    name=e3.get()
    print("\nConnecting.................to ",IP_address,"on Port",Port)
    #time.sleep(4)
    st.connect((IP_address,Port))
  
    print("\n..../// Successfully Connected. (for exit enter 'Abort')")
    


    def _recieve():
    
            recv_msg=st.recv(1048)
            recv_msg=recv_msg.decode()
            if recv_msg=="Abort":
                t=server_name+" went offline "
                list_msg.insert(END,t)
                list_msg.see(END)
                top.quit()
            t=server_name+" : "+recv_msg
            list_msg.insert(END,t)
            list_msg.see(END)
    
    def _send(event=None):
         
         msg=sent_msg.get()
         
         sent_msg.set("")
         
         m="ME : "+msg
         list_msg.insert(END,m)
         list_msg.see(END)
         if msg=="Abort":
             st.send(msg.encode())
             top.exit()
         st.send(msg.encode())
         #time.sleep(10)
         _recieve()
            
         

    top=Toplevel()
    msg_frame =Frame(top)
    sent_msg = StringVar()
    sent_msg.set("")
    scrollbar = Scrollbar(msg_frame)

    list_msg = Listbox(msg_frame, height=30, width=100, yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y") 
    list_msg.pack(side="left", fill="both")
    list_msg.pack() 
    msg_frame.pack()
    entry_field = Entry(top, textvariable=sent_msg)
    entry_field.bind("<Return>",_send)
    entry_field.pack()
    list_msg.insert(END,"....Welcome to the Chat Room.....")
    list_msg.see(END)   
    
    st.send(name.encode())
    server_name=st.recv(1048)
    server_name=server_name.decode()
    t="\n"+server_name+" is Online"
    list_msg.insert(END,t)
    list_msg.see(END)
     
    
    
    send_b = Button(top, text="Send",command=_send)
    send_b.pack()


    
  
def about():
    l="This is a simple one to one chat room"
    messagebox.showinfo("About",l)
def _exit():
    quit()

""" root """  
root=Tk()
root.title(".....Chat Room....")
root.geometry('400x400+250+50')

"""Menu"""
menu = Menu(root)
root.config(menu=menu)
subMenu=Menu(menu)
menu.add_cascade(label="Option",menu=subMenu)
subMenu.add_command(label="About",command=about)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=_exit)
"""Menu end """


l1=Label(text="Server IP",bg="Red",justify="left")
l2=Label(text="Port",bg="Red",justify="left")
l3=Label(text="Your Name",bg="Red",justify="left")


l1.grid(row=0,sticky="E")
l2.grid(row=1,sticky="E")
l3.grid(row=2,sticky="E")

e1=Entry()
e2=Entry()
e3=Entry()

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)

b1=Button(root,text='Start',command=s_t)
b1.grid(columnspan='3')



root.mainloop()


