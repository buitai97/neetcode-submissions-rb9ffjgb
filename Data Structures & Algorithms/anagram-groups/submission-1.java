class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();

        for (String str: strs){
            char[] strArr = str.toCharArray();
            Arrays.sort(strArr);
            String key = Arrays.toString(strArr);
            res.putIfAbsent(key, new ArrayList<>());
            res.get(key).add(str);
        }
        return new ArrayList<>(res.values());
    }
}
