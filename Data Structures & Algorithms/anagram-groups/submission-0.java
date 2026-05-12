class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        int[] seenLetters;
        for(String s: strs) {
            seenLetters = new int[26];

            for(char c : s.toCharArray()) {
                seenLetters[c - 'a']++;
            }
            map.putIfAbsent(Arrays.toString(seenLetters), new ArrayList<>());
            map.get(Arrays.toString(seenLetters)).add(s);
        }    
        return new ArrayList<>(map.values());
    }
}
