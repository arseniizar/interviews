# Goldman Sachs Challenge 1: Account Transaction Ledger API

## Mission Overview
You are tasked with fixing and completing the **Account Transaction Ledger REST API** for Goldman Sachs.
Currently, several endpoints are either returning incorrect HTTP status codes or missing core business logic.

---

## Your Objectives

### 1. Fix `AccountController.java`
* `POST /api/accounts`:
  - When creating a valid account, it currently returns `200 OK`.
  - **Requirement:** Must return `201 CREATED` with the created `Account` body.

### 2. Implement `AccountService.java` -> `transfer(...)`
Implement the money transfer method:
```java
public synchronized TransferResponse transfer(TransferRequest request)
```
Business rules:
1. **Same Account Check:**
   - If `fromAccountId.equals(toAccountId)`, throw `new InvalidTransferException("Cannot transfer to the same account")`.
   - Resulting HTTP Status: `400 BAD REQUEST`.
2. **Account Existence Check:**
   - Both `fromAccountId` and `toAccountId` must exist in `repository`.
   - If either is missing, throw `new AccountNotFoundException("Account not found: " + missingId)`.
   - Resulting HTTP Status: `404 NOT FOUND`.
3. **Sufficient Funds Check:**
   - `fromAccount.getBalance()` must be greater than or equal to `request.getAmount()`.
   - Use `balance.compareTo(amount) < 0` for `BigDecimal`.
   - If insufficient, throw `new InsufficientFundsException("Insufficient funds")`.
   - Resulting HTTP Status: `400 BAD REQUEST`.
4. **Execute Transfer:**
   - Deduct `amount` from `fromAccount`: `fromAccount.setBalance(fromAccount.getBalance().subtract(amount))`.
   - Add `amount` to `toAccount`: `toAccount.setBalance(toAccount.getBalance().add(amount))`.
   - Save both accounts via `repository.save(...)`.
5. **Return Response:**
   - Return a `TransferResponse` with:
     - `fromAccountId`
     - `toAccountId`
     - `transferredAmount`
     - `fromAccountBalance`
     - `toAccountBalance`
     - `status = "SUCCESS"`

---

## How to Test Your Code
Open your terminal in this directory and run:
```bash
mvn clean test
```
Currently: **6 tests failing**.
Your goal: **11/11 tests passing (BUILD SUCCESS)**!
