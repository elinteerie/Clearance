"use client";

import { useState } from "react";

const Sex = () => {
  const [sex, setSex] = useState([
    {
      name: "Male",
      checked: false,
    },
    {
      name: "Female",
      checked: false,
    },
  ]);
  return (
    <>
      <div className="w-full flex flex-row justify-start items-center gap-4  mt-5  lg:w-1/3">
        <div className=" w-1/12 ">
          <label className=" text-brown text-sm font-medium">Sex:</label>
        </div>
        <div className="w-11/12 flex flex-row gap-4">
          {sex.map(({ name, checked }) => (
            <div key={name} className=" w-auto gap-3 flex flex-row items-center justify-evenly">
              <p>{name}</p>
              <input type="checkbox" />
            </div>
          ))}
        </div>
      </div>
    </>
  );
};

export default Sex;
