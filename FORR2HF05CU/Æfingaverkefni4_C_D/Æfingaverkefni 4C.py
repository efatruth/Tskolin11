#1

listi=[1,2,3,6,8,9,99,333] #listi sem unnið er með
#finnur allar tölur sem ganga upp í 3 og setur í nýjan lista
nyr_listi=list(filter(lambda x: (x % 3==0), listi))
#úttak
print(nyr_listi)

#2

nyr_listi2=list(map(lambda x: x*4, listi))
print(nyr_listi2)

