  1 def func(f, x):
  2     return eval(f.replace('x', str(x)))
  3 
  4 def factors(x):
  5     x = abs(x)
  6     for i in range(1, x+1):
  7         if x % i == 0:
  8             yield i
  9             yield -i
 10 
 11 print('... ax^3 + bx^2 + cx^1 + dx^0 = a b c d\n')
 12 coefs = input('Coeffs: ').split(' ')
 13 size = len(coefs)
 14 f = ' + '.join(['(' + coefs[i] + '*x**' + str(size-i-1) + ')' for i in range(size)])
 15 print('\nfactors of', f, '\n')
 16 
 17 for a in factors(int(coefs[0])):
 18     for b in factors(int(coefs[-1])):
 19         if func(f, b/a) == 0:
 20             print(f'({a}x - {b})')
