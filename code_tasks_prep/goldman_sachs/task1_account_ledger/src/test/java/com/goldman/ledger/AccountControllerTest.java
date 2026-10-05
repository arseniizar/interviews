package com.goldman.ledger;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.goldman.ledger.dto.CreateAccountRequest;
import com.goldman.ledger.dto.TransferRequest;
import com.goldman.ledger.model.Account;
import com.goldman.ledger.service.AccountRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import java.math.BigDecimal;

import static org.hamcrest.Matchers.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest
@AutoConfigureMockMvc
public class AccountControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper;

    @Autowired
    private AccountRepository repository;

    @BeforeEach
    void setUp() {
        repository.clear();
    }

    @Test
    void test1_createAccount_validRequest_returns201Created() throws Exception {
        CreateAccountRequest req = new CreateAccountRequest("Alice Smith", new BigDecimal("1000.00"));

        mockMvc.perform(post("/api/accounts")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(req)))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.id", notNullValue()))
                .andExpect(jsonPath("$.holderName", is("Alice Smith")))
                .andExpect(jsonPath("$.balance", is(1000.00)));
    }

    @Test
    void test2_createAccount_blankHolderName_returns400BadRequest() throws Exception {
        CreateAccountRequest req = new CreateAccountRequest("", new BigDecimal("1000.00"));

        mockMvc.perform(post("/api/accounts")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(req)))
                .andExpect(status().isBadRequest());
    }

    @Test
    void test3_createAccount_negativeBalance_returns400BadRequest() throws Exception {
        CreateAccountRequest req = new CreateAccountRequest("Bob", new BigDecimal("-50.00"));

        mockMvc.perform(post("/api/accounts")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(req)))
                .andExpect(status().isBadRequest());
    }

    @Test
    void test4_getAccount_existingId_returns200OkWithDetails() throws Exception {
        Account acc = repository.save(new Account("ACC-1", "Charlie", new BigDecimal("500.00")));

        mockMvc.perform(get("/api/accounts/ACC-1"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id", is("ACC-1")))
                .andExpect(jsonPath("$.holderName", is("Charlie")))
                .andExpect(jsonPath("$.balance", is(500.00)));
    }

    @Test
    void test5_getAccount_nonExistingId_returns404NotFound() throws Exception {
        mockMvc.perform(get("/api/accounts/UNKNOWN-ID"))
                .andExpect(status().isNotFound());
    }

    @Test
    void test6_transfer_validRequest_returns200AndUpdatesBalances() throws Exception {
        repository.save(new Account("ACC-SENDER", "Alice", new BigDecimal("1000.00")));
        repository.save(new Account("ACC-RECEIVER", "Bob", new BigDecimal("200.00")));

        TransferRequest req = new TransferRequest("ACC-SENDER", "ACC-RECEIVER", new BigDecimal("300.00"));

        mockMvc.perform(post("/api/transfers")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(req)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.fromAccountId", is("ACC-SENDER")))
                .andExpect(jsonPath("$.toAccountId", is("ACC-RECEIVER")))
                .andExpect(jsonPath("$.transferredAmount", is(300.00)))
                .andExpect(jsonPath("$.fromAccountBalance", is(700.00)))
                .andExpect(jsonPath("$.toAccountBalance", is(500.00)))
                .andExpect(jsonPath("$.status", is("SUCCESS")));
    }

    @Test
    void test7_transfer_insufficientFunds_returns400BadRequest() throws Exception {
        repository.save(new Account("ACC-POOR", "Alice", new BigDecimal("50.00")));
        repository.save(new Account("ACC-RECEIVER", "Bob", new BigDecimal("200.00")));

        TransferRequest req = new TransferRequest("ACC-POOR", "ACC-RECEIVER", new BigDecimal("500.00"));

        mockMvc.perform(post("/api/transfers")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(req)))
                .andExpect(status().isBadRequest());
    }

    @Test
    void test8_transfer_senderNotFound_returns404NotFound() throws Exception {
        repository.save(new Account("ACC-RECEIVER", "Bob", new BigDecimal("200.00")));

        TransferRequest req = new TransferRequest("ACC-UNKNOWN", "ACC-RECEIVER", new BigDecimal("50.00"));

        mockMvc.perform(post("/api/transfers")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(req)))
                .andExpect(status().isNotFound());
    }

    @Test
    void test9_transfer_receiverNotFound_returns404NotFound() throws Exception {
        repository.save(new Account("ACC-SENDER", "Alice", new BigDecimal("1000.00")));

        TransferRequest req = new TransferRequest("ACC-SENDER", "ACC-UNKNOWN", new BigDecimal("50.00"));

        mockMvc.perform(post("/api/transfers")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(req)))
                .andExpect(status().isNotFound());
    }

    @Test
    void test10_transfer_sameAccount_returns400BadRequest() throws Exception {
        repository.save(new Account("ACC-SAME", "Alice", new BigDecimal("1000.00")));

        TransferRequest req = new TransferRequest("ACC-SAME", "ACC-SAME", new BigDecimal("50.00"));

        mockMvc.perform(post("/api/transfers")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(req)))
                .andExpect(status().isBadRequest());
    }

    @Test
    void test11_transfer_zeroOrNegativeAmount_returns400BadRequest() throws Exception {
        repository.save(new Account("ACC-SENDER", "Alice", new BigDecimal("1000.00")));
        repository.save(new Account("ACC-RECEIVER", "Bob", new BigDecimal("200.00")));

        TransferRequest req = new TransferRequest("ACC-SENDER", "ACC-RECEIVER", new BigDecimal("-10.00"));

        mockMvc.perform(post("/api/transfers")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(req)))
                .andExpect(status().isBadRequest());
    }
}
