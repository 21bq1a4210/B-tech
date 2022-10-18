class Test{
	public static int getCount(int arr[], int n) { 
		int count1 = 0; 
		int count2 = 0;
		int index;
		for (int index1 = 0; index1 < n - 1; index1++) 
			for (int index2 = index1 + 1; index2 < n; index2++) 
				if (arr[index1] > arr[index2]) 
					count1++; 
				else {
					index=index2;
					count2=0;
					while(index>index1) {
						count2++;
						index--;
					}
				}
		return Math.max(count1, count2); 
	};
	
	public static void main(String[] args) {
		int arr[]={1,2,3,4,5};
		System.out.println(getCount(arr,arr.length));
		
	};
}

