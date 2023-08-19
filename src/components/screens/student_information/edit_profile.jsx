import Button from "@/components/common/button";
import Image from "next/image";
import placeholderImage from "../../../../public/assets/images/user-placeholder.jpeg";
const Edit_Profile = () => {
  return (
    <>
      <div className="w-full mb-4 mt-6 lg:flex lg:flex-col ">
        <Image
        alt="user img"
          src={placeholderImage}
          className="w-full h-20 object-cover mb-3 lg:rounded-full lg:w-1/2 lg:h-2/4 lg:flex lg:self-center"
        />
        <Button
          title={"Edit profile"}
          padding={"4px"}
          className={`w-full bg-dark_green text-white p-2 rounded-md  text-center hover:bg-light_green lg:w-1/2 lg:self-center`}
        />
      </div>
    </>
  );
};

export default Edit_Profile;
