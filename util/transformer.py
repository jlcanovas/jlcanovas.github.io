f = open("papers.log", "r", encoding="utf-8")
o = open("publications.log", "w", encoding="utf-8")

start = False

o.write("[\n")
while True:
    line = f.readline()  
    if line.strip().startswith("<li>"):
        title = f.readline()
        title = title.split("<strong>")[1].split("</strong>")[0]
        authors = f.readline()
        reference = f.readline()
        
        year = f.readline()
        empty = f.readline()
        href = f.readline()
        url = href.split("\"")[1]
        o.write(f'    {{\n')
        o.write(f'    "title"     : "{title.strip()}",\n')
        o.write(f'    "authors"   : "{authors.strip()}",\n')
        o.write(f'    "reference" : "{reference.strip()}",\n')
        o.write(f'    "year"      : "{year.strip()}",\n')
        o.write(f'    "url"       : "{url.strip()}"\n')
        o.write(f'    }},\n')

    if not line:
        break


o.write("]")