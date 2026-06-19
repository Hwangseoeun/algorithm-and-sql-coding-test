import java.util.*;

class Solution {
    private List<List<String>> results = new ArrayList<>();

    public List<List<String>> partition(String s) {
        
        bactracking(s, 0, new ArrayList<>());

        return results;
    }

    private void bactracking(String s, int start, List<String> current) {
        if (start == s.length()) {
            results.add(new ArrayList<>(current));
        }

        for (int i=start; i<s.length(); i++) {
            String chars = s.substring(start, i+1);

            StringBuilder sb = new StringBuilder(chars);
            
            if (chars.equals(sb.reverse().toString())) {
                current.add(chars);
                bactracking(s, start + chars.length(), current);
                current.remove(current.size() - 1);
            }
        }
    }
}

