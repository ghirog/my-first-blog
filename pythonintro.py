def hi(name):
    if name=='Hiro':
        print('Hi Hiro!')
    elif name=='HHH':
        print('Hi HHH!')
    else:
        print('Hi! ' +name )


print('hello django girls')

if 5>9:
    print('5 is indeed greater than 2')
else:
     print('5 is not greater than 2')

#コメントです！

name='AAAA'
if name=='BBB':
    print('HELLO BBB')
elif name=='AAA':
    print('HELLO AAA')
else:
    print('知らない')

hi('HiroA')

#-------------------------------------------------------
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']

for name in girls:
    hi(name)
    print('Next Girl')
