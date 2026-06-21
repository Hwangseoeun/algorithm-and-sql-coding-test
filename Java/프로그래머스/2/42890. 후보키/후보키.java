import java.util.*;

class Solution {
    private List<List<Integer>> candidates = new ArrayList<>();
    private List<List<Integer>> allCombinations = new ArrayList<>();
    
    public int solution(String[][] relation) {
        getCombinations(0, relation[0].length, new ArrayList<>());
        
        Collections.sort(allCombinations, (o1, o2) -> o1.size() - o2.size());
        
        for (List<Integer> comb : allCombinations) {
            boolean isMinimal = true;
            for (List<Integer> candidate : candidates) {
                if (comb.containsAll(candidate)) {
                    isMinimal = false;
                    break;
                }
            }
            
            if (!isMinimal) {
                continue;
            }
            
            if (checkUniqueness(relation, comb)) {
                candidates.add(comb);
            }
        }
        
        return candidates.size();
    }
    
    private void getCombinations(int start, int totalCols, List<Integer> selectedCols) {
        if (!selectedCols.isEmpty()) {
            allCombinations.add(new ArrayList<>(selectedCols));
        }
        
        for (int i = start; i < totalCols; i++) {
            selectedCols.add(i);
            getCombinations(i + 1, totalCols, selectedCols);
            selectedCols.remove(selectedCols.size() - 1);
        }
    }
    
    private boolean checkUniqueness(String[][] relation, List<Integer> comb) {
        Map<Integer, List<String>> map = new HashMap<>();
        
        for (int i=0; i<relation.length; i++) {
            map.put(i, new ArrayList<>());
        }
        
        for (int i=0; i<relation.length; i++) {
            for (int c : comb) {
                map.get(i).add(relation[i][c]);
            }
        }
        
        Collection<List<String>> values = map.values();
        Set<List<String>> set = new HashSet<>(values);
        
        if (set.size() == relation.length) {
            return true;
        }
        
        return false;
    }
}