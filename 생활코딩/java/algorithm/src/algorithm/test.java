package algorithm;

import java.util.*;

public class test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList<Integer> arr = new ArrayList<Integer>();
		Queue<Integer> q = new LinkedList<Integer>();
		Stack<Integer> s = new Stack<Integer>();
		Scanner sc = new Scanner(System.in);
		char abc = 'a';
//		String s = "My name is ";
		System.out.println(abc);
		System.out.println(s);
		for(int i=0; i<10; i++) {
			arr.add(i);
			q.add(i);
		}
		System.out.println(arr);
		System.out.println(q.poll());
		sc.close();
	}

}
