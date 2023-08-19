import Image from "next/image";
import logo from "../../../public/assets/images/logo.png";
const Logo = ({bg}) => {
  return (
    <div style={{background:bg}} className="flex flex-row justify-start  items-center gap-2 w-full">
      <Image priority alt="logo" src={logo} width={'auto'} height={'auto'} />
      <h3 className=" text-black text-base lg:text-lg">
        Federal university technology owerri
      </h3>
    </div>
  );
};

export default Logo;
