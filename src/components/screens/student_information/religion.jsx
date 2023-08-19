"use client";

const Religion = () => {
  return (
    <div className="w-full flex flex-row justify-evenly items-baseline gap-4  mb-5 lg:w-2/5 ">
      <div className=" w-1/3">
        <label className=" text-brown text-sm font-medium">Religion:</label>
      </div>
      <div className=" w-4/6 flex flex-row gap-4">
        <input
          className={
            " w-full   rounded p-2 outline-none border-none  bg-gray-300 mt-3 text-black lg:w-4/5 "
          }
        />
      </div>
    </div>
  );
};

export default Religion;
