#include <iostream>
#include <map>
#include <list>
#include <queue>

using namespace std;

class graph{
public:
    map<int,list<int>> adjlist;
    map<int,bool> visited;
    queue<int> q;

    void addedge(int start , int end){
        adjlist[start].push_back(end);
        adjlist[end].push_back(start);
    }

    void dfs(int a){

        visited[a]=true;
        cout<<a<<" ";
        for(int i : adjlist[a]){
            if(!visited[i]){
                dfs(i);
            }
        }
    }

    void bfs(){
        if(q.empty()){
            return;
        }
        int n =q.front();
        q.pop();
        cout<<n<<" ";
        for(int i : adjlist[n]){
            if(!visited[i]){
                q.push(i);
            }
        }
    dfs(0);
    }
};


int main(){
    graph g;

    int n,e;

    cout<<"enter number of nodes:";
    cin>>n;
    cout<<"enter number of edges";
    cin>>e;

    for(int i =0;i<e;i++){
        int u,v;
        cout<<"enter edge ";
        cin>>u;
        cin>>v;
        g.addedge(u,v);
    }
    g.dfs(0);

}
