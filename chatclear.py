import sqlitepython as sqlpy

def get_index(b,c):
    try:
        a=b.index(c)
    except:
        a=0
    return a

k=0;set1=['',''];set2=['','']
sherba=['Thiago Ferreira', 'Gustavo Café', 'Ze', 'Gabriel Barbosa', 'Sanson',
        'Leonardo Souto', 'Joao Boger', 'Ian Jordy', 'Anthony Apost',
        'Alexandher Kill', 'Remus', 'Juarez', 'Adolfo', 'Alisson',
        'Franck', 'Romulo', 'Krik', 'O Pêssegussy', 'Kevin Voigt',
        'Helcio', 'Ibarra', 'Tirelli']

with open('testebotburro.txt', 'r', encoding="UTF-8") as b, open('teste12.txt', 'r+', encoding="UTF-8") as d:
	for line in b:
		if 'omitted>' not in line:
			hifen=get_index(line, '- ')
			if hifen != 0:
				a=line[get_index(line, '- ')+2:]
				d.write(a)
			else:
				d.write(line)
				a=line
b.close();d.close()

a=['','']
with open('teste123.txt', 'r', encoding="UTF-8") as e:
	for line in e:
		if line[:get_index(line,':')] in sherba:
			sqlpy.insert_into_msg(sqlpy.connection(r'frases.db'),a)
		if	line[:get_index(line,':')] in sherba:
			a[0]=line[:get_index(line,':')];a[1]=line[get_index(line,':')+2:].replace('\n','')
		else:
			formatedline=line[get_index(line,':'):].replace("\n"," ")
			a[1]=a[1]+f"{formatedline}"
e.close()