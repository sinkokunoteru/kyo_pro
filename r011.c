#include<stdio.h>

int main(void){
	int a,kokugo,shakai,rika;
	int goukei,heikin;

	printf("����̓_����");
	scanf("%d",&kokugo);
	printf("�Љ�̓_����");
	scanf("%d",&shakai);
	printf("���Ȃ̓_����");
	scanf("%d",&rika);
	

	goukei=kokugo+shakai+rika;
	heikin=goukei/3;

	printf("���v��%d",goukei);
	printf("���ρ�%d",heikin);
	scanf("%d",&a);
	return 0;
}