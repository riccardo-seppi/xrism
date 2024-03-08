import os

def fit_Tbabs_bapec(p2spec, p2out, Emin, Emax, nH, kT, z, vel):
    p2plot = os.path.join('/'.join(p2out.split('/')[:-1]), p2out.split('/')[-1].split('.')[0]+'.ps')
    p2model = os.path.join('/'.join(p2out.split('/')[:-1]), p2out.split('/')[-1].split('.')[0]+'.xcm')
    if not os.path.isfile(p2out):
        f = open('todo.xcm', 'w')
        print('data %s' % p2spec, file=f)
        print('abund aspl', file=f)
        print('cosmo 70 0 0.73', file=f)
        print('statistic cstat', file=f)
        print("method leven 1000 1e-03", file=f)
        print('ignore **-%.1f %.1f-**'%(Emin, Emax), file=f)
        print('model Tbabs(bapec)', file=f)
        print('%s -1 0 0 1 1' % nH, file=f)  # nH
        print('%s 0.001 2 2 15 15' % kT, file=f)  # kT
        print('0.3 -1 0 0 1 1', file=f)  # abundance
        print('%s 1e-5 0.1 0.1 0.3 0.3' % z, file=f)  # z
        print('%s 0.01 5 5 500 500' % vel, file=f)  # vel
        print('1 0.001 0 0 1e10 1e10', file=f)  # norm
        print('fit', file=f)
        print('log %s' % p2out, file=f)
        print('error 1. 2 4 5 6', file=f)
        print('show free', file=f)
        print('log none', file=f)
        print('save model %s'%p2model, file=f)
        print('cpd %s/ocps' % p2plot, file=f)
        print('setplot energy', file=f)
        print('setpl rebin 10 50', file=f)
        print('plot ld delchi', file=f)
        print('setplot com time off', file=f)
        print('setplot com la t " "', file=f)
        print('setplot com cs 1.3', file=f)
        print('setplot com view 0.15 0.35 0.98 0.98', file=f)
        print('setplot com win 2', file=f)
        print('setplot com view 0.15 0.1 0.98 0.35', file=f)
        print('setplot com lw 3', file=f)
        print('plot ld delchi', file=f)
        print('quit', file=f)
        f.close()

        os.system('xspec - todo.xcm')
        os.system('rm todo.xcm')
    else:
        print(p2spec, 'already fitted!')



def fit_Tbabs_bapec_bapec(p2spec, p2out, Emin, Emax, nH, kT, z, vel):
    p2plot = os.path.join('/'.join(p2out.split('/')[:-1]), p2out.split('/')[-1].split('.')[0]+'.ps')
    p2model = os.path.join('/'.join(p2out.split('/')[:-1]), p2out.split('/')[-1].split('.')[0]+'.xcm')
    if not os.path.isfile(p2out):
        f = open('todo.xcm', 'w')
        print('data %s' % p2spec, file=f)
        print('abund aspl', file=f)
        print('cosmo 70 0 0.73', file=f)
        print('statistic cstat', file=f)
        print("method leven 1000 1e-03", file=f)
        print('ignore **-%.1f %.1f-**'%(Emin, Emax), file=f)
        print('model Tbabs(bapec + bapec)', file=f)
        print('%s -1 0 0 1 1' % nH, file=f)  # nH
        print('%s 0.001 2 2 15 15' % kT, file=f)  # kT
        print('0.3 -1 0 0 1 1', file=f)  # abundance
        print('%s 1e-5 0.1 0.1 0.3 0.3' % z, file=f)  # z
        print('%s 0.01 5 5 500 500' % vel, file=f)  # vel
        print('1 0.001 0 0 1e10 1e10', file=f)  # norm
        print('%s 0.001 2 2 15 15' % kT, file=f)  # kT
        print('0.3 -1 0 0 1 1', file=f)  # abundance
        print('%s 1e-5 0.1 0.1 0.3 0.3' % z, file=f)  # z
        print('%s 0.01 5 5 500 500' % vel, file=f)  # vel
        print('1 0.001 0 0 1e10 1e10', file=f)  # norm
        print('fit', file=f)
        # print('save model ',p2out_model, file=f)
        print('log %s' % p2out, file=f)
        print('error 1. 2 4 5 6 7 9 10 11', file=f)
        print('show free', file=f)
        print('log none', file=f)
        print('save model %s'%p2model, file=f)
        print('cpd %s/ocps' % p2plot, file=f)
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
    else:
        print(p2spec, 'already fitted!')