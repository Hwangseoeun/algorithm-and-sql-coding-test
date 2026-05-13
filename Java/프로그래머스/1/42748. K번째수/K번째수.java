import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> answer = new ArrayList<>();
        
        for(int c = 0; c < commands.length; c++) {
            int i = commands[c][0];
            int j = commands[c][1];
            int k = commands[c][2];
                
            List<Integer> arr = new ArrayList<Integer>();
            
            for(int n = i-1; n < j; n++) {
                arr.add(array[n]);
            }
            
            Collections.sort(arr);
            
            answer.add(arr.get(k-1));
        }
        
        int[] arrAnswer = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            arrAnswer[i] = answer.get(i);
        }
        
        return arrAnswer;
    }
}