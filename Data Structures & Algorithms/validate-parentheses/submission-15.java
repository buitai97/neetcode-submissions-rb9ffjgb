class Solution {
    public boolean isValid(String s) {
        Stack<Character> brackets = new Stack<>();

        for (char c : s.toCharArray()){
            if (c == '[' || c == '(' || c == '{'){
                brackets.push(c);
            }
            else {
                if (!brackets.isEmpty()){
                    if (c == ']' && '[' == brackets.peek()){
                        brackets.pop();
                    }
                    else if (c == '}' && '{' == brackets.peek()){
                        brackets.pop();
                    }
                    else if (c == ')' && '(' == brackets.peek()){
                        brackets.pop();
                    }
                    else {
                        return false;
                    }
                }
                else {
                        return false;
                    }
               
            }
        }
        return brackets.isEmpty();
    }
}
