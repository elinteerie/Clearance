"use client";
import { useState } from "react";
import Input from "./input";

const Sponsor = () => {
  const [address, setAddress] = useState([
    {
      name: "Address",
      value: "",
    },
  ]);
  return (
    <>
      <div className="w-full  mt-11">
        <div className="w-full">
          <Input
            label={"Sponsor name"}
            className={
              " w-full  p-2 outline-none  border-b  bg-transparent  border-black  mt-0 text-black"
            }
          />
        </div>

        <div className="w-full flex items-end flex-col">
          {address.map(({ name, value }) => (
            <div className=" w-11/12 mt-3 " key={name}>
              <Input
                label={name}
                className={
                  " w-full  p-1 outline-none  border-b bg-transparent  border-black  mt-0 text-black"
                }
              />
            </div>
          ))}
        </div>
      </div>
    </>
  );
};

export default Sponsor;
