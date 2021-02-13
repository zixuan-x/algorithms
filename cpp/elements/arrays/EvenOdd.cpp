#include <iostream>
#include <vector>
using namespace std;

/** Given an array of integers, reorder its entries so that 
 *  the even entries appear first.
 */
 
void EvenOdd(vector<int>* A_ptr) {
    vector<int>& A = *A_ptr;
    int next_even = 0, next_odd = A.size() - 1;
    while (next_even < next_odd) {
        if (A[next_even] % 2 == 0) {
            next_even++;
        } else {
            swap(A[next_even], A[next_odd--]);
        }
    }
}

int main() {
    vector<int> A{1, 2, 3, 4, 5, 6, 7, 8};
    cout << "Before reordering: "; 
    for (auto num: A) cout << num << " ";
    cout << endl;

    EvenOdd(&A);
    cout << "After reordering: "; 
    for (auto num: A) cout << num << " ";
    cout << endl;
}