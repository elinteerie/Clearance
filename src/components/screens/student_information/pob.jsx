"use client";

import { useState } from "react";
import Input from "./input";

const POB = () => {
  const [pob, setPob] = useState([
    {
      name: "Town/village",
      value: "",
    },
    {
      name: "State",
      value: "",
    },
  ]);
  return (
    <div className="w-full flex flex-col justify-start items-baseline  mt-4 ">
      <div className=" w-full lg:w-3/12">
        <label className=" text-brown text-sm font-medium">
          Place of Birth:
        </label>
      </div>

      <div className=" w-full lg:flex lg:flex-row lg:justify-start lg:items-center gap-4">
        {pob.map(({ name, value }) => (
          <div key={name} className="w-full mt-2 lg:w-2/5  ">
            <Input
              key={name}
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

export default POB;
