import Input from "./input";

const Nationality = () => {
  return (
    <>
      <div className=" w-full lg:w-1/3 ">
        <Input
          className={
            " w-full  rounded p-2 outline-none border-none  bg-gray-300 mt-3 text-black lg:w-4/5 "
          }
          label={"Nationality code"}
        />
      </div>
    </>
  );
};

export default Nationality;
