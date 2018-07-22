import sys


class FileReader():
	def __init__(self,filename):
		self.filename = filename

	def read(self):
		try:
			return open(self.filename).read()
		except OSError as err:
			return ""


if __name__ == '__main__':
	reader = FileReader("example.txt")
	print(reader.read())