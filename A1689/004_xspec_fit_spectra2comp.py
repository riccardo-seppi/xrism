import sys, os

p2spec = '/home/riccardo/xrism/A1689/sixte_files/2comp/A1689_SPEC_resolve.pha'
#p2out_model = os.path.join('/'.join(p2spec.split('/')[:-1]), 'modelpars.txt')
p2plot = os.path.join('/'.join(p2spec.split('/')[:-1]), 'plot_spec.ps')
p2plot_Fe = os.path.join('/'.join(p2spec.split('/')[:-1]), 'plot_spec_Fe.ps')
p2log = os.path.join('/'.join(p2spec.split('/')[:-1]), 'bestfit.log')

nH = 0.0167
kT = 8.8
z = 0.1842
vel = 180
f = open('todo.xcm', 'w')
print('data %s'%p2spec,file=f)
print('abund aspl', file=f)
print('cosmo 70 0 0.73', file=f)
print('statistic cstat', file=f)
print("method leven 1000 1e-03", file=f)
print('ignore **-2.0 8.0-**', file=f)
print('model Tbabs(bapec + bapec)', file=f)
print('%s -1 0 0 1 1'%nH, file=f) #nH
print('%s 0.001 2 2 15 15'%kT, file=f) #kT
print('0.3 -1 0 0 1 1', file=f) #abundance
print('%s 1e-5 0.1 0.1 0.3 0.3'%z, file=f) #z
print('%s 0.01 5 5 500 500'%vel, file=f) #vel
print('1 0.001 0 0 1e10 1e10', file=f) #norm
print('%s 0.001 2 2 15 15'%kT, file=f) #kT
print('0.3 -1 0 0 1 1', file=f) #abundance
print('%s 1e-5 0.1 0.1 0.3 0.3'%z, file=f) #z
print('%s 0.01 5 5 500 500'%vel, file=f) #vel
print('1 0.001 0 0 1e10 1e10', file=f) #norm
print('fit', file=f)
#print('save model ',p2out_model, file=f)
print('log %s'%p2log, file=f)
print('error 1. 2 4 5 6 7 9 10 11', file=f)
print('show free', file=f)
print('log none', file=f)
print('cpd %s/ocps'%p2plot, file=f)
print('setplot energy', file=f)
print('setpl rebin 10 30', file=f)
print('plot ld delchi', file=f)
print('setplot com time off', file=f)
print('setplot com la t " "', file=f)
print('setplot com cs 1.3', file=f)
print('setplot com view 0.15 0.35 0.98 0.98', file=f)
print('setplot com win 2', file=f)
print('setplot com view 0.15 0.1 0.98 0.35', file=f)
print('setplot com lw 3', file=f)
print('quit', file=f)
f.close()

os.system('xspec - todo.xcm')
os.system('rm todo.xcm')


sys.exit()