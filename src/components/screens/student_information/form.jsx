"use client";
import { ReactStepForm } from "@ebubechi_ihediwa/react-step-form";
import Step_One from "./step_one";
import Step_Two from "./step_two";
import { useState } from "react";

const Studen_Information_Form = () => {
  const [steps, setSteps] = useState(0);
  const noOfSteps = 2;
  const components = [
    <Step_One steps={steps} setSteps={setSteps} noOfSteps={noOfSteps} />,
    <Step_Two steps={steps} setSteps={setSteps} noOfSteps={noOfSteps} />,
  ];
  return (
    <>
      <div className="w-full h-full p-6 lg:bg-light_brown lg:pt-5 lg:w-11/12 lg:flex lg:flex-col lg:self-center">
        <div className="w-full">
          <h1 className=" text-xl  text-dark_green text-center font-bold lg:text-3xl">
            Student information form
          </h1>
          <p className=" text-sm text-brown  font-normal text-center">
            please enter correct details
          </p>
        </div>
        <div className="mt-8 w-full flex flex-col ">
          <ReactStepForm
            indicatorActiveColor={"#0e530e"}
            indicatorInActiveColor={"#6b816b"}
            steps={steps}
            setSteps={setSteps}
            noOfSteps={noOfSteps}
            components={components}
          />
        </div>
      </div>
    </>
  );
};

export default Studen_Information_Form;
