/* Dutch national flag partitioning: [less than, equal to, greater than] */
#include <iostream>
#include <vector>
using namespace std;

/** 
 * 4. [bottom, middle, unclassified, top]
 * time: O(n) - one passes
 * space: O(1)
 */
void DutchFlagPartition(int pivot_index, vector<int>* A_ptr) {
    vector<int>& A = *A_ptr;
    int pivot = A[pivot_index];
    /**
     * Keep the following invariants during partitioning:
     * bottom group: A[0 : smaller - 1]
     * middle group: A[smaller : equal - 1]
     * unclassified group: A[equal : larger - 1]
     * top group: A[larger : A.size() - 1]
     */
    int smaller = 0, equal = 0, larger = A.size();
    // Keep iterating as long as there is an unclassified element
    while (equal < larger) {
        // A[equal] is the incoming unclassified element
        if (A[equal] < pivot) {
            swap(A[smaller++], A[equal++]);
        } else if (A[equal] == pivot) {
            equal++;
        } else { // A[equal] > pivot
            swap(A[equal], A[--larger]);
        }
    }
}

/** 
 * 3. put all smaller elements at the front, then
 *    put all larger elements at the back.
 * time: O(n) - two passes
 * space: O(1)
 */
void DutchFlagPartition3(int pivot_index, vector<int>* A_ptr) {
    vector<int>& A = *A_ptr;
    int pivot = A[pivot_index];
    // First pass: group elements smaller than pivot.
    int smaller = 0;
    for (int i = 0; i < A.size(); i++) {
        if (A[i] < pivot) {
            swap(A[i], A[smaller++]);
        }
    }
    // Second pass: group elements larger than pivot.
    int larger = A.size() - 1;
    for (int i = A.size() - 1; i >= 0 && A[i] >= pivot; i--) {
        if (A[i] > pivot) {
            swap(A[i], A[larger--]);
        }
    }
}

/** 2. put all smaller elements at the front, then
 *     put all larger elements at the back.
 *  time: O(n ^ 2)
 *  space: O(1)
 */
void DutchFlagPartition2(int pivot_index, vector<int>* A_ptr) {
    vector<int>& A = *A_ptr;
    int pivot = A[pivot_index];
    // First pass: group elements smaller than pivot.
    for (int i = 0; i < A.size(); i++) {
        // Look for a smaller element.
        for (int j = i + 1; j < A.size(); j++) {
            if (A[j] < pivot) {
                swap(A[i], A[j]);
                break;
            }
        }
    }
    // Second pass: group elements larger than pivot.
    for (int i = A.size() - 1; i >= 0 && A[i] >= pivot; i--) {
        // Look for a larger element. Stop when we reach an element less
        // than pivot, since frist pass has moved them to the start of A.
        for (int j = i - 1; j >= 0 && A[j] >= pivot; j--) {
            swap(A[i], A[j]);
            break;
        }
    } 
}

/** 1. use three lists
 *  time: O(n) - 2 passes
 *  space: O(n)
 */

int main() {
    vector<int> A = {0, 1, 2, 0, 1, 2, 0, 1, 2};
    cout << "Before partitioning: "; 
    for (auto num: A) cout << num << " ";
    cout << endl;

    DutchFlagPartition(1, &A);
    cout << "After partitioning: "; 
    for (auto num: A) cout << num << " ";
    cout << endl;
}