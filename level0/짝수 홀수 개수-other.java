import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[2];
        int oddNum = (int) Arrays.stream(num_list).filter(num -> num % 2 == 1).count();
        int evenNum = (int)Arrays.stream(num_list).filter(num -> num % 2 == 0).count();
        
        answer[0] = evenNum;
        answer[1] = oddNum;
        return answer;
    }
}