import socket
import time
import sys
from tkinter import *
from tkinter import messagebox



"""
host_name=st.gethostname()
IP_address=st.gethostbyname()
"""

         
    
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
    
    st.bind((IP_address,Port))

    st.listen(1)

    
    print("\n...Waiting for client................ ",)
    client,addr_list=st.accept()
  
    
    print("\n   Client connection IP: ",addr_list[0],"on Port ",addr_list[1])

    print("\n..../// Successfully Connected. (for exit enter 'Abort')")
     
    print("\n ",name,"  ....Welcome to the Chat Room..... ")
   
    
    

    def _recieve():
        

            recv_msg=client.recv(1048)
            recv_msg=recv_msg.decode()
            if recv_msg=="Abort":
                t=client_name+" went offline "
                list_msg.insert(END,t)
                list_msg.see(END)
                top.quit()
                
            t=client_name+" : "+recv_msg
            list_msg.insert(END,t)
            list_msg.see(END)
        
    def _send(event=None):
            
            
            msg=sent_msg.get()
            sent_msg.set("")
            m="ME : "+msg
            list_msg.insert(END,m)
            list_msg.see(END)
            if msg=="Abort":
                client.send(msg.encode())
                top.exit()
            
            client.send(msg.encode())
            time.sleep(10)
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
    entry_field.bind("<Return>", _send)
    entry_field.pack()
    list_msg.insert(END,"....Welcome to the Chat Room.....")
    list_msg.see(END)
    client_name=client.recv(1048)
    client_name=client_name.decode()
    print("\n",client_name," is Online")

    client.send(name.encode()) 
     
    t="\n"+client_name+" is Online"
    list_msg.insert(END,t)
    list_msg.see(END)
    
    send_b = Button(top, text="Send",command=_send)
    send_b.pack() 

    _recieve()

def about():
    l="This is a simple one to one chat room"
    messagebox.showinfo("About",l)
def _exit():
    quit()

""" root """  
root=Tk()
root.title(".....Chat Room..Server")
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
