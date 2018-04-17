import tkinter as tk


def do_cmd():
	t0.delete(1.0,'end')
	t0.insert('insert', 'dadfasdf')
	var = t0.get(1.0,'end')
	print(var)

	
win = tk.Tk()
win.geometry('800x600')
#frm = tk.Frame(win,width='400',height='300', bg='yellow').grid(row=0)
#frml = tk.Frame(frm,width='200',height='100',bg='red').grid(row=0, column=0)
#frmr = tk.Frame(win,width='200',height='100',bg='green').grid(row=1,column=1)

cmd = ['cmd0','cmd1','cmd2','cmd2','cmd2','cmd2','cmd2','cmd2','cmd2',
'cmd2','cmd2','cmd2','cmd2']
arg = ['0x00000000','0x00ff8080','0x00000000','0x00300000','0x00000000','0x00000000','0x00000000'
,'0x00000000','0x00000000','0x00000000','0x00000000','0x00000000','0x00000000']
for i in range(13): 
	lb0=tk.Label(win,text=i,width='5',height='2').grid(row=i,column=0)
	b0=tk.Button(win, text=cmd[i],width='5',height='1',command=do_cmd).grid(row=i,column=1)
	t0=tk.Text(win,width='15',height='1')
	t0.insert(1.0, arg[i])
	t0.grid(row=i,column=2)
e0=tk.Entry(win,text='dafsdf').grid(row=3,column=3)

#b2=tk.Button(win, text='2').grid(row=1,column=1)
win.mainloop()
