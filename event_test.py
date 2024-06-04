# https://stackoverflow.com/questions/4083796/

import unittest
import tkinter
import tkinter.ttk as ttk



class TKinterTestCase(unittest.TestCase):
	""" These methods are going to be the same for every GUI test,
		so refactored them into a separate class
	"""
	def setUp(self):
		self.root = tkinter.Tk()
		self.pump_events()


	def tearDown(self):
		if self.root:
			self.root.destroy()
			self.pump_events()


	def pump_events(self):
		while self.root.dooneevent(tkinter._tkinter.ALL_EVENTS | tkinter._tkinter.DONT_WAIT):
			pass



class TestViewAskText(TKinterTestCase):

	def test_enter(self):
	
		v = View_AskText(self.root, value='A')
		self.pump_events()
		v.e.focus_set()
		v.e.insert(tkinter.END, 'B')
		v.e.event_generate('<Return>')
		self.pump_events()

		#self.assertRaises(tkinter.TclError, lambda: v.winfo_viewable())
		#self.assertEqual(v.value, 'AB')
		self.assertEqual(v.value, 'Return')


# ###########################################################
# The class being tested (normally, it's in a separate module
# and imported at the start of the test's file)
# ###########################################################

class View_AskText(tkinter.Toplevel):

	def __init__(self, root, value=None):
	
		self.value = value
		
		super().__init__(root)
		self.grab_set()
		
		self.l = ttk.Label(self, text='Value:')
		self.l.pack()
		
		self.e = ttk.Entry(self)
		self.e.pack()
		
		self.b = ttk.Button(self, text='Ok', command=self.save)
		self.b.pack()

		
		if value: self.e.insert(0, value)
		
		
		self.e.focus_set()
		self.bind('<Return>', self.save)
		################################


	def save(self, event=None):
		#self.value = self.e.get()
		self.value = event.keysym
		self.destroy()


if __name__ == '__main__':
	unittest.main()

