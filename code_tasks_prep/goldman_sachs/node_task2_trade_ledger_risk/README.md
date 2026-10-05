# Challenge 2: Trade Ledger & Real-Time Risk Controller

This challenge simulates a trade ledger and real-time risk management engine for an investment banking equities trading desk at Goldman Sachs.

## Problem Description
Implement the controller and route handlers to ingest trade orders, enforce pre-trade risk limits, filter historical trades, and aggregate trader portfolio positions.

### Endpoints

#### 1. `POST /trades`
Record a new trade with validation and risk controls.

**Request Body (JSON):**
```json
{
  "traderId": "T-001",
  "symbol": "GS",
  "side": "BUY",
  "shares": 500,
  "price": 380.5
}
```

**Input Validation Rules (HTTP 400 Bad Request):**
- `traderId`: non-empty string.
- `symbol`: non-empty uppercase string, length between 1 and 5 characters.
- `side`: strictly `'BUY'` or `'SELL'`.
- `shares`: integer strictly > 0 (`shares > 0 && Number.isInteger(shares)`).
- `price`: number strictly > 0 (`price > 0`).
- If any validation rule is violated, respond with HTTP status **`400 Bad Request`**.

**Risk Limits (HTTP 422 Unprocessable Entity):**
1. **Single Transaction Notional Limit:**
   - Single trade value (`shares * price`) cannot exceed `$1,000,000`.
   - If exceeded: return status `422` with JSON `{ "error": "Order value exceeds single transaction limit of 1,000,000" }`.
2. **Trader Net Position Limit per Symbol:**
   - Calculate current net position for this trader and symbol (`sum(BUY shares) - sum(SELL shares)`).
   - Add the proposed new trade.
   - If the resulting net position > `10,000` shares: return status `422` with `{ "error": "Maximum long position limit of 10,000 shares exceeded" }`.
   - If the resulting net position < `-5,000` shares (short): return status `422` with `{ "error": "Maximum short position limit of -5,000 shares exceeded" }`.

**Success:** Save the trade in the database and return HTTP **`201 Created`** with the created trade object.

---

#### 2. `GET /trades`
Retrieve historical trades with optional filtering.

**Query Parameters:**
- `traderId` (optional)
- `symbol` (optional)
- `side` (optional)
- `startDate` & `endDate` (ISO date strings, optional):
  - If only one of the dates is provided (only `startDate` or only `endDate`) $\to$ return **`400 Bad Request`**.
  - If both are provided $\to$ filter `timestamp >= startDate AND timestamp <= endDate`.
- Sorting: by `timestamp` descending (`DESC`).
- Return HTTP **`200 OK`** with array of trades.

---

#### 3. `GET /portfolio/:traderId`
Aggregate open positions for a given trader.

**Path Parameter:** `traderId`

**Logic:**
- Group all trades for this `traderId` by `symbol`.
- For each symbol, compute `netShares = sum(BUY shares) - sum(SELL shares)`.
- Return HTTP **`200 OK`**:
```json
{
  "traderId": "T-001",
  "positions": [
    { "symbol": "AAPL", "netShares": 300 },
    { "symbol": "GS", "netShares": 500 }
  ]
}
```
- If the trader has no trades, return `{ "traderId": "...", "positions": [] }`.

---

### Files to Edit
- [controllers/trades.js](file:///Users/arseniizarudniuk/test/code_tasks_prep/goldman_sachs/node_task2_trade_ledger_risk/controllers/trades.js)
- [routes/trades.js](file:///Users/arseniizarudniuk/test/code_tasks_prep/goldman_sachs/node_task2_trade_ledger_risk/routes/trades.js)

### Running Tests
```bash
python3 run_tests.py
# or
npm test
```
