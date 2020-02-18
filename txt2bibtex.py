class Article:
    def __init__(self, label, authorlist, title, journal, volume, number, year, pages, doi):
        self.label = label
        self.authorlist = authorlist
        self.title = title
        self.journal = journal
        self.volume = volume
        self.number = number
        self.year = year
        self.pages = pages
        self.doi = doi

    @classmethod
    def fromline(cls,line):
        stringlist = line.split('"')
        authors = stringlist[0].split(',')[:-1]
        authorlist = []
        for author in authors:
            names = author.split(" ")
            lastname = names[-1]
            firstnames = "  ".join([name for name in names[:-1] if name != 'and'])
            authorlist.append((lastname,firstnames))
        title = stringlist[1]
        journal = stringlist[2].split(",")[0]
        rest = stringlist[2].split(",")[1].split()
        volume = rest[0]
        number = '""'
        year = "".join([c for c in rest[2] if c in "0123456789"])
        pages = rest[1]
        doi = ""
        label = authorlist[0][0]+year
        return Article(label, authorlist, title, journal, volume, number, year, pages, doi)

    def write(self):
        print("@article{%s," % self.label)
        print('  author = "', end="")
        for author in self.authorlist[:-1]:
            print("%s, %s and " % (author[0],author[1]), end="")
        lastauthor = self.authorlist[-1]
        print('%s, %s",' % (lastauthor[0],lastauthor[1]))
        print('  title = "%s",' % self.title)
        print('  journal = "%s",' % self.journal)
        print('  volume = %s,' % self.volume)
        print('  number = %s,' % self.number)
        print('  year = %s,' % self.year)
        print('  pages = "%s",' % self.pages)
        print('  doi = "%s",' % self.doi)
        print("}\n")

# @article{alleman2017,
#   author = "Alleman, Coleman and Foulk, III., James W. and Mota, Alejandro and Lim, Hojun and Littlewood, David J.",
#   title = "Concurrent multiscale modeling of microstructural effects on localization behavior in finite deformation solid mechanics",
#   journal = "Computational Mechanics",
#   volume = 61,
#   number = {1-2},
#   year = 2018,
#   pages = "207--218",
#   doi = "10.1007/s00466-017-1481-5",
# }

# label = "alleman2017"
# authorlist = [
#     ("Alleman", "Coleman"), 
#     ("Foulk", "III., James W."), 
#     ("Mota", "Alejandro"),
#     ("Lim", "Hojun"),
#     ("Littlewood", "David J.")
# ]
# title = \
# "Concurrent multiscale modeling of microstructural effects on localization behavior in finite deformation solid mechanics"
# journal = "Computational Mechanics"
# volume = "61"
# number = "{1-2}"
# year = "2018"
# pages = "207--218"
# doi = "10.1007/s00466-017-1481-5"

# a = Article(label, authorlist, title, journal, volume, number, year, pages,doi)
# a.write()

# line = 'Y. Zuo, C. Chen, X. Li, Z. Deng, Y. Chen, J. Behler, G. Csnyi, A. V. Shapeev, A. P. Thompson, M. A. Wood, and S. P. Ong, "A performance and cost assessment of machine learning interatomic potentials," J. Phys. Chem. A, 124 731 (2020).'

# a = Article.fromline(line)
# a.write()

filename = "vita_2020.txt"
file = open(filename,'r',encoding="utf-16")

startflag = False
while 1:
    line = file.readline()
    if "PUBLICATIONS" in line:
        startflag = True
    elif "INVITED TALKS" in line:
        break
    elif startflag:
        if len(line) > 1:
            a = Article.fromline(line)
            a.write()

