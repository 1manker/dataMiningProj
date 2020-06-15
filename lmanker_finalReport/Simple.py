class Simple:
	def __init__(self, age, gender, education, country, ethnicity, nscore,
		escore, oscore, ascore, cscore, impulse, sensation):
		self.age = age
		self.gender = gender
		self.education = education
		self.country = country
		self.ethnicity = ethnicity
		self.nscore = nscore
		self.escore = escore
		self.oscore = oscore
		self.ascore = ascore
		self.cscore = cscore
		self.impulse = impulse
		self.sensation = sensation

	def printToFile(self, filename):
		f = open(filename, "a+")
		f.write(str(self.age))
		f.write(",")
		f.write(str(self.gender))
		f.write(",")
		f.write(str(self.education))
		f.write(",")
		f.write(str(self.country))
		f.write(",")
		f.write(str(self.ethnicity))
		f.write(",")
		f.write(str(self.nscore))
		f.write(",")
		f.write(str(self.escore))
		f.write(",")
		f.write(str(self.oscore))
		f.write(",")
		f.write(str(self.ascore))
		f.write(",")
		f.write(str(self.cscore))
		f.write(",")
		f.write(str(self.impulse))
		f.write(",")
		f.write(str(self.sensation))
		f.write("\n")
		f.close()