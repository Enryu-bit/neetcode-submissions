class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<string> temp;
        vector<vector<string>> ans;
        vector<vector<int>> vis(n , vector<int>(n , 0));
        vector<int> colcheck(n , 0);

        auto leftcheck = [&](int i , int j , auto &&self) -> bool{
            if(i < 0 || j < 0)return true;
            if(vis[i][j] == 1)return false;
            return self(i - 1 , j - 1 , self);
        };
        auto rightcheck = [&](int i , int j , auto &&self) -> bool{
            if(i < 0 || j > n-1)return true;
            if(vis[i][j] == 1)return false;
            return self(i - 1 , j + 1, self);
        };

        auto helper = [&](int i , auto &&self) -> void{
            if(i == n){
                ans.push_back(temp);
                return;
            }
            for(int j = 0; j<n ; j++){
                if(vis[i][j] == 0 && colcheck[j] == 0 && leftcheck(i , j , leftcheck) && rightcheck(i , j , rightcheck)){
                    vis[i][j] = 1;
                    colcheck[j] = 1;
                    temp.push_back(string(j , '.') + 'Q' + string(n - (j+1) , '.'));
                    self(i + 1 , self);
                    colcheck[j] = 0;
                    temp.pop_back();
                    vis[i][j] = 0;
                }
            }
        };
        helper(0 , helper);
        return ans;
    }
};
