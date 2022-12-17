class Solution {
    public int[] solution(int[] array) {
        int[] answer = new int[2];
        
        int maxIndex = 0;
        int maxNum = 0;
        
        for (int i = 1; i < array.length; i++) {
            if (maxNum < array[i]) {
                maxIndex = i;
                maxNum = array[i];
            }
            
        }
        
        answer[0] = maxNum;
        answer[1] = maxIndex;
        
        return answer;
    }
}