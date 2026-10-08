def calc_NPV(c0, ct, r, t):
    sum_ct=0
    i=1
    while i<=t:
        sum_ct+=ct/(1+r/100)**i
        i+=1
    nvp=sum_ct - c0
    return nvp

def is_investment(NPV):
    if NPV > 0:
        print("the project can be invested")
        return("the project can be invested")
    elif NPV < 0:
        print  ("the project absolutely could not invested")
        return("the project absolutely could not invested")
    else:
        print("it depends on your company plan")
        return("it depends on your company plan")
