"use client";

import { useState } from "react";
import Input from "./input";

const POO = () => {
  const [poo, setPoo] = useState([
    {
      name: "Town/village",
      value: "",
    },
    {
      name: "State",
      value: "",
    },
    {
      name: "LGA",
      value: "",
    },
  ]);
  return (
    <div className="w-full flex flex-col justify-start items-baseline  mt-4">
      <div className=" w-full lg:w-3/12">
        <label className=" text-brown text-sm font-medium">
          Place of Origin:
        </label>
      </div>
      <div className=" w-full lg:flex lg:flex-row lg:justify-start lg:items-center gap-4">
        {poo.map(({ name, value }) => (
          <div className="w-full mt-2" key={name} >
            <Input
              
              direction={"flex-col-reverse"}
              align={"text-center "}
              marginTop={"mt-1"}
              label={name}
              className={
                " w-full rounded p-2 outline-none border-none  bg-gray-300 mt-3 text-black"
              }
            />
          </div>
        ))}
      </div>
    </div>
  );
};

export default POO;
