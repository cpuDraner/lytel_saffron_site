//**************************************************************
// Jacob C.T. Schaner
// Program #4
// Due 9/18/2025
// A class IntegerSet, which is an array of n bool values repres
// -senting integers 0 thru n
//**************************************************************

#include <iostream>
#include <cstring>
using namespace std;

class IntegerSet{
    public:
        bool a;
        IntegerSet(int n);
        IntegerSet(const IntegerSet&);
};

IntegerSet::IntegerSet(int n=4){
    bool a[n+1];
    for(int i=0;i<n;i++)
      a[i]=false;
};

IntegerSet::IntegerSet(const IntegerSet&){

};



int main(){
    IntegerSet a(5);
    cout << a.a[0] << endl;
    return 0;
}