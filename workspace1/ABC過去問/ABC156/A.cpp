#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,r;
    cin >> n >> r;
    int ans = 0;
    if(n > 10){
        ans = r;
    }else{
        ans = 100*(10-n) + r;
    }
    cout << ans << endl;
}