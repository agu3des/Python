import { Oswald } from 'next/font/google'
import './globals.css'
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import { AkariProvider } from '@/context/AkariContext'


const oswald = Oswald({style: 'normal', weight: '400', preload: false, display: 'swap', serif: false})


export const metadata = {
  title: 'Akari',
  description: 'Aplicação de uma loja',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">   
      <head>
        <link rel="icon" href="/public/favicon.ico" type="image/icon" />
      </head>
      <body className={oswald.className}>
        <AkariProvider>
          <Header />
          <div>
            {children}
          </div>
          <Footer />
        </AkariProvider>
      </body>
    </html>
  )
}