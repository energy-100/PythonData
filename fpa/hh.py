import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import log
from scipy.optimize import curve_fit
from scipy import log as log
from scipy.stats.distributions import  t
import seaborn as sns
def fun(u, d, f, data):
    selectedFunction = f
    z = 0
    temp = 0
    tss = 0
    datax = range(1, len(data) + 1)
    for spot in data:
        temp += spot
    datamean = temp / len(data)
    for spot in data:
        tss += (spot - datamean) ** 2

    if selectedFunction == 1:
        for i in range(len(data)):
            z += (u[0] * ((u[1] + datax[i] / u[2]) ** (-u[3])) + u[4] - data[i]) ** 2
        # print(z)
    elif selectedFunction == 2:
        for i in range(len(data)):
            z += (u[0]*datax[i]**4+u[1]*datax[i]**3 + u[2]*datax[i]**2+u[3]*datax[i]+ u[4] - data[i])**2
        # print(z)

    return 1 - z / tss
def YU(data,u):
    temp = 0
    tss = 0
    z=0
    datax = range(1, len(data) + 1)
    for spot in data:
        temp += spot
    datamean = temp / len(data)
    for spot in data:
        tss += (spot - datamean) ** 2
    for i in range(len(data)):
        z += (u[0] * ((u[1] + datax[i] / u[2]) ** (-u[3])) + u[4] - data[i]) ** 2
        # print(z)
    return 1 - z / tss

def levy(d):
    lamda = 1.5
    sigma = (math.gamma(1 + lamda) * math.sin(math.pi * lamda / 2) / (
        math.gamma((1 + lamda) / 2) * lamda * (2 ** ((lamda - 1) / 2)))) ** (1 / lamda)
    # sigma = 0.6965745025576968
    u = np.random.randn(1, d) * sigma
    v = np.random.randn(1, d)
    step = u / abs(v) ** (1 / lamda)
    return 0.01 * step


def simple(s, lb, ub, d):
    ns_tmp = s
    for i in range(0, d):
        if ns_tmp[i] < lb:
            ns_tmp[i] = lb
        if ns_tmp[i] > ub:
            ns_tmp[i] = ub
    return ns_tmp


def fpa(n, p, N_iter, lb, ub, d, f, datay):
    autop = 0
    if p == -1:
        autop = 1
    sol = np.ones((n, d))
    fitness = np.ones((n, 1))
    for i in range(0, n):
        sol[i,] = lb + (ub - lb) * np.random.rand(1, d)
        fitness[i, 0] = fun(sol[i,], d, f, datay)
    fmin, I = fitness.min(0), fitness.argmin(0)
    best = sol[I,]
    # for i in range(0,n):
    #     sol[i,]=best*np.random.randn(1);
    S = sol.copy()

    for t in range(0, N_iter):
        for i in range(0, n):
            if autop == 1:
                p = 0.8 - 0.7 * t / N_iter
            if np.random.random() < p:
                L = levy(d)
                S[i,] = sol[i,] + L * (sol[i,] - best)
            else:
                epsilon = np.random.random_sample()
                jk = np.random.permutation(n)
                S[i,] = S[i,] + epsilon * (sol[jk[0],] - sol[jk[1],])
            S[i,] = simple(S[i,], lb, ub, d)
            Fnew = fun(S[i,], d, f, datay)
            # if Fnew <= fitness[i]:
            if Fnew >= fitness[i]:
                sol[i,] = S[i,]
                fitness[i] = Fnew
            # if Fnew <= fmin:
            if Fnew >= fmin:
                best = S[i,]
                fmin = Fnew
        # if t % 1 == 0:
        print(t + 1, "\t", fmin)
        # print(best)
        # print(fmin)
        # if fmin < 10 ** -10:
        #     return t
        # elif t==N_iter-1:
        #     return N_iter-1

    print("最优参数：")
    for temp in best:
        print(temp)
    print("拟合优度：")
    print(fmin)
    return best.tolist()


def do(data, para):
    # def do(data):
    # print(int(para[0]),para[1],int(para[2]),para[3],para[4])
    # fpa(50,-1,10,0,50,4,1,data)
    result = fpa(int(para[0]), para[1], int(para[2]), para[3], para[4], 5, 1, data)
    datax = range(1, len(data) + 1)
    plt.scatter(datax, data)
    x=np.linspace(1,len(data)+1,1000)
    y=result[0] * ((result[1] + x/ result[2]) ** (-result[3])) + result[4]
    y2=47 * ((0 + x/ 0.62) ** (-1.317)) +0.41
    plt.plot(x,y)
    plt.plot(x, y2,color='green')
    plt.show()
    print(len(result))
    return result


def func1(x,a,b):
    y = a * log(x)+ b
    return y

def func2(x,a,b,c,d,e):
    y = a*((b+x/c)**(-d))+e
    return y

def polyfit(x, y, degree):
    results = {}
    # coeffs = numpy.polyfit(x, y, degree)
    popt, pcov = curve_fit(func2, x, y)
    results['polynomial'] = popt

    # r-squared
    yhat = func2(x, popt[0], popt[1],popt[2],popt[3],popt[4])  # or [p(z) for z in x]
    ybar = np.sum(y) / len(y)  # or sum(y)/len(y)
    ssreg = np.sum((yhat - ybar) ** 2)  # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = np.sum((y - ybar) ** 2)  # or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot

    return results

def autofit(data,list):
    datax = range(1, len(data) + 1,1)
    z1 = polyfit(datax,data, 2)
    print(z1)
    print("优度：",YU(data,z1['polynomial']))

    z2=[1,2,3,4,5]
    initial_guess = [10., 10., 10., 10., 10.]
    pars, pcov = curve_fit(func2, datax, data, p0=initial_guess)
    alpha = 0.05  # 95% confidence interval = 100*(1-alpha)

    n = len(data)  # number of data points
    p = len(pars)  # number of parameters

    dof = max(0, n - p)  # number of degrees of freedom

    # student-t value for the dof and confidence level
    tval = t.ppf(1.0 - alpha / 2., dof)

    for i, p, var in zip(range(n), pars, np.diag(pcov)):
        sigma = var ** 0.5
        print('p{0}: {1} [{2}  {3} ]'.format(i, p, p - sigma * tval, p + sigma * tval))
    print("优度：", YU(data, pars))
    return z2