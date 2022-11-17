import posixpath
import string


class Loc:
	def __init__(self):
		self.total = 0

	def visit(self, arg, dirname, names):
		for name in names:
			if name in (".", ".."):
				continue

			f = open(dirname + "/" + name, "r")
			lines = len(string.splitfields(f.read(), "\n"))
			print string.rjust(str(lines), 6), dirname + "/" + name
			self.total = self.total + lines
			f.close()


loc = Loc()
posixpath.walk("./Desktop/python-1.0.1", loc.visit, 0)
print string.rjust(str(loc.total), 6), "total"
