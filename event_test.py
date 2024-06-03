import tkinter


class Editor(tkinter.Toplevel):

	def __init__(self, root):
		
		self.root = root
		super().__init__(self.root, class_='myclass', bd=4)

		self.textwid = tkinter.Text(self.root)
		self.textwid.pack()
		self.textwid.bind('<Control-p>', self.mycallback2)

		
		self.eventnum = 0
		self.textwid.insert('1.0', 'asd')
		self.textwid.wait_visibility()
		self.textwid.focus_set()
		self.textwid.mark_set('insert', '1.0')
		print('1')
		self.after(300, self.textwid.event_generate('<Control-p>'))
		print('2')
	
	def mycallback2(self, event=None):
		print('3')
		print(event.state)
		self.root.quit()
		self.root.destroy()

	
	def mycallback(self, event=None):
		self.eventnum += 1
		
		print(f'Begin Event {self.eventnum}:\n')
	
		l = [ item for item in dir(event) if '_' not in item ]
		
		for key in l:
			print(key, getattr(event, key))
		
		
		print(f'\nEnd Event {self.eventnum}:')
		print(10*'= ')
		
		return 'break'



if __name__ == '__main__':

	r = tkinter.Tk()
	e = Editor(r)
	e.mainloop()

		
