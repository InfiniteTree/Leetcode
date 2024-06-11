class Solution {
    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        List<Integer>[] g = new ArrayList[n];
        Arrays.setAll(g, x -> new ArrayList<>());
        for (int[] e: edges){
            g[e[1]].add(e[0]);
        }
        //System.out.print(Arrays.asList(g));
        List<Integer> [] ans = new ArrayList[n];
        Arrays.setAll(ans, x -> new ArrayList<>());
        boolean[] vis = new boolean[n];
        for (int i = 0; i < n; i++){
            Arrays.fill(vis, false);
            dfs(i, g, vis);
            vis[i] = false;
            for (int j = 0; j < n; j++){
                if (vis[j]){
                    ans[i].add(j);
                }
            }
        }

        return Arrays.asList(ans);
    }

    private void dfs(int x, List<Integer>[] g, boolean[] vis){
        vis[x] = true; // Avoid visiting repeatedly
        for (int y: g[x]){
            if (!vis[y]){
                dfs(y, g, vis);
            }
        }
    }
}