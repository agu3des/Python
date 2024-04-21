'use client';

import { useEffect } from 'react';
import ProductCard from '@/components/ProductCard';
import { useBook } from '@/context/AkariContext';


export default function Home() {
  const {
    books,
    loadBooks,
  } = useBook();

useEffect(() => {
  loadBooks();
}, []);

  return (
    <>
      <main>
        <div className="grid grid-cols-3 max-sm:grid-cols-1 gap-3 pt-3 pb-3 pl-4 pr-4">
          {books.map((book) => (<BooksCards {...book} key={book.id} />))}
        </div>
      </main>
    </>
  );
}