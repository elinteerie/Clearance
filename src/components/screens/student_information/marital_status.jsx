"use client";

const Marital_Status = () => {
  return (
    <div className="w-full flex flex-row justify-evenly items-baseline gap-4  mt-5 mb-5 lg:w-2/5 ">
      <div className=" w-1/3  ">
        <label className=" text-brown text-sm font-medium">
          Marital Status:
        </label>
      </div>
      <div className=" w-4/6 flex flex-row gap-4">
        <select
          className={
            " w-full   rounded p-2 outline-none border-none  bg-gray-300 mt-3 text-black lg:w-4/5 "
          }
        >
          <option>Single</option>
          <option>Married</option>
        </select>
      </div>
    </div>
  );
};

export default Marital_Status;
