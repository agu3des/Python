import React from "react";

export function Akari({className='w-4'}) {
    return (
        <img
          src="/img/logo.png"
          className={className}
          alt="Picture of the author"
        />
    )
}

export function AkariLogo({className='lg:flex'}) {
    return (
        <img
          src="/img/logo-AK.png"
          className={className}
          alt="Picture of the author"
        />
    )
}