"use client";
import React, { useState, useEffect } from "react";

interface Token {
  contract_address: string;
  name: string;
  symbol: string;
}

interface Transaction {
  to: string;
  from: string;
  blockNumber: number | null;
  transactionHash: string | null;
  method: string;
  decimal: number | null;
  amount: string | null;
  token: Token;
  timestamp: string;
}

interface ApiResponseData {
  status: number;
  result: Transaction[];
  pagination: {
    current_page: number;
    first_page_url: string;
    last_page: number;
    last_page_url: string;
    next_page_url: string | null;
    per_page: number;
    prev_page_url: string | null;
    total: number;
  };
}

interface ApiResponse {
  status: string;
  data: ApiResponseData;
}

const ApiTest: React.FC = () => {
  const [transactions, setTransactions] = useState<Transaction[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/maschain_token/api_get_transaction_from/0x5b3a8eCB9677F56e46d67B7e69900cE322c030d1")
      .then((response) => response.json())
      .then((data: ApiResponse) => {
        setTransactions(data.data.result);
      })
      .catch((error) => {
        console.error("Error fetching the API:", error);
      });
  }, []);

  return (
    <div>
      <h1>API Test</h1>
      {transactions.length > 0 ? (
        <ul>
          {transactions.map((transaction, index) => (
            <li key={index}>
              <p>To: {transaction.to}</p>
              <p>From: {transaction.from}</p>
              <p>Block Number: {transaction.blockNumber}</p>
              <p>Transaction Hash: {transaction.transactionHash}</p>
              <p>Method: {transaction.method}</p>
              <p>Decimal: {transaction.decimal}</p>
              <p>Amount: {transaction.amount}</p>
              <p>Token: {transaction.token.name} ({transaction.token.symbol})</p>
              <p>Timestamp: {transaction.timestamp}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>No transactions found</p>
      )}
    </div>
  );
};

export default ApiTest;
