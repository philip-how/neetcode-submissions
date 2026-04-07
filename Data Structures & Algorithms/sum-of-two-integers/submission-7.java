class Solution {
    public int getSum(int a, int b) {
        int base = a ^ b;
        int carry = (a & b) << 1;
        while (carry != 0) {
            int stored_base = base;
            base = base ^ carry;
            carry = (stored_base & carry) << 1;
        }

        return base;
    }
}
