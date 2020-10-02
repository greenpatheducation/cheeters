import random 
import config as conf
#l = [['अ','आ ','उ','ऊ ','ओ ','औ ','अं','अः ','ऌ'],['इ','ई','ड','झ','ङ','ह'],['ऋ','ॠ','ञ','त्र'],['ए','ऐ','र','ग'],['क','फ','ख','य'],['थ','ख','य','ञ'],['घ','छ','ध','ख'],['च','ज','ञ','त्र'],['ट','ठ','ढ','द'],['ण','प','फ','ग','ष','ब'],['त','न','भ','म','स'],['ब','ष','व','द']] 
l=conf.l
number=conf.number
URL=conf.URL
URL2=conf.URL2
def img(fname):
	return '<img src\="'+URL+fname+'.jpg?raw\=true width\="100" height\="100">'
def audio(fname):
	fname=URL2+fname+".mp3"
	return '<br><audio controls><source src\='+fname+' type\="audio/mpeg"></audio>'

def create_quetions(number,f):
	#f = open("QueImg3.txt","w")
	random.shuffle(l)
	for j in range(number):
		options=random.sample(l[j],k=4)
		random.shuffle(options)
		ans=random.choice(options)
	
		f.write("identify the अक्षर: "+img(ans)+audio(ans)+" <br><br>{")	
		
		for i in range(len(options)):
			f.write("\n="+img(options[i])+audio(options[i]) if ans == options[i] else "\n~"+img(options[i])+audio(options[i]))
		
		f.write("\n}\n")
		f.write("\n")
	#f.close()


f = open("MyQueBank.txt","w")
while number > 12:
	number-=12
	create_quetions(12,f)
create_quetions(number,f)

f.close()
