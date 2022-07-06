#serialization(dump)
import pickle
f=open("pickled.txt","wb")
dct={"name":"ram","age":23,"gender":"male"}
pickle.dump(dct,f)
f.close()

#deserialization(load)
import pickle
f=open("pickled.txt","rb")
d=pickle.load(f)
print(d)
f.close()

#output:{'name': 'ram', 'age': 23, 'gender': 'male'}

#serialization (dumps)
from pickle import dumps
dct={"name":"ram","age":23,"gender":"male"}
dctstring=dumps(dct)
print(dctstring)
#outPut:b'\x80\x04\x95*\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x03ram\x94\x8c\x03age\x94K\x17\x8c\x06gender\x94\x8c\x04male\x94u.'


import pickle
def storedate():
    ram={'key':'ram','name':'ramkumar','age':'23','pay':'40000'}
    bharani={'key':'kumar','name':'kumar','age':'25','pay':'50000'}
    db={}
    db['ram']=ram
    db['bharani']=bharani
    dbfile=open('examplepickle','ab')
    pickle.dump(db,dbfile)
    dbfile.close()