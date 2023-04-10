import datetime
import glob


class Filexts:
	'''
	This class scans files of a single given file extension or file type.
	This class takes two arguements:
	(1)root_dir: a directory string where the search stars and 
	(2)search_depth: the number of directories to scan from the "search_str", is optional and defaults to 1.
	'''
	
	
	def __init__(self, root_dir, search_depth = 1):
		self.root_dir = root_dir
		self.star = self.root_dir.find('*')
		
		self.all_files = []
		
		self.fix = '*/'
		
		
		for i in range(search_depth):
			self.next_dir()

		
	def list(self):
		return self.all_files
		
	def __getitem__(self, index):
		return self.all_files[index]
		
		
	def next_dir(self):
		self.search_dir = glob.glob(self.root_dir)
		for self.file in self.search_dir:
			if self.file not in self.all_files:
				self.all_files.append(self.file)
			else:
				pass
		self.root_str = (
		    self.root_dir[:self.star]
		    + self.fix
		    + self.root_dir[self.star:])
