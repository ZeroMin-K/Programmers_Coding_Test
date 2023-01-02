import java.util.*;

class Solution {
    public int[] solution(String my_string) {
        List<String> list = new ArrayList<>();
        
        for(int i = 0; i < my_string.length(); i++) {
            char now = my_string.charAt(i);
            
            if (Character.isDigit(now)) {
                String currentString = String.valueOf(now);
                list.add(currentString);
            }
        }
        return list.stream()
            .sorted()
            .mapToInt(Integer::parseInt)
            .toArray();
    }
}