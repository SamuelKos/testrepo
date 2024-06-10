import tkinter
import os


class Editor(tkinter.Toplevel):

	def __init__(self):
		#os.system('Xvfb  &')
		#os.environ["DISPLAY"] = ":0.0"
		
		self.root = tkinter.Tk()
		super().__init__(self.root, class_='myclass', bd=4)

		self.textwid = tkinter.Text(self.root)
		#self.textwid.bind('<<Copy>>', self.mycallback2)
		self.textwid.bind('<Shift-Left>', self.mycallback2)
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
		self.eventnum += 1
		
		print(f'Begin Event {self.eventnum}:\n')
	
		l = [ item for item in dir(event) if '_' not in item ]
		
		for key in l:
			print(key, getattr(event, key))
		
		
		print(f'\nEnd Event {self.eventnum}:')
		print(10*'= ')
		
		return 'break'
		





