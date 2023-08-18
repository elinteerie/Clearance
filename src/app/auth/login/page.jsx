import Image from "next/image";
import sideImg from "../../../../public/assets/images/school_gate.png";
import Logo from "@/components/common/logo";
import Login_Form from "@/components/screens/login/form";
export const metadata = {
    title: 'Login',
    description: 'Document verification portal',
  }
  
export default function Login() {
  return (
    <>
      <main className="flex flex-col h-screen bg-light_green w-full m-0 p-0 ">
        <div className=" h-full flex flex-row w-full flex-nowrap  items-start justify-evenly p-0 m-0 ">
          <section className=" hidden md:hidden lg:w-2/4 lg:h-full lg:block ">
            <Image src={sideImg} className=" w-full h-full object-cover" />
          </section>
          <section className=" h-full w-full flex justify-center items-center lg:w-2/4  lg:pr-10 lg:pl-10 lg:pt-5 lg:block  ">
            <div className="bg-white w-full h-full flex-1 rounded pt-4  pr-6 pl-6  pb-10 sm:w-3/4 md:flex-initial md:h-fit lg:w-full lg:flex-1 lg:h-fit  ">
              <Logo />
              <div className="w-full mt-3">
                <h1 className=" text-2xl text-dark_green text-center font-bold ">
                  Welcome, Sign up
                </h1>
                <p className="text-center text-base text-brown">
                  please enter correct details{" "}
                </p>
              </div>

              <Login_Form />

              <div className="w-full mt-3 ">
                <p className="text-center text-black text-base ">
                  Already a member?{" "}
                  <span className="left-8  text-dark_green font-medium cursor-pointer ">
                    Sign In
                  </span>
                </p>
              </div>
            </div>
          </section>
        </div>
      </main>
    </>
  );
}
