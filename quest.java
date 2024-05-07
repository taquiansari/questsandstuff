class quest{
    public static void main(String[] args) {
        int[] arr = {0,-1,42,-3,1};
        int x = -2;
        int check = 0;
        for(int i=0; i<5 && check ==0; i++){
            for(int j=0; j<5 && check ==0; j++){
                if(i!=j && arr[i]+arr[j]==x){
                    check++;
                }    
            }  
        }
        System.out.println((check == 1) ? "Exists" : "Does Not Exist");
    }
}