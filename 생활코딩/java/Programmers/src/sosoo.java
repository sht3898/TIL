
public class sosoo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 10;
		int answer = 0;
        for (int i=2; i<=n; i++){
        	boolean chk = true;
        	for (int j=2; j*j <= i;j++) {
        		if (i % j == 0) {
        			chk = false;
        			break;
        		}
        	}
        	if(chk) {
        		answer++;
        	}
        }
        System.out.println(answer);
	}

}
