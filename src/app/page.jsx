import Image from "next/image";
import sideImg from "../../public/assets/images/school_gate.png";
import Button from "@/components/common/button";
import Logo from "@/components/common/logo";
export default function Home() {
  return (
    <>
      <main className="flex flex-col min-h-screen bg-light_green w-full m-0 p-0 ">
        <div className=" flex flex-row w-full flex-nowrap  items-start justify-evenly p-0 m-0 ">
          <section className=" basis-2/4 h-full">
            <Image src={sideImg} className=" w-full h-full object-cover" />
          </section>
          <section className=" basis-2/4 h-full  pr-10 pl-10 pt-5 ">
            <div className="bg-white rounded pt-4 pb-4 pr-6 pl-6 h-full flex-1 ">
              <Logo />

              <div className="w-full mt-3">
                <h1 className=" text-2xl text-dark_green text-center font-bold ">
                  Clearance for first year
                </h1>
              </div>

              <div className="w-full mt-10  mb-48">
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
                <Button title={"Get Started"} width={"150px"} />
              </div>
            </div>
          </section>
        </div>
      </main>
    </>
  );
}
