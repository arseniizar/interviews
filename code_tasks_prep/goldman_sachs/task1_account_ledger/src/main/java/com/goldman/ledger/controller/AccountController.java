package com.goldman.ledger.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import com.goldman.ledger.service.AccountService;
import com.goldman.ledger.dto.CreateAccountRequest;
import com.goldman.ledger.dto.TransferRequest;
import com.goldman.ledger.dto.TransferResponse;
import com.goldman.ledger.model.Account;
import jakarta.validation.Valid;

@RestController 
@RequestMapping("/api")
public class AccountController {

    private final AccountService accountService;

    public AccountController(AccountService accountService) {
        this.accountService = accountService;
    }

    @PostMapping("/accounts")
    public ResponseEntity<Account> createAccount(@Valid @RequestBody CreateAccountRequest dto) {
        Account account = accountService.createAccount(dto);
    
        return ResponseEntity.status(HttpStatus.CREATED).body(account);
    }

    @GetMapping("/accounts/{id}")
    public ResponseEntity<Account> getAccount(@PathVariable String id) {
        Account account = accountService.getAccount(id);
        
        return ResponseEntity.status(HttpStatus.OK).body(account);
    }

    @PostMapping("/transfers")
    public ResponseEntity<TransferResponse> transfer(@Valid @RequestBody TransferRequest dto) {
        TransferResponse response = accountService.transfer(dto);

        return ResponseEntity.status(HttpStatus.OK).body(response);
    }
}
