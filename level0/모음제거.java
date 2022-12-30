class Solution {
    public String solution(String my_string) {
        String[] alphas = new String[]{"a", "e", "i", "o", "u"};
        for (String alpha : alphas) {
            my_string = my_string.replace(alpha, "");
        }
        
        return my_string;
    }
}