package com.goldman.ledger.service;

import com.goldman.ledger.model.Account;
import org.springframework.stereotype.Repository;

import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;

@Repository
public class AccountRepository {
    private final ConcurrentHashMap<String, Account> storage = new ConcurrentHashMap<>();

    public Account save(Account account) {
        storage.put(account.getId(), account);
        return account;
    }

    public Optional<Account> findById(String id) {
        return Optional.ofNullable(storage.get(id));
    }

    public boolean existsById(String id) {
        return storage.containsKey(id);
    }

    public void clear() {
        storage.clear();
    }
}
