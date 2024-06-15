import tkinter
import tkinter.font


class Editor(tkinter.Toplevel):

	def __init__(self):
		
		self.root = tkinter.Tk()
		super().__init__(self.root, class_='myclass', bd=4)

		self.menufont = tkinter.font.Font(family='TkDefaulFont', size=10, name='menufont')
		self.textwid = tkinter.Text(self.root, font=self.menufont)
		
		#self.textwid.bind('<<Copy>>', self.mycallback2)
		self.textwid.bind('<Shift-Left>', self.mycallback2)
		self.textwid.bind( "<<TkWorldChanged>>", self.mycallback)

		self.textwid.pack()
		
		
		self.eventnum = 0
		self.textwid.insert('1.0', 'asd')
		self.textwid.wait_visibility()
		self.textwid.focus_set()
		self.textwid.mark_set('insert', '1.1')
		
		self.waitvar = tkinter.IntVar()
		self.waitvar.set(False)
		
		#self.after(300,self.textwid.event_generate('<Left>'))
		#self.textwid.event_generate('<Control-p>')
		

	def mycallback2(self, event=None):
		#self.textwid.event_generate('<Control-p>')
		#self.update_idletasks()
		print(event.state, event.keysym)
		return 'break'

	
	def quit_me(self, event=None):
		self.root.quit()
		self.root.destroy()
		return 'break'
		
		
	def mycallback(self, event=None):
		print('jou')
		





