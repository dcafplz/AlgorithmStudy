import java.io.*;
import java.util.Arrays;
import java.util.stream.*;

public class Main {
	
	static int lowerBound(int list[], int key)
	{
		int left = 0;
		int right = list.length;
		while(left < right)
		{
			int mid = (left + right) / 2;

			if(list[mid] >= key)
				right = mid;
			else
				left = mid + 1;
		}
		return left;
	}

	static int upperBound(int list[], int key)
	{
		int left = 0;
		int right = list.length;
		while(left < right)
		{
			int mid = (left + right) / 2;

			if(list[mid] <= key)
				left = mid + 1;
			else
				right = mid;
		}
		return left;
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		br.readLine();
		int[] have = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		int[] answer = new int[Integer.parseInt(br.readLine())];
		int[] search =  Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		Arrays.sort(have);
		for (int i = 0; i < search.length; i++) {
			answer[i] += upperBound(have,search[i]) - lowerBound(have,search[i]);
		}
		StringBuilder sb = new StringBuilder();
		for(int i: answer) {
			sb.append(i + " ");
		}
		System.out.println(sb.toString().substring(0,sb.toString().length()-1));
	}
}