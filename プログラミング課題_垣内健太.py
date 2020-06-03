def money_or_ic():
    print('現金なら0、電子マネーなら１を入力してください')
    x=int(input())
    if x==0:
        return True
    if x==1:
        return False

def input_money_print():
    
    print('現金を投入\n'
          '10円なら0\n'
          '50円なら1\n'
          '100円なら2\n'
          '500円なら3\n'
          '1000円なら4\n'
          '5000円なら5\n'
          '10000円なら6\n'
          '投入終了は9を入力\n')

def input_money(money_count,money_sum):
    x=0
    while x!=9:
        x=int(input())
        if x<=6 and x>=0 or x==9:
            if x==9:
                break

            if money_sum[x]<=0:
                print('所持金がたりません')
            if x<=6 and x>=0:
                money_count[x]=money_count[x]+1
                money_sum[x]=money_sum[x]-1
        else:
            print('該当しない数字です')
            
def caluculate_money_sum(money_define,money_count):
    money_sum=0
    for i in range(len(money_define)):
        money_sum=money_sum+money_count[i]*money_define[i]
    print('投入金額',money_sum)
    return money_sum    

def pay_money(total_change):
    if total_change<130:
        print('投入金額が足りません')
    else:    
        total_change=total_change-130
    return total_change
    
def calculate_change(total_change,money_define,money_change,money_sum):
    tmp=0
    for i in range(6,0,-1):
        tmp=total_change//money_define[i]
        money_change[i]=tmp
        money_sum[i]=money_sum[i]+tmp
        total_change=total_change%money_define[i]
        
def print_money_change(money_sum,money_define):
    print('釣り銭受領後の所持金 ')
    for i in range(len(money_sum)):
        print(money_define[i],'円  ',money_sum[i],'枚')
        
def ic_result(ic):
    if ic<124:
        print('引き去り失敗')
        print('引き去り額',0,'円')
        print('残高 ',ic,'円')
    else:
        ic=ic-124
        print('引き去り成功')
        print('引き去り額',124,'円')
        print('残高 ',ic,'円')
    return ic
    
def define_ic():
    ic=1000
    return ic
    
    
    
def main():
    MoneyDefine=[10,50,100,500,1000,5000,10000]
    MoneyCount=[0,0,0,0,0,0,0]
    MoneySum=[15,3,2,1,1,1,1]
    MoneyChange=[0,0,0,0,0,0,0]
    
    m_or_ic=money_or_ic()
    
    if m_or_ic==True: #現金の処理
        input_money_print()
        input_money(MoneyCount,MoneySum)
        TotalChange=caluculate_money_sum(MoneyDefine,MoneyCount)
        TotalChange=pay_money(TotalChange)
        calculate_change(TotalChange,MoneyDefine,MoneyChange,MoneySum)
        print_money_change(MoneySum,MoneyDefine)
        
    elif m_or_ic==False: #電子マネーの処理
        IC=define_ic()
        IC=ic_result(IC)
        
        
        
if __name__ =="__main__":
    main()