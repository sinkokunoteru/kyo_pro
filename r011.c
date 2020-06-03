#include<stdio.h>

int main(void){
	int a,kokugo,shakai,rika;
	int goukei,heikin;

	printf("国語の点数＝");
	scanf("%d",&kokugo);
	printf("社会の点数＝");
	scanf("%d",&shakai);
	printf("理科の点数＝");
	scanf("%d",&rika);
	

	goukei=kokugo+shakai+rika;
	heikin=goukei/3;

	printf("合計＝%d",goukei);
	printf("平均＝%d",heikin);
	scanf("%d",&a);
	return 0;
}