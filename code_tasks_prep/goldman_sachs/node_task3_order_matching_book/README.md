# Challenge 3: Limit Order Book & Matching Engine

This challenge simulates an electronic order matching engine and limit order book (LOB) utilized across Goldman Sachs algorithmic execution and market-making desks. It tests state machines, queue matching algorithms (Price-Time Priority), and aggregated depth calculations.

## Problem Description
Implement the trading engine to accept limit orders (`BUY` / `SELL`), match them against existing orders on the book, update the order lifecycle state machine, and expose real-time aggregated market depth.

### Order Model (`Order`):
- `id`: integer (auto-increment primary key)
- `symbol`: string (e.g., `"GS"`, `"AAPL"`)
- `side`: `'BUY'` or `'SELL'`
- `price`: float (unit share price)
- `quantity`: integer (original order size)
- `remainingQuantity`: integer (unfilled quantity)
- `status`: `'OPEN'`, `'PARTIALLY_FILLED'`, `'FILLED'`, `'CANCELLED'`
- `createdAt`: Date / timestamp

---

### Endpoints

#### 1. `POST /orders`
Create and match a new limit order against the book.

**Request Body (JSON):**
```json
{
  "symbol": "GS",
  "side": "BUY",
  "price": 350.0,
  "quantity": 100
}
```

**Validation (HTTP 400 Bad Request):**
- `symbol`: non-empty string in uppercase (1-5 characters).
- `side`: strictly `'BUY'` or `'SELL'`.
- `price`: number strictly > 0 (`price > 0`).
- `quantity`: integer strictly > 0 (`quantity > 0 && Number.isInteger(quantity)`).

**Matching Engine Algorithm (Price-Time Priority):**
1. The new order starts with `remainingQuantity = quantity`.
2. Find matchable active opposite orders in the database for the same `symbol` (`status IN ('OPEN', 'PARTIALLY_FILLED')`):
   - If incoming order is **`BUY`**: opposite orders are `side: 'SELL'` and `ask.price <= buy.price`. Order by: **lowest ask price first** (`price ASC`, `createdAt ASC`).
   - If incoming order is **`SELL`**: opposite orders are `side: 'BUY'` and `bid.price >= sell.price`. Order by: **highest bid price first** (`price DESC`, `createdAt ASC`).
3. While incoming order has `remainingQuantity > 0` and matchable opposite orders exist:
   - Match quantity: `matchQty = Math.min(newOrder.remainingQuantity, oppositeOrder.remainingQuantity)`.
   - Deduct `matchQty` from both orders.
   - Update opposite order status: if `remainingQuantity === 0` $\to$ `'FILLED'`, otherwise `'PARTIALLY_FILLED'`. Save it to the database.
4. Update new order status:
   - If `remainingQuantity === 0` $\to$ `'FILLED'`.
   - If `remainingQuantity < quantity` $\to$ `'PARTIALLY_FILLED'`.
   - If no match occurred $\to$ `'OPEN'`.
5. Save the new order to the database and return it with HTTP status **`201 Created`**.

---

#### 2. `DELETE /orders/:id`
Cancel an active order.

**Lifecycle Rules:**
- If order with `id` is not found $\to$ HTTP **`404 Not Found`**.
- If order status is already `'FILLED'` $\to$ cannot cancel completed order: HTTP **`422 Unprocessable Entity`** with `{ "error": "Cannot cancel completely filled order" }`.
- If order status is already `'CANCELLED'` $\to$ HTTP **`400 Bad Request`** with `{ "error": "Order already cancelled" }`.
- If order status is `'OPEN'` or `'PARTIALLY_FILLED'`:
  - Set `status = 'CANCELLED'`.
  - Save and return the updated order with HTTP **`200 OK`**.

---

#### 3. `GET /orderbook/:symbol`
Retrieve aggregated market depth for active orders:
- Filter by `symbol` and `status IN ('OPEN', 'PARTIALLY_FILLED')`.
- Group by `price`:
  - **`bids`** (`BUY`): sum of `remainingQuantity` for each price level, sorted by `price` descending (**DESC**).
  - **`asks`** (`SELL`): sum of `remainingQuantity` for each price level, sorted by `price` ascending (**ASC**).
- Return HTTP **`200 OK`**:
```json
{
  "symbol": "GS",
  "bids": [
    { "price": 300, "totalQuantity": 150 },
    { "price": 295, "totalQuantity": 40 }
  ],
  "asks": [
    { "price": 305, "totalQuantity": 80 },
    { "price": 310, "totalQuantity": 120 }
  ]
}
```

---

#### 4. `GET /orders`
List historical and active orders:
- Optional query parameters: `symbol`, `status`.
- Sort by `createdAt` descending (`DESC`).
- Return HTTP **`200 OK`**.

---

### Files to Edit
- [controllers/orders.js](file:///Users/arseniizarudniuk/test/code_tasks_prep/goldman_sachs/node_task3_order_matching_book/controllers/orders.js)
- [routes/orders.js](file:///Users/arseniizarudniuk/test/code_tasks_prep/goldman_sachs/node_task3_order_matching_book/routes/orders.js)

### Running Tests
```bash
python3 run_tests.py
# or
npm test
```
