#include<stdio.h>
#include<conio.h>
	int main(void){
	int tanka,suryo,kingaku,zeikomi;

	scanf("%d",&tanka);
	scanf("%d",&suryo);

	kingaku=tanka*suryo;

	zeikomi=kingaku*105/100;
	printf("%d\n\n%d",kingaku,zeikomi); 
	getch();
	return 0;
}	