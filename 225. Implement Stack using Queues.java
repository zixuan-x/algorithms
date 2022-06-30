package leetcode.Queue;

import java.util.Queue;
import java.util.LinkedList;

// 只用一个queue
class MyStack {

    /** offer, poll, peek, isEmpty */
    Queue<Integer> queue;
    
    /** Initialize your data structure here. */
    public MyStack() {
        this.queue = new LinkedList<>();
    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        this.queue.offer(x);
        int size = queue.size();
        for (int i = 0; i < size - 1; i++) {
            queue.offer(queue.poll());
        }
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        if (empty()) {
            return -1;
        }
        return this.queue.poll();
    }
    
    /** Get the top element. */
    public int top() {
        if (empty()) {
            return -1;
        }
        return this.queue.peek();
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        return this.queue.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */