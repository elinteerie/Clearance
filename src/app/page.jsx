"use client";
import Image from "next/image";
import sideImg from "../../public/assets/images/school_gate.png";
import Button from "@/components/common/button";
import Logo from "@/components/common/logo";
import { useRouter } from "next/navigation";
export default function Home() {
  const router = useRouter();
  return (
    <>
      <main className="flex flex-col h-screen bg-light_green w-full m-0 p-0 ">
        <div className=" h-full flex flex-row w-full flex-nowrap  items-start justify-evenly p-0 m-0 ">
          <section className=" hidden md:hidden lg:basis-2/4 lg:h-full lg:block ">
            <Image src={sideImg} className=" w-full h-full object-cover" />
          </section>
          <section className=" h-full basis-full flex justify-center items-center lg:basis-2/4  lg:pr-10 lg:pl-10 lg:pt-5 lg:block ">
            <div className="bg-white w-full h-full flex-1 rounded pt-4  pr-6 pl-6  pb-10 sm:w-3/4 md:flex-initial md:h-fit lg:w-full lg:flex-1 lg:h-fit  ">
              <Logo />

              <div className="w-full mt-3">
                <h1 className=" text-2xl text-dark_green text-center font-bold ">
                  Clearance for first year
                </h1>
              </div>

              <div className="w-full mt-10 mb-28">
                <p className="text-black text-lg text-left">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. In at
                  pellentesque dui. Sed eget euismod enim. Vivamus m aximus
                  lacinia lectus vitae vehicula. Ut placerat molestie lectus, et
                  accumsan ris us gravida et. Praesent eget aliquam purus, ac
                  rutrum leo. Quisque et mattis nulla. Cras vestibulu m sem eu
                  ante i aculis, nec sollicitudin nulla porttitor. Aliquam
                  blandit orci erat, sed viverra libero lobortis lacinia. Donec
                  eu placera t ex, eget laoreet risus.
                </p>
              </div>
              <div className="w-full mt-14 flex flex-row items-center justify-center mb-9  ">
                <Button
                  onClick={() => {
                    router.push("/auth/login");
                  }}
                  title={"Get Started"}
                  width={"150px"}
                />
              </div>
            </div>
          </section>
        </div>
      </main>
    </>
  );
}
