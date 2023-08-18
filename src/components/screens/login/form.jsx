"use client";
import Button from "@/components/common/button";
import { useState } from "react";

const Login_Form = () => {
  const [formData, setFormData] = useState([
    {
      name: "Reg No",
      value: "",
      type: "text",
    },
    {
      name: "Email",
      value: "",
      type: "email",
    },
    {
      name: "Password",
      value: "",
      type: "password",
    },
    {
      name: "Confirm Password",
      value: "",
      type: "password",
    },
  ]);

  const handleInputChange = (index, newValue) => {
    const updatedFormData = [...formData];
    updatedFormData[index].value = newValue;
    setFormData(updatedFormData);
  };
  return (
    <>
      <form
        className="w-full mt-6 "
        onSubmit={(e) => {
          e.preventDefault();
        }}
      >
        {formData.map(({ name, value, type },index) => (
          <div className="w-full mt-3">
            <div className="w-full flex  justify-start items-center">
              <label className=" text-ls text-brown font-medium">{name}:</label>
            </div>
            <div className="w-full mt-1 ">
              <input
                onChange={(e) => handleInputChange(index, e.target.value)}
                type={type}
                value={value}
                className=" w-full border-b text-black  border-black focus:outline-none focus:border-black "
              />
            </div>
          </div>
        ))}

        <div className="w-full flex justify-center items-center mt-16 ">
          <Button
            radius={"21px"}
            width={"60%"}
            title={"Sign Up"}
            bg={"#114111"}
          />
        </div>
      </form>
    </>
  );
};

export default Login_Form;
