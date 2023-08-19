"use client";
import { useState } from "react";
import Input from "./input";

const Next_Of_Kin = () => {
  const [address, setAddress] = useState([
    {
      name: "Address",
      value: "",
    },
    {
      name: "Telephone",
      value: "",
    },
  ]);
  return (
    <>
      <div className="w-full mt-5">
        <div className="w-full">
          <Input
            label={"Next of kin name"}
            className={
              " w-full  bg-transparent  p-2 outline-none  border-b   border-black  mt-0 text-black"
            }
          />
        </div>

        <div className="w-full flex items-end flex-col">
          {address.map(({ name, value }) => (
            
            <div className=" w-11/12 mt-3 "  key={name} >
              <Input
                label={name}
                className={
                  " w-full  p-1 outline-none  bg-transparent border-b   border-black  mt-0 text-black"
                }
              />
            </div>
          ))}

          <div className="w-full mt-8">
            <Input
              label={"Marital Status:"}
              direction={"flex-row"}
              items={"items-baseline"}
              justify={"justify-start"}
              className={
                " w-1/2   bg-transparent text-sm ml-4 rounded p-1 outline-none border-none  bg-gray-300  border-black  mt-0 text-black"
              }
            />
          </div>
        </div>
      </div>
    </>
  );
};

export default Next_Of_Kin;
