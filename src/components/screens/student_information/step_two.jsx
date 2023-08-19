'use client'
import Button from "@/components/common/button";
import Address from "./address";
import Next_Of_Kin from "./next_of_kin";
import Sponsor from "./sponsor";
import { Prev } from "@ebubechi_ihediwa/react-step-form";
import { useEffect } from "react";

const Step_Two = ({steps, setSteps, noOfSteps}) => {
  useEffect(()=>{
    window.scroll(0,0)
  },[])
  return (
    <>
      <div className="w-full mt-11 ">
        <Address />
        <Next_Of_Kin />
        <Sponsor />
        <div className="w-full flex mt-14 mb-6 justify-between items-center ">
          <Button
          onClick={()=>{
            Prev(steps,setSteps,noOfSteps)
          }}
            className={
              " w-4/12 bg-dark_green text-white p-2 rounded-md  text-center hover:bg-light_green lg:w-4/12"
            }
            title={"Back"}
          />
            <Button
            className={
              "w-1/2 bg-dark_green text-white p-2 rounded-md  text-center hover:bg-light_green lg:w-4/12"
            }
            title={"Preview & submit"}
          />
        </div>
      </div>
    </>
  );
};

export default Step_Two;
