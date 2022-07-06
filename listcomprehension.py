#simple code  with out useing list_comprehension
#fruits=['apple','banana','cherry','mango']
#newlist=[]
#for x in fruits:
   # if 'a' in x:
     #   newlist.append(x)
      #  print(newlist)

# list comprehension code

#fruits=['apple','banana','cherry','mango']
#newlist=[each_fruits for each_fruits in fruits if 'a'in each_fruits]
#print(newlist)

#with out list comprehension code for str
#h_letter=[]
#for letter in 'ramkumar':
#    h_letter.append(letter)
#    print(h_letter)

#useing list comprehension code for str

#h_letter=[letter for letter in 'RAMKUMAR']
#print(h_letter)

#list comprehension code for even number's

#even_list=[x for x in range(20) if (x%2==0)]
#print(even_list)

#with out list comprehension code for odd number
#for x in range(50):
#    if(x%2)!=0:
#        print("even number:",x)

# with out list comprehension code useign fumction
#def doubl(x):
#    return x*2
#seq=doubl(21)
#print(seq)


#list comprehension code
#def doubl(x):
#    return x**2
#    y=[double(x) for x in range(10)]
#    print(y)


# text="ramkumar,kumar,sai,bharani,lsakmi,sai,sri,kavya,chelli"
#newstr=[]
#for x in text:
 #   if  text in 'aeiou':
#        newstr.append(text)
 #       print(newstr)


text="ramkumar,kumar,sai,sri,kavya,chelli"
vowels=(each_letter for each_letter in text if each_letter in 'aeiou')
print(vowels)
print(next(vowels))
print(next(vowels))
print(next(vowels))
print(next(vowels))
print(next(vowels))
print(next(vowels))
print(next(vowels))
print(next(vowels))
