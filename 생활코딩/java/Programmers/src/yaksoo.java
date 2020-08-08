import java.util.Scanner;

public class yaksoo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int answer = 0;
		for (int i=1; i<=n; i++){
			if (n % i == 0){
				answer += i;
			}
		}
		System.out.println(answer);
		sc.close();
	}

}
