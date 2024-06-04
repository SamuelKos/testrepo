import unittest
import time

from event_test3 import start_application

class TestGui(unittest.TestCase):
	
	# this will run on a separate thread.
	async def _start_app(self):
		self.app.mainloop()
	
	
	async def _doit(self):
		self.app.wait_variable(self.app.waitvar)
		
	
	def setUp(self):
		self.app = start_application()
		self._start_app()
		self._doit()

	
	def tearDown(self):
		self.app.destroy()

	
	def test_startup(self):
##		title = self.app.winfo_toplevel().title()
##		expected = 'Titteli'
##		self.assertEqual(title, expected)
		#value = 'no'
		expected = 3
			
		value = self.app.waitvar.get()
		#print(i, 'AAAAAAAA')
		self.assertEqual(value, expected)
		


if __name__ == '__main__':
	unittest.main()

