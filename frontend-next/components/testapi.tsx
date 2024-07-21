"use client";

export async function FetchTestMessage() {
  const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
  if (!response.ok) {
    throw new Error("Network response was not ok");
  }
  const data = await response.json();
  return data;
}
``