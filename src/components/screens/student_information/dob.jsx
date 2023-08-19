"use client";

// import { useState } from "react";

const DOB = () => {
  return (
    <>
      <div className="w-full flex flex-col justify-start items-baseline  mt-4  lg:w-1/3 lg:flex-row ">
        <div className=" w-full lg:w-3/12">
          <label className=" text-brown text-sm font-medium">
            Date of birth:
          </label>
        </div>
        <div className=" w-full lg:w-9/12">
          <input
            placeholder="dd/mm/yy"
            className={
              " w-full   rounded p-2 outline-none border-none  bg-gray-300 mt-3 text-black lg:w-3/4 "
            }
          />
        </div>
      </div>
    </>
  );
};

export default DOB;
