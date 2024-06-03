import tkinter


class Editor(tkinter.Toplevel):

	def __init__(self):
		
		self.root = tkinter.Tk()
		super().__init__(self.root, class_='myclass', bd=4)

		self.textwid = tkinter.Text(self.root)
		self.textwid.pack()
		self.textwid.bind('<Control-p>', self.mycallback2)
		
		
		self.eventnum = 0
		self.textwid.insert('1.0', 'asd')
		self.textwid.wait_visibility()
		self.textwid.focus_set()
		self.textwid.mark_set('insert', '1.0')
		
		self.after(300, self.textwid.event_generate('<Control-p>'))
		self.do_nothing()
		
	
	def mycallback2(self, event=None):
		print(event.state, 'jou')
		return 'break'
		
	def do_nothing(self):
		x = 0
		for i in range(10000):
			x = x// 100
			for j in range(10000):
				x = x// 100
				for k in range(10000):
					x = x// 100
					for l in range(10000):
						x = x// 100
						for m in range(10000):
							x = x // 100
							for n in range(10000):
								x = x + n
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
		
