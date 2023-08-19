import { useState } from "react";
import Input from "./input";

const Address = () => {
  const [address, setAddress] = useState([
    {
      name: "Permanent address",
      value: "",
    },
    {
      name: "Contact address",
      value: "",
    },
  ]);
  return (
    <>
      <div className="flex flex-col justify-evenly items-center">
        <div className="w-full">
          <label className=" text-brown text-sm font-medium text-left ">
            Address:
          </label>
        </div>
        {address.map(({ name, value }) => (
          <Input
          key={name}
            label={name}
            align={'text-center'}
            marginTop={'mt-1'}
            direction={"flex-col-reverse"}
            className={
              " w-full  p-2 outline-none  bg-transparent border-b   border-black  mt-0 text-black"
            }
          />
        ))}
      </div>
    </>
  );
};

export default Address;
