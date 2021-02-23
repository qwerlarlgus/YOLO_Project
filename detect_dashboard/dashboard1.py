import sys
import entry_exit
import detect1

if __name__ == '__main__':
    argument = sys.argv
    del argument[0]			# 첫번째 인자는 script.py 즉 실행시킨 파일명이 되기 때문에 지운다
#    print('Argument : {}'.format(argument))

a, b = detect1.detect()
c, d = entry_exit.entry_exit()

print('Occupied   : {:03d}'.format(a))
print('Free Space : {:03d}'.format(b))
print('# of Entry : {:03d}'.format(c))
print('# of Exit  : {:03d}'.format(d))

