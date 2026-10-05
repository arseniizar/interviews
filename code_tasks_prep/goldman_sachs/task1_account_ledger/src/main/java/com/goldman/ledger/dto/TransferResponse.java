package com.goldman.ledger.dto;

import java.math.BigDecimal;

public class TransferResponse {
    private String fromAccountId;
    private String toAccountId;
    private BigDecimal transferredAmount;
    private BigDecimal fromAccountBalance;
    private BigDecimal toAccountBalance;
    private String status;

    public TransferResponse() {}

    public TransferResponse(String fromAccountId, String toAccountId, BigDecimal transferredAmount,
                            BigDecimal fromAccountBalance, BigDecimal toAccountBalance, String status) {
        this.fromAccountId = fromAccountId;
        this.toAccountId = toAccountId;
        this.transferredAmount = transferredAmount;
        this.fromAccountBalance = fromAccountBalance;
        this.toAccountBalance = toAccountBalance;
        this.status = status;
    }

    public String getFromAccountId() { return fromAccountId; }
    public void setFromAccountId(String fromAccountId) { this.fromAccountId = fromAccountId; }

    public String getToAccountId() { return toAccountId; }
    public void setToAccountId(String toAccountId) { this.toAccountId = toAccountId; }

    public BigDecimal getTransferredAmount() { return transferredAmount; }
    public void setTransferredAmount(BigDecimal transferredAmount) { this.transferredAmount = transferredAmount; }

    public BigDecimal getFromAccountBalance() { return fromAccountBalance; }
    public void setFromAccountBalance(BigDecimal fromAccountBalance) { this.fromAccountBalance = fromAccountBalance; }

    public BigDecimal getToAccountBalance() { return toAccountBalance; }
    public void setToAccountBalance(BigDecimal toAccountBalance) { this.toAccountBalance = toAccountBalance; }

    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}
