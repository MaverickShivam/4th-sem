#include<stdio.h>
int findit(int array[],int noe,int key)
{
    int i;
    for(i=0;i<noe;i++)
    {
        if(array[i]==key)
        {
            return 1;
        }
    }
    return -1;
}
void main()
{
    int i,n;
    int result[100];
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        int noe;
        int key;
        int array[100];
        int j;
        scanf("%d %d",&noe,&key);
        for(j=0;j<noe;j++)
        {
            scanf("%d",&array[j]);
        }
        result[i]=findit(array,noe,key);
    }
    printf("Output:\n");
    for (i=0;i<n;i++)
    {
        printf("%d\n",result[i]);
    }
}
