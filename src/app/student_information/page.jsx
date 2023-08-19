import Logo from "@/components/common/logo";
import Studen_Information_Form from "@/components/screens/student_information/form";
// import y from "../../../public/assets/images/school_gate.png"
export const metadata = {
  title: "Student Information",
  description: "Collecting student information",
};
const Student_Information = () => {
  return (
    <>
      <main className="w-full min-h-screen ">
        <Logo bg={"green"} />
        <div className="w-full min-h-inherit flex flex-col lg:p-8 lg:bg-[url('../../public/assets/images/school_gate.png')] lg:bg-no-repeat lg:bg-center lg:bg-cover">
          <Studen_Information_Form />
        </div>
      </main>
    </>
  );
};

export default Student_Information;
