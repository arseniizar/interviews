package com.goldman.ledger.exception;

import java.util.Map;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.ErrorResponse;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestControllerAdvice;

// TODO: Wire up this class to intercept exceptions across all controllers
@RestControllerAdvice
public class GlobalExceptionHandler {

    // TODO: Handle AccountNotFoundException -> Return HTTP 404 NOT FOUND with body {"error": message}
    @ExceptionHandler(value = AccountNotFoundException.class)
    public ResponseEntity<Map<String, String>> handleNotFound(AccountNotFoundException ex) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(Map.of("error", ex.getMessage()));
    }

    // TODO: Handle InsufficientFundsException -> Return HTTP 400 BAD REQUEST with body {"error": message}
    @ExceptionHandler(value = InsufficientFundsException.class)
    public ResponseEntity<Map<String, String>> handleInsufficientFunds(InsufficientFundsException ex) {
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(Map.of("error", ex.getMessage()));
    }

    // TODO: Handle InvalidTransferException -> Return HTTP 400 BAD REQUEST with body {"error": message}
    @ExceptionHandler(value = InvalidTransferException.class)
    public ResponseEntity<Map<String, String>> handleInvalidTransfer(InvalidTransferException ex) {
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(Map.of("error", ex.getMessage()));
    }
    

    // TODO: Handle MethodArgumentNotValidException -> Return HTTP 400 BAD REQUEST with body {"error": "Validation failed"}
    @ExceptionHandler(value = MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, String>> handleMethodArgumentNotValid(MethodArgumentNotValidException ex) {
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(Map.of("error", ex.getMessage()));
    }    
}
