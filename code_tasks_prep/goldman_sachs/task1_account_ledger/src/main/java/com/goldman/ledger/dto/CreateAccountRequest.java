package com.goldman.ledger.dto;

import java.math.BigDecimal;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

// TODO: Add Jakarta validation annotations so that:
// 1. holderName cannot be blank
// 2. initialBalance cannot be null, and must be zero or positive (>= 0)
public class CreateAccountRequest {

    @NotBlank
    private String holderName;

    @NotNull
    @Min(value = 0, message = "Initial balance must be zero or positive")
    private BigDecimal initialBalance;

    public CreateAccountRequest() {
    }

    public CreateAccountRequest(String holderName, BigDecimal initialBalance) {
        this.holderName = holderName;
        this.initialBalance = initialBalance;
    }

    public String getHolderName() { return holderName; }
    public void setHolderName(String holderName) { this.holderName = holderName; }

    public BigDecimal getInitialBalance() { return initialBalance; }
    public void setInitialBalance(BigDecimal initialBalance) { this.initialBalance = initialBalance; }
}
