import os
import sys
import subprocess

# Soluciones
s1 = 'equal test 1 result = 1\nequal test 2 result = 0'
s2 = 'Checking first list for cycles. There should be none, ll_has_cycle says it has no cycle'
s2+='\nChecking second list for cycles. There should be a cycle, ll_has_cycle says it has a cycle'
s2+='\nChecking third list for cycles. There should be a cycle, ll_has_cycle says it has a cycle'
s2+='\nChecking fourth list for cycles. There should be a cycle, ll_has_cycle says it has a cycle'
s2+='\nChecking fifth list for cycles. There should be none, ll_has_cycle says it has no cycle'
s2+='\nChecking length-zero list for cycles. There should be none, ll_has_cycle says it has no cycle'



s3 = 'My number is: 1'
s3+='\nMy number is: 5185'
s3+='\nMy number is: 38801'
s3+='\nMy number is: 52819'
s3+='\nMy number is: 21116'
s3+='\nMy number is: 54726'
s3+='\nMy number is: 26552'
s3+='\nMy number is: 46916'
s3+='\nMy number is: 41728'
s3+='\nMy number is: 26004'
s3+='\nMy number is: 62850'
s3+='\nMy number is: 40625'
s3+='\nMy number is: 647'
s3+='\nMy number is: 12837'
s3+='\nMy number is: 7043'
s3+='\nMy number is: 26003'
s3+='\nMy number is: 35845'
s3+='\nMy number is: 61398'
s3+='\nMy number is: 42863'
s3+='\nMy number is: 57133'
s3+='\nMy number is: 59156'
s3+='\nMy number is: 13312'
s3+='\nMy number is: 16285'
s3+='\n ... etc etc ... '
s3+='\nGot 65535 numbers before cycling!'
s3+='\nCongratulations! It works!'


def execute(cmd):
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    out, err = proc.communicate()
    return out, proc.returncode


def evaluate(total, tests, program):
    discount = total
    for test in tests:
        result = test
        out, returncode = execute('./' + program)
        if not (returncode == 0 and out.strip() == result):
            total -= discount
            print "result: \n"+out.strip()
            print('.' * 20)
            print "expected: \n" + result
        print('.' * 20)
    return total


def ex2():
    return evaluate(25, [s1], 'll_equal.out')


def ex3():
    return evaluate(25, [s2], 'll_cycle.out')


def ex4():
    return evaluate(25, [s3], 'll_lfsr.out')


def main(n):
    fs = [ex2, ex3, ex4]
    if n != -1:
        print('Calificando Ejercicio: {0}'.format(n))
        print('.' * 20)
        print('Nota: {0}/25'.format(fs[n-2]()))
    else:
        total = 0
        print('Calificando Todo:\n')
        for n, ex in enumerate(fs):
            nota = ex()
            print('Calificando Ejercicio: {0}'.format(n + 2))
            print('.' * 20)
            print('Nota: {0}/25'.format(nota))
            total += nota
            print('')
        print('TOTAL: {0}/75'.format(total))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        main(-1)
    else:
        main(int(sys.argv[1]))
