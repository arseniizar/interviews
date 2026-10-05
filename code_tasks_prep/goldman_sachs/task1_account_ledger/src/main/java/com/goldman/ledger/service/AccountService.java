package com.goldman.ledger.service;

import com.goldman.ledger.dto.CreateAccountRequest;
import com.goldman.ledger.dto.TransferRequest;
import com.goldman.ledger.dto.TransferResponse;
import com.goldman.ledger.exception.AccountNotFoundException;
import com.goldman.ledger.exception.InsufficientFundsException;
import com.goldman.ledger.exception.InvalidTransferException;
import com.goldman.ledger.model.Account;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.util.UUID;

@Service
public class AccountService {

    private final AccountRepository repository;

    public AccountService(AccountRepository repository) {
        this.repository = repository;
    }

    public Account createAccount(CreateAccountRequest request) {
        String id = UUID.randomUUID().toString();
        Account account = new Account(id, request.getHolderName(), request.getInitialBalance());
        return repository.save(account);
    }

    public Account getAccount(String id) {
        return repository.findById(id)
                .orElseThrow(() -> new AccountNotFoundException("Account not found: " + id));
    }

    public synchronized TransferResponse transfer(TransferRequest request) {
        if (request.getFromAccountId().equals(request.getToAccountId())) {
            throw new InvalidTransferException("Cannot transfer to the same account");
        }

        Account fromAccount = repository.findById(request.getFromAccountId())
                .orElseThrow(() -> new AccountNotFoundException("Sender account not found: " + request.getFromAccountId()));

        Account toAccount = repository.findById(request.getToAccountId())
                .orElseThrow(() -> new AccountNotFoundException("Receiver account not found: " + request.getToAccountId()));

        if (fromAccount.getBalance().compareTo(request.getAmount()) < 0) {
            throw new InsufficientFundsException("Insufficient funds in account: " + request.getFromAccountId());
        }

        fromAccount.setBalance(fromAccount.getBalance().subtract(request.getAmount()));
        toAccount.setBalance(toAccount.getBalance().add(request.getAmount()));

        repository.save(fromAccount);
        repository.save(toAccount);

        return new TransferResponse(
                fromAccount.getId(),
                toAccount.getId(),
                request.getAmount(),
                fromAccount.getBalance(),
                toAccount.getBalance(),
                "SUCCESS"
        );
    }
}
