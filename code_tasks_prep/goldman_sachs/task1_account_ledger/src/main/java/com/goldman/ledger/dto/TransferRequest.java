package com.goldman.ledger.dto;

import java.math.BigDecimal;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

// TODO: Add Jakarta validation annotations so that:
// 1. fromAccountId cannot be blank
// 2. toAccountId cannot be blank
// 3. amount cannot be null, and must be strictly positive (> 0)
public class TransferRequest {

    @NotBlank(message = "From account ID cannot be blank")
    private String fromAccountId;
    
    @NotBlank(message = "To account ID cannot be blank")
    private String toAccountId;
    
    @NotNull 
    @Min(value = 1, message = "Amount must be positive")
    private BigDecimal amount;

    public TransferRequest() {}

    public TransferRequest(String fromAccountId, String toAccountId, BigDecimal amount) {
        this.fromAccountId = fromAccountId;
        this.toAccountId = toAccountId;
        this.amount = amount;
    }

    public String getFromAccountId() { return fromAccountId; }
    public void setFromAccountId(String fromAccountId) { this.fromAccountId = fromAccountId; }

    public String getToAccountId() { return toAccountId; }
    public void setToAccountId(String toAccountId) { this.toAccountId = toAccountId; }

    public BigDecimal getAmount() { return amount; }
    public void setAmount(BigDecimal amount) { this.amount = amount; }
}
