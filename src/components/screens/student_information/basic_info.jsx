import { useState } from "react";
import Input from "./input";
import Edit_Profile from "./edit_profile";

const Basic_Info = () => {
  const [names, setName] = useState([
    {
      name: "First name",
      value: "",
      id: 1,
    },
    {
      name: "Last name",
      value: "",
      id: 2,
    },
    {
      name: "Middle name",
      value: "",
      id: 3,
    },
    {
      name: "Any former name?",
      value: "",
      id: 4,
    },
  ]);
  return (
    <>
      <div className="w-full flex flex-col justify-evenly items-center lg:flex-row lg:items-start ">
        <section className="w-full lg:w-3/4 ">
          <Input
            label={"Registration number"}
            className={
              " w-full  rounded p-2 outline-none border-none  bg-gray-300 mt-3 text-black "
            }
          />

          <div className="flex flex-col justify-evenly items-center lg:flex-row lg:flex-wrap lg:justify-between">
            {names.map(({ name, value, id }) => (
              <div key={id} className="w-full  mt-4 lg:w-1/2 lg:flex lg:justify-end ">
                <Input
                  label={name}
                  key={id}
                  className={
                    " w-full  rounded p-2 outline-none border-none  bg-gray-300 mt-3 text-black lg:w-11/12 "
                  }
                />
              </div>
            ))}
          </div>
        </section>

        {/* Image section */}
        <section className="w-full lg:w-1/4 " >
        <Edit_Profile/>
        </section>
      </div>
    </>
  );
};

export default Basic_Info;
