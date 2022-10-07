# Chapter02-1
# 파이썬 완전 기초
# Print 사용법  
# 기본 출력 
print('Python start!')
print("Python start!")
print('''Python start!''')
print("""Python start!""")
print("hello python")
print()
print('P','Y','T','H','O','N',sep=('|'))
print('010', '4692', '9542', sep='-')
print('harchoio','amazon.com',sep='@')
print('Welcome to',end=('  '))
print('IT News',end=(''))


#import 옵션
import sys 

print('Learn python', file=sys.stdout)

# format 사용 (d:3,s:'python',f:3.12442)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one','two'))
print('{1} {0}'.format('one','two'))
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%5s' % ('nice'))
print('%5s' % ('pythonstudy'))
print('%.5s' % 'Pythonstudy')
print('{:10.5}'.format('pythonstudy'))

#d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))
print('%4d' % (42))
print('{:4d}'.format(42))

print('%1.8f' % (3.14609842794))
print('{:f}'.format(3.14609842794))
print('%06.2f'% (3.14609842794))
print('{:06.2f}'.format(3.14609842794))