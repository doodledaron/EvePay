'use client';

import Image from "next/image";
import { useEffect, useState } from 'react';
import { FetchTestMessage } from '../components/testapi';

export default function Home() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    async function getData() {
      try {
        const data = await FetchTestMessage();
        console.log('Fetched data:', data);
        setMessage(data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }

    getData();
  }, []);

  return (
    <main>
     <h1>Test API Connection</h1>
     {/* <p>{message}</p> */}
    </main>
  );
}
