import tkinter
import os


class Editor(tkinter.Toplevel):

	def __init__(self, root):
		
		self.root = root
		super().__init__(self.root, class_='myclass', bd=4)
		self.title('Tittelii')
		
		self.textwid = tkinter.Text(self.root)
		self.textwid.bind('<Control-p>', self.mycallback2)
		self.textwid.pack()
		
		
		self.eventnum = 0
		self.textwid.insert('1.0', 'asd')
		self.textwid.wait_visibility()
		self.textwid.focus_set()
		self.textwid.mark_set('insert', '1.0')
		
		self.waitvar = tkinter.IntVar()
		self.waitvar.set(False)
		
		self.after(300, self.textwid.event_generate('<Control-p>'))
		
	
	def mycallback2(self, event=None):
		#print(event.state)
		self.waitvar.set(event.state)
		#self.root.quit()
		#self.root.destroy()

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
		



def start_application():
	root = tkinter.Tk()
	app = Editor(root)
	return app



if __name__ == '__main__':
	a = start_application()
	a.mainloop()
	
##	if os.name != "nt" and os.getenv("GITHUB_ACTIONS"):
##		print('jou')
##		os.system('Xvfb :1 -screen 0 1600x1200x16  &')
##		os.environ["DISPLAY"] = ":1.0"
##
##	r = tkinter.Tk()
##	e = Editor(r)
##	e.mainloop()
