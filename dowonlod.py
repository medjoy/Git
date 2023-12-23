from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from tkinter import messagebox

aymane = Tk()
aymane.geometry('1000x500+175+95')
aymane.title('Download Video')
aymane.configure(background="#CA37AE")
aymane.resizable(False,False)
aymane.iconbitmap('ic.ico')
title= Label(aymane , text=('Download Video System'),bg='white',fg='black',font=('Bauhaus 93',15,'bold'))
title.pack(fill=X)

def URL():
  E1 = e_url.get()
  all_stream = YouTube(E1).streams.all()
  def Download():
    try:
      E2=e1_url.get()
      folder_name= filedialog.askdirectory()
      choice =all_stream[int(E2)].download(folder_name)
      messagebox.showinfo('[Dowanload] system','The vidio was Dowanload withot porblem')
    except Exception as r:
      messagebox.showerror('[Dowanload] Error',r)
      

  F=Frame(aymane,bg='#EBE3D5')
  F.place(x=50,y=150,width=900,height=340)
  title_Fr=Label(F,text='Choose The Suitable Stream',bg='#E82578',fg='black',font=('Bauhaus 93',12))
  title_Fr.pack(fill=X)
  v=-1
  for i in all_stream:
    v=v+1
    Label(F,text=(str(v),''':''',str(i))).pack()

  e1_url=Entry(F,bg='#F4DFC8')
  e1_url.place(x=150,y=300,width=200,height=30)
  B1_url=Button(F,text='Download',bg='#3C7DF1' ,command=Download)
  B1_url.place(x=450,y=300,width=200, height=30)



lb_url=Label(aymane,text='Enter The URL :',bg='#CA37AE',font=('Bauhaus 93',12))
lb_url.place(x=30,y=50)
e_url=Entry(aymane,bg='#F4DFC8')
e_url.place(x=200,y=37,width=600,height=50)
B_url=Button(aymane,text='Download',bg='#3C7DF1', command=URL )
B_url.place(x=820,y=37,width=160, height=50)



aymane.mainloop()