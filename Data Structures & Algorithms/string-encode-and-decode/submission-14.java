class Solution {

    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();
        for (String str: strs){
            encoded.append(str.length()).append("#").append(str);
        }
        return encoded.toString();
    }
public List<String> decode(String str) {
    List<String> list = new ArrayList<>();
    int i = 0;
    while (i < str.length()) {
        // Find the position of the '#'
        int j = str.indexOf('#', i);
        // Parse the length before the '#'
        int length = Integer.parseInt(str.substring(i, j));
        // Get the substring that represents the original string
        i = j + 1 + length;
        list.add(str.substring(j + 1, i));
    }
    return list;
}
}
