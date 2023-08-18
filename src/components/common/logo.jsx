import Image from "next/image";
import logo from "../../../public/assets/images/logo.png";
const Logo = () => {
  return (
    <div className="flex flex-row justify-start  items-center gap-2 w-full">
      <Image src={logo} width={70} height={77} />
      <h3 className=" text-black text-base lg:text-lg">
        Federal university technology owerri
      </h3>
    </div>
  );
};

export default Logo;
