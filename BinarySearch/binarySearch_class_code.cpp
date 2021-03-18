#include<iostream.h>
#include<conio.h>
int bsiterative(int arr[], int item, int size)
{
    int low = 0, high = size-1, mid;
    while(low<=high)
    {
	mid = (low+high)/2;
	if(item<arr[mid])
	{
	    high = mid-1;
	}
	else if (item>arr[mid])
	{
	    low = mid+1;
	}
	else
	{
	    return mid;
	}
    }
    return 0;
}
int bsrecursive(int arr[], int low, int high, int item)
{
    int mid;
    if(low==high)
    {
	if(item==arr[low])
	{
	    return low;
	}
	else
	{
	    return 0;
	}
    }
    else
    {
	mid = (low+high)/2;
	if(item==arr[mid])
	{
	    return mid;
	}
	else if(item<arr[mid])
	{
	    return bsrecursive(arr,low, mid-1, item);
	}
	else
	{
	    return bsrecursive(arr, mid+1, high, item);
	}
    }
}
int bsonethird(int arr[], int low, int high, int item)
{
    int mid;
    if(low==high)
    {
	if(item==arr[low])
	{
	    return low;
	}
	else
	{
	    return 0;
	}
    }
    else
    {
	mid = (low+high)/3;
	if(item==arr[mid])
	{
	    return mid;
	}
	else if(item<arr[mid])
	{
	    return bsonethird(arr,low, mid-1, item);
	}
	else
	{
	    return bsonethird(arr, mid+1, high, item);
	}
    }
}

int main()
{
    int arr[10], size=10, item, n;

    cout<<"\nEnter 10 Elements: ";
    for(int i=0; i<size; i++)
    {
	cin>>arr[i];
    }
    cout<<"Enter element to search: ";
    cin>>item;
    cout<<"\nEnter choice:\n1.Binary search iterative\n2.Binary search recursive\n3.Binary One-Third\nChoice: ";
    cin>>n;
    switch(n)
    {
	case 1:
	     cout<<bsiterative(arr, item, size);
	     break;
	case 2:
	     cout<<bsrecursive(arr, 0, size-1, item);
	     break;
	case 3:
	     cout<<bsonethird(arr, 0, size-1, item);
	     break;
	default:
	     cout<<"Invalid Option"<<endl;
    }
    getch();
    return 0;
}
