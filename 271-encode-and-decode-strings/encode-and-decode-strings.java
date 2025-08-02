public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        String res = "";
        for (String s : strs) {
            res += s.length() + "#" + s;
        }

        return res;
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        int l = 0;
        List<String> res = new ArrayList<>();
        while (l < s.length()) {
            int r = l;
            while (s.charAt(r) != '#') {
                r += 1;
            }

            int length = Integer.parseInt(s.substring(l, r));
            int start = r + 1;
            res.add(s.substring(start, start + length));

            l = start + length;
        }

        return res;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));