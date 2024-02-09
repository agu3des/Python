'use client';

import React, { createContext, useState, useContext } from 'react';
import Storage from '@/services/supabase';
import { validEmail } from '@/lib/regex';

export const BookContext = createContext({});

export function AkariProvider({ children }) {
  const initialBookFormData = {
    id: '',
    name: '',
    value: '',
    autor: '',
    editora: '',
    image: '',
  };

  const [products, setProduct] = useState([]);

  const [isShowBookForm, setIsShowBookForm] = useState(false);

  const [bookFormData, setBookFormData] = useState(initialBookFormData);

  const [email, setEmail] = useState('');

  const [emailErr, setEmailErr] = useState(false);

  const [currentIndex, setCurrentIndex] = useState(0);

  const handleNext = () => {
    if (currentIndex < products.length - 1) {
      setCurrentIndex(currentIndex + 1);
    }
  };

  const handlePrevious = () => {
    if (currentIndex > 0) {
      setCurrentIndex(currentIndex - 1);
    }
  };

  const handleCreateBook = async () => {
    setBookFormData(initialBookFormData);

    toggleShowBookForm();
  };

  const toggleShowBookForm = () => {
    setIsShowBookForm(!isShowBookForm);
  };

  const loadProducts = async () => {
    const products = await Storage.read('products');

    setProduct(products);
  };

  const createBook = async (book) => {
    const newBook = await Storage.create('products', book);

    setProduct([...products, newBook]);
  };

  const removeBook = (id) => {
    const newProducts = products.filter(
      (book) => book.id !== id
    );

    setProduct(newProducts);

    Storage.remove('products', id);
  };

  const validate = async () => {
     if (!validEmail.test(email)) {
        setEmailErr(true);
     }
  }
  
  return (
    <AkariContext.Provider
      value={{
        products,
        setProduct,
        isShowBookForm,
        setIsShowBookForm,
        bookFormData,
        setBookFormData,
        email,
        setEmail,
        emailErr,
        setEmailErr,
        currentIndex, 
        setCurrentIndex,
        handleNext,
        handlePrevious,
        toggleShowBookForm,
        loadProducts,
        createBook,
        removeBook,
        handleCreateBook,
        validate,

      }}
    >
      {children}
    </AkariContext.Provider>
  );
}

export function useBook() {
  return useContext(AkariContext);
}