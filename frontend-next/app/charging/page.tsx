import React from "react";
import ChargingCard from "../../components/Card/charging-card";
import NextButton from "../../components/Button/next-button";

const WalletCheck = () => {
  const capacityUsed = 1.1;
  const api_url = `http://127.0.0.1:8000/maschain_token/api_transfer_token/${capacityUsed}`;
  // Define the payload
  const payload = {
    wallet_address: "0x5b3a8eCB9677F56e46d67B7e69900cE322c030d1",
    to: "0xa5314CF6Bd3a4fB9e2448CC92899EA15f24b538e",
    amount: "7",
    contract_address: "0xA10b5960afae880bA86cb3Bb5ec1Ae2eBAe19083",
    callback_url: "https://postman-echo.com/post?"
  };

  return (
    <div>
      <ChargingCard />
      <NextButton urlLink={api_url} buttonText="Stop Charging" payload={payload} />
    </div>
  );
};

export default WalletCheck;
