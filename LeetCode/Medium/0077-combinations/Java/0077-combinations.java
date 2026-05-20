class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> answer = new ArrayList<>();

        for(int i=1; i<=n; i++) {
            List<Integer> com = new ArrayList<>();
            com.add(i);
            combination(answer, com, n, k, i);
            com.remove(com.size() - 1);
        }

        return answer;
    }

    private void combination(List<List<Integer>> answer, List<Integer> com, int n, int k, int num) {
        if(com.size() == k) {
            answer.add(new ArrayList<>(com));
            return;
        }

        for(int i=num+1; i<=n; i++) {
            com.add(i);

            combination(answer, com, n, k, i);

            com.remove(com.size() - 1);
        }
    }
}