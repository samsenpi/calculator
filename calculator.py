import tkinter as tk
import re

root=tk.Tk()
root.title('calculator')

e=tk.Entry(width=70,borderwidth=5,fg='black',bg='white',)
e.grid(row=0,column=1,columnspan=3,padx=50,sticky='ew')

def on_click(n):
      
      if n=='=':
          ans=enter(e.get())
          e.delete(0, tk.END)
          e.insert(0,str(ans))
      elif n=='X':
          l=e.get()
          ml=len(l)
          e.delete(ml-1,tk.END)
          
      else:    
         num=[]
         num.append(n)
         current=str(e.get())
         e.delete(0, tk.END)
         e.insert(0,current+str(n))
      
      

   

def oper(num):
   
      # if i in operator:
      #    x,y=n.split(j in n for j in operator)
      #    num=eval(x)
      #    num2=eval(y)
      # else: 
   ...
   
def enter(n):
   print(n)
   operator=['+','-','*','/']
   
   result=re.search(r"^(\d+)[+/*-](\d+)$",n)
   print(result)
   
   if result:
       num =eval( result.group(1))
       num2 = eval(result.group(2))
       print("Number 1:", num)
       print("Number 2:", num2)
   else:
       print("Pattern not found in the text.")     
   for i in n:
       
       if i=="+":
           return num+num2
       
       elif i=="-":
           return num-num2
       
       elif i=="/":
           return num/num2
            
       elif i=="*":
           return num*num2
       
   

def main():
   # btnFrame=tk.Frame(root)
   # btnFrame.columnconfigure(0,weight=1)
   # btnFrame.columnconfigure(1,weight=1)
   # btnFrame.columnconfigure(2,weight=1)
   # btnFrame.columnconfigure(3,weight=1)
   # btnFrame.columnconfigure(4,weight=1)
   btn0=tk.Button(root,text='0',command=lambda:on_click(0),fg='white',bg='black',padx=50,pady=20)
   btn1=tk.Button(root,text='1',command=lambda:on_click(1),fg='white',bg='black',padx=50,pady=20)
   btn2=tk.Button(root,text='2',command=lambda:on_click(2),fg='white',bg='black',padx=50,pady=20)
   btn3=tk.Button(root,text='3',command=lambda:on_click(3),fg='white',bg='black',padx=50,pady=20)
   btn4=tk.Button(root,text='4',command=lambda:on_click(4),fg='white',bg='black',padx=50,pady=20)
   btn5=tk.Button(root,text='5',command=lambda:on_click(5),fg='white',bg='black',padx=50,pady=20)
   btn6=tk.Button(root,text='6',command=lambda:on_click(6),fg='white',bg='black',padx=50,pady=20)
   btn7=tk.Button(root,text='7',command=lambda:on_click(7),fg='white',bg='black',padx=50,pady=20)
   btn8=tk.Button(root,text='8',command=lambda:on_click(8),fg='white',bg='black',padx=50,pady=20)
   btn9=tk.Button(root,text='9',command=lambda:on_click(9),fg='white',bg='black',padx=50,pady=20)
   btn_add=tk.Button(root,text='+',command=lambda:on_click('+'),fg='white',bg='black',padx=50,pady=20)
   btn_sub=tk.Button(root,text='-',command=lambda:on_click('-'),fg='white',bg='black',padx=50,pady=20)
   btn_div=tk.Button(root,text='/',command=lambda:on_click('/'),fg='white',bg='black',padx=50,pady=20)
   btn_mul=tk.Button(root,text='*',command=lambda:on_click('*'),fg='white',bg='black',padx=50,pady=20)
   btn_clear=tk.Button(root,text='X',command=lambda:on_click('X'),fg='white',bg='black',padx=60,pady=20)
   btn_equal=tk.Button(root,text='=',command=lambda:on_click('='),fg='white',bg='black',padx=70,pady=20)
   btn1.grid(row=1,column=1,sticky="news")
   btn2.grid(row=1,column=2,sticky="news")
   btn3.grid(row=1,column=3,sticky="news")
   btn4.grid(row=2,column=1,sticky="news")
   btn5.grid(row=2,column=2,sticky="news")
   btn6.grid(row=2,column=3,sticky="news")
   btn7.grid(row=3,column=1,sticky="news")
   btn8.grid(row=3,column=2,sticky="news")
   btn9.grid(row=3,column=3,sticky="news")
   btn0.grid(row=4,column=1,sticky="news")
   btn_add.grid(row=4,column=2,sticky="news")
   btn_sub.grid(row=4,column=3,sticky="news")
   btn_div.grid(row=5,column=1,sticky="news")
   btn_mul.grid(row=5,column=2,sticky="news")
   btn_clear.grid(row=5,column=3,sticky="news")
   btn_equal.grid(row=6,column=1,sticky="news")

   # btnFrame.pack(fill="both")
   # btnFrame.grid(root)

   root.mainloop()
 

if __name__=='__main__':
   main()
