class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size() , m = grid[0].size();
        vector<vector<int>> vis(n+1 , vector<int>(m+1 , 0));
        vector<int> dx = {1 , -1 , 0 , 0} , dy = {0 , 0, -1 , 1};
        auto dfs = [&](int i , int j , auto &&self) -> void{
            vis[i][j] = 1;
            // cout<<i<<" "<<j<<endl;
            for(int k = 0 ; k<4 ; k++){
                int x = dx[k] + i , y = dy[k] + j;
                if(x >= 0 && y >= 0 && x < n && y < m && (grid[x][y] == '1') && (0 == vis[x][y])) 
                    self(x , y , self);
            }
        };
        int count = 0;
        for(int i = 0 ; i<n ; i++){
            for(int j = 0 ; j<m ; j++){
                if(grid[i][j] == '1' && !vis[i][j]){
                    dfs(i , j , dfs);
                    count++;
                }
            }
        }
        return count;
    }
};
