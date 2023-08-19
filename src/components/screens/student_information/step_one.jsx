'use client'
import Button from "@/components/common/button";
import Basic_Info from "./basic_info";
import DOB from "./dob";
import Marital_Status from "./marital_status";
import Nationality from "./nationality";
import POB from "./pob";
import POO from "./poo";
import Religion from "./religion";
import Sex from "./sex";
import { Next } from "@ebubechi_ihediwa/react-step-form";
import { useEffect } from "react";

const Step_One = ({steps, setSteps, noOfSteps}) => {
  useEffect(()=>{
    window.scroll(0,0)
  },[])
  return (
    <>
      <div className="w-full mt-11  ">
        <Basic_Info />
        <div className="w-full flex flex-col  justify-evenly items-center  mt-8 lg:flex-row lg:justify-evenly lg:items-center">
          <Nationality />
          <Sex />
          <DOB />
        </div>

        <POB />
        <POO />
        <div className="w-full flex flex-col  justify-evenly items-center  mt-8 lg:flex-row lg:justify-start lg:items-center">
          <Marital_Status />
          <Religion />
        </div>

        <div className="w-full mt-6 mb-6 lg:flex lg:justify-center lg:items-center ">
          <Button
          onClick={()=>{
            Next(steps,setSteps,noOfSteps)
          }}
            className={
              "w-full bg-dark_green text-white p-2 rounded-md  text-center hover:bg-light_green lg:w-1/2"
            }
            title={"Next"}
          />
        </div>
      </div>
    </>
  );
};

export default Step_One;
