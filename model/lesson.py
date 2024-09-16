class Lesson:
	def __init__(self, title, code):
		self.title = title
		self.code = code


	@property
	def title(self):
		return self._title


	@title.setter
	def title(self, title):
		self._title = title

	


