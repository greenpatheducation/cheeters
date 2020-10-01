import random 
import test1_config as conf
URL=conf.URL
URL2=conf.URL2
ucharan_varg = conf.varg
akshars = conf.akshars
number = conf.number

def img(fname):
	return '<img src\="'+URL+fname+'.jpg?raw\=true width\="100" height\="100">'
def audio(fname):
	fname=URL2+fname+".mp3"
	return '<br><audio controls><source src\='+fname+' type\="audio/mpeg"></audio>'

def create_QB(number,f):
	temp = list(zip(ucharan_varg, akshars)) 
	random.shuffle(temp) 
	ucharan_varg1, akshars1 = zip(*temp) 
	for i in range(number):
		temp2=list(ucharan_varg1)
		ans=ucharan_varg1[i]

		temp2.remove(ans)
		akshar=random.choice(akshars1[i])	# akshar
		opts=random.sample(temp2,k=3)	# options 
		opts.append(ans)				# answer
		random.shuffle(opts)

		f.write("::MCQ Question::"+img(akshar)+" ध्वनि का उच्चारण स्थान क्या है ?"+audio(akshar)+" {")	
	
		for i in range(len(opts)):
			f.write("\n="+img(opts[i])+audio(opts[i]) if  ans == opts[i] else "\n~"+img(opts[i])+audio(opts[i]))
		
		f.write("\n}\n")
		f.write("\n")
f = open("QueBank.txt","w")
while number > 9:
	number-=9
	create_QB(9,f)
create_QB(number,f)
f.close()

