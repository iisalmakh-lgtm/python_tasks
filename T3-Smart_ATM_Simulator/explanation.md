# Smart ATM Simulator

## Description
This program simulates a simple ATM system. It verifies the user's PIN before allowing access to banking operations. After successful authentication, the user can either check their balance or withdraw money.

## Features
- PIN verification
- Check account balance
- Withdraw money
- Balance validation before withdrawal

## Program Logic
1. The user enters their PIN.
2. If the PIN is incorrect, the transaction is rejected.
3. If the PIN is correct, the user chooses an operation:
   - Withdraw money
   - Check balance
4. For withdrawals, the program checks whether the balance is sufficient before completing the transaction.

## Skills Used
- Variables
- User Input
- if / elif / else
- Nested if
- Arithmetic Operations
- String Methods (`strip()` and `lower()`)
