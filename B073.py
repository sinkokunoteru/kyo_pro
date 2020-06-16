#B073

tmp=list(map(int,input().split()))
tree_count=tmp[0]
judge=tmp[1]
first_tree_lights=list(map(int,input().split()))
Q=int(input())

def cul_average(A_range,first_tree):
    ave=0
    for i in range(A_range[0],A_range[1]+1):
        ave=ave+first_tree[i-1]
    ave=int(ave/(A_range[1]-A_range[0]+1))
    return ave
    
def judge_anzen(M,ave):
    judge=True
    if M<=ave:
        judge=True
    else:
        judge=False
        
    return judge
    
def plus_lights(tree_light,A_range):
    for i in range(A_range[0]-1,A_range[1]):
        tree_light[i]=tree_light[i]+1

def main():
    for i in range(Q):
        where=list(map(int,input().split()))
        average=cul_average(where,first_tree_lights)
        while judge_anzen(judge,average)==False:
            plus_lights(first_tree_lights,where)
            average=cul_average(where,first_tree_lights)

    print(' '.join(map(str,first_tree_lights)))

if __name__ == "__main__":
    main()
    
    
    
