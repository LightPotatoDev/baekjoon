#include <iostream>
#include <vector>
using namespace std;

void continue_num(int n, int i, vector<int> *v);
void print_vector(vector<int> *v);

int main(){
    int n;
    cin >> n;
    vector<int> seq;
    for (int i=0; i<=n; i++){
        continue_num(n,i,&seq);
    }

    cout << seq.size() << endl;
    print_vector(&seq);

    return 0;
}

void continue_num(int n, int i, vector<int> *v){
    vector<int> seq;
    seq.push_back(n);
    seq.push_back(i);
    while (true){
        int a = seq[seq.size()-2];
        int b = seq[seq.size()-1];
        if (a-b >= 0){
            seq.push_back(a-b);
        }
        else{
            break;
        }
    }
    if (seq.size() > v->size())
        *v = seq;
}

void print_vector(vector<int> *v){
    for (int i=0; i<v->size(); i++){
        cout << (*v)[i] << ' ';
    }
    cout << endl;
}
