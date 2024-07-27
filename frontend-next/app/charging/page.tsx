"use client";
import React, { useEffect, useState } from 'react';
// import { BaseSyntheticEvent, useState } from 'react';
import ChargingCard from "../../components/Card/charging-card";
import NextButton from "../../components/Button/next-button";

// export default function WalletCheck() {
//   return (
//     <div>
//       <ChargingCard />

//       <NextButton urlLink="/payment" buttonText="Stop Charging" />
//     </div>
//   );
// }

export default function WalletCheck() {
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState(false);

  useEffect(() => {
    const sendMessage = async () => {
      setLoading(true);
      setError(false);
      setSuccess(false);
      
      try {
        const res = await fetch('/api/sendMessage', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const apiResponse = await res.json();

        if (apiResponse.success) {
          setSuccess(true);
        } else {
          setError(true);
        }
      } catch (error) {
        setError(true);
      } finally {
        setLoading(false);
      }
    };

    const timer = setTimeout(sendMessage, 30000); // 30 seconds

    return () => clearTimeout(timer); // Cleanup timer on unmount
  }, []);

  return (
    <div>
      <ChargingCard />
      <NextButton urlLink="/payment" buttonText="Stop Charging" />
      {loading && <p>Sending message...</p>}
      {success && <p>Message sent successfully.</p>}
      {error && <p>Something went wrong. Please check the number.</p>}
    </div>
  );
}