class TimeMap {
    private Map<String, List<String[]>> store;

    public TimeMap() {
        store = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        store.putIfAbsent(key, new ArrayList<>());
        store.get(key).add(new String[]{value, String.valueOf(timestamp)});
    }
    
    public String get(String key, int timestamp) {
        List<String[]> values = store.getOrDefault(key, new ArrayList<>());
        String res = "";
        int l = 0, r = values.size() - 1;

        while (l <= r) {
            int m = (l + r) / 2;
            int ts = Integer.parseInt(values.get(m)[1]);
            if (ts <= timestamp) {
                res = values.get(m)[0];
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return res;
    }
}