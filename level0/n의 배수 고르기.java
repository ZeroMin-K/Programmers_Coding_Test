
class Solution {
    public int[] solution(int n, int[] numlist) {
        
        int len = 0;
        for (int number : numlist) {
            if (number % n == 0) {
                len++;
            }
        }
        
        int[] answer = new int[len];
        int i = 0; 
        for (int number : numlist) {
            if (number % n == 0) {
                answer[i++] = number;
            }
        }
        
        return answer;
    }
}