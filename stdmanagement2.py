import customtkinter
import tkinter
import customtkinter as Ctk
from tkinter import*
from tkinter import ttk
from tkcalendar import DateEntry
from customtkinter import CTkTextbox
from tkinter import filedialog
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

def openImageFile():
    global img, photo
    imPath = filedialog.askopenfilename(initialdir="C:\\", title = "Open an image", filetypes = (("PNG file","*.png"), ("JPEG File","*.jpeg"), ("JPG File","*.jpg"), ("All File Types","*.*")))
    if imPath:
        img=ImageTk.PhotoImage(Image.open(imPath).resize((250, 250), Image.ANTIALIAS))



 


class Student():
    def __init__(std,root):
        std.root=root
        std.root.title("DHEMAJI ENGINEERING COLLEGE")
        std.root.iconbitmap("icon.ico")
        std.root.geometry("1200x900+0+0")
        n_rows = 3
        n_columns = 1
        for i in range(n_rows): root.grid_rowconfigure(i, weight=1) 
        for i in range(n_columns): root.grid_columnconfigure(i, weight=1)                 
       
       
        
        
        frame1 = customtkinter.CTkFrame(master=root, width=1200, height=32)
        frame1.grid_rowconfigure(0, weight=1)
        frame1.grid_columnconfigure(0, weight=1)
        frame1.grid(row=0, column=0, sticky="nsew")

        frame2 = customtkinter.CTkFrame(master=root, width=1200, height=350)
        frame2.grid_rowconfigure(1, weight=1)
        frame2.grid_columnconfigure(0, weight=1)
        frame2.grid(row=1, column=0, sticky="nsew")

        frame3 = customtkinter.CTkFrame(master=root, width=1200, height=400, bg_color="green")
        frame3.grid_rowconfigure(2, weight=1)
        frame3.grid_columnconfigure(0, weight=1)
        frame3.grid(row=2, column=0, sticky="nsew")
        
        
        
        
       
        label = customtkinter.CTkLabel(master=frame1,width=500,  text="___________________________________STUDENT MANAGEMENT SYSTEM_____________________________________", font= ("Times New Roman", 30, 'bold',UNDERLINE))
        label.place(relx=0.5,rely=0.4, anchor = "center")
        
        
                                       #######################################  FRAME 2 ##########################################
        
        title_label = customtkinter.CTkLabel(master=frame2, text="________________________________________________Personal Information_______________________________________________________", font= ("Times New Roman", 25, 'bold', UNDERLINE))
        title_label.place(relx=0.5,rely=0.04, anchor = "center")
        
        labelname = customtkinter.CTkLabel(master=frame2,text="Name:", font= ("Times New Roman", 20))
        labelname.place(relx=0.01, rely=0.28)
        entryname= customtkinter.CTkEntry(master=frame2,width=180, placeholder_text="Student Name")
        entryname.place(relx=0.11, rely=0.28)
        
        labelFname = customtkinter.CTkLabel(master=frame2,text="Father's Name:", font= ("Times New Roman", 20))
        labelFname.place(relx=0.35, rely=0.28)
        entryFname= customtkinter.CTkEntry(master=frame2,width=180, placeholder_text="Father's Name")
        entryFname.place(relx=0.48, rely=0.28)
        
        labelmname = customtkinter.CTkLabel(master=frame2,text="Mother's Name:", font= ("Times New Roman", 20))
        labelmname.place(relx=0.7, rely=0.28)
        entrymname= customtkinter.CTkEntry(master=frame2,width=180, placeholder_text="Mother's Name")
        entrymname.place(relx=0.82, rely=0.28)
        
        labelroll = customtkinter.CTkLabel(master=frame2, text="Student id:", font= ("Times New Roman", 20))
        labelroll.place(relx=0.01, rely=0.48)
        entryroll = customtkinter.CTkEntry(master=frame2,width=180, placeholder_text="ASTU Roll no")
        entryroll.place(relx=0.11, rely= 0.48)
        
        labelbranch = customtkinter.CTkLabel(master=frame2,text="Stream:", font= ("Times New Roman", 20))
        labelbranch.place(relx=0.35, rely=0.48)
        entrybranch = customtkinter.CTkOptionMenu(master=frame2, width=180,values= ("","COMPUTER SCIENCE", "MECHANICAL", "CIVIL"))
        entrybranch.place(relx=0.48, rely=0.48)
        
         
        labelbranch = customtkinter.CTkLabel(master=frame2,text="Batch:", font= ("Times New Roman", 20))
        labelbranch.place(relx=0.70, rely=0.48)
        entrybranch = customtkinter.CTkOptionMenu(master=frame2, width=180,values= ("","2020-2024", "2021-2025", "2022-2026"))
        entrybranch.place(relx=0.82, rely=0.48)
        
        labelcat = customtkinter.CTkLabel(master=frame2,text="Category:", font= ("Times New Roman", 20))
        labelcat.place(relx=0.70, rely=0.70)
        entrycat =  customtkinter.CTkOptionMenu(master=frame2, width=180, values= ("","General", "OBC", "MOBC","SC", "ST","ST Hills","Others"))
        entrycat.place(relx=0.82, rely=0.70)
        
        
        labeldob = customtkinter.CTkLabel(master=frame2,text="Date of Birth:", font= ("Times New Roman", 19))
        labeldob.place(relx=0.01, rely=0.70)
        entrydob = DateEntry(frame2, font=("Arial", 13), width=16)
        entrydob.place(relx=0.11, rely= 0.70)
        
        
        labelbranch = customtkinter.CTkLabel(master=frame2,text="Registration no.:", font= ("Times New Roman", 20))
        labelbranch.place(relx=0.35, rely=0.70)
        entrybranch = customtkinter.CTkEntry(master=frame2,width=180,placeholder_text="2xxxxxxx")
        entrybranch.place(relx=0.48, rely=0.70)
        title_endlabel = customtkinter.CTkLabel(master=frame2, text="_______________________________________________________________________________________________________________________________________________________", font= ("Times New Roman", 25, 'bold',UNDERLINE))
        title_endlabel.place(relx=0,rely=0.90)
        
       
        
        
        
                                               #######################################  FRAME 3 ##########################################
    
        title_label = customtkinter.CTkLabel(master=frame3, text="________________________________________________Contact Information_______________________________________________________", font= ("Times New Roman", 25, 'bold',UNDERLINE))
        title_label.place(relx=0.5,rely=0.04, anchor = "center")
        
        labelphone = customtkinter.CTkLabel(master=frame3,text="Contact no:", font= ("Times New Roman", 20))
        labelphone.place(relx=0.35, rely=0.2)
        entryphone = customtkinter.CTkEntry(master=frame3,width=180, placeholder_text="+91XXXXXXXXXX")
        entryphone.place(relx=0.48, rely= 0.2)
        
        labelwp = customtkinter.CTkLabel(master=frame3,text="WhatsApp:", font= ("Times New Roman", 19))
        labelwp.place(relx=0.7, rely=0.2)
        entrywp = customtkinter.CTkEntry(master=frame3, width=180,placeholder_text="+91XXXXXXXXXX")
        entrywp.place(relx=0.82, rely=0.2)
        
        labelemail = customtkinter.CTkLabel(master=frame3,text="Email:", font= ("Times New Roman", 20))
        labelemail.place(relx=0.01, rely=0.2)
        entryemail = customtkinter.CTkEntry(master=frame3,width=250, placeholder_text="fftr@xyzmail.com")
        entryemail.place(relx=0.1, rely= 0.2)
        
        labeladdres1 = customtkinter.CTkLabel(master=frame3,text="Permanent", font= ("Times New Roman", 20))
        labeladdres1.place(relx=0.01, rely=0.37)
        labeladdress = customtkinter.CTkLabel(master=frame3,text="Address:", font= ("Times New Roman", 20))
        labeladdress.place(relx=0.01, rely=0.44)
        entryaddress = CTkTextbox(master=frame3, width=250, height=70, wrap='word', font=("Arial", 15))
        entryaddress.place(relx=0.1, rely= 0.34)
        
        labelpin = customtkinter.CTkLabel(master=frame3,text="PIN Code:", font= ("Times New Roman", 20))
        labelpin.place(relx=0.35, rely=0.39)
        entrypin = customtkinter.CTkEntry(master=frame3,width=180, placeholder_text="Postal Code")
        entrypin.place(relx=0.48, rely=0.39)
        
        labeldis = customtkinter.CTkLabel(master=frame3,text="District:", font= ("Times New Roman", 20))
        labeldis.place(relx=0.70, rely=0.39)
        entrydis = customtkinter.CTkEntry(master=frame3, width=180)
        entrydis.place(relx=0.82, rely=0.39)
        
        labellocaladdress = customtkinter.CTkLabel(master=frame3,text="Present", font= ("Times New Roman", 20))
        labellocaladdress.place(relx=0.01, rely=0.58)
        labellocaladdress = customtkinter.CTkLabel(master=frame3,text="Address:", font= ("Times New Roman", 20))
        labellocaladdress.place(relx=0.01, rely=0.65)
        entrylocaladdress = CTkTextbox(master=frame3, width=250, height=70, wrap='word', font=("Arial", 15))
        entrylocaladdress.place(relx=0.1, rely= 0.57)
        
        labellgaurd = customtkinter.CTkLabel(master=frame3,text="Local Guardian:", font= ("Times New Roman", 19))
        labellgaurd.place(relx=0.35, rely=0.60)
        entrylgaurd = customtkinter.CTkEntry(master=frame3,width=180, placeholder_text="Name")
        entrylgaurd.place(relx=0.48, rely=0.58)
        
        labellgaurd = customtkinter.CTkLabel(master=frame3,text="Local Guardian:", font= ("Times New Roman", 19))
        labellgaurd.place(relx=0.70, rely=0.60)
        entrylgaurd = customtkinter.CTkEntry(master=frame3,width=180, placeholder_text="Contact no.")
        entrylgaurd.place(relx=0.82, rely=0.60)
        
        
        
            

        



class Student():
    pass
    root = customtkinter.CTk()
    obj = Student(root)   
    root.mainloop()  