import Image from "next/image";
import NextButton from "../components/Button/getStarted-button";
import AosWrapper from "../components/AOS/aos-wrapper";

export default function Home() {
  return (
    <div className="flex flex-col mt-16 items-center">
      <AosWrapper animationType="fade-up" duration={1400}>
        <Image src="/main-page.jpg" alt="Main Page" width={421} height={396} />

        <p className="mt-5 text-center font-semibold text-gray">
          Get ready for seamless and secure charging?
        </p>
        <p className="text-center font-semibold text-gray">
          Login to your <span className="text-light-cyan">Maschain wallet</span>.
        </p>
      </AosWrapper>

      <NextButton urlLink="/login" buttonText="Get Started"/>
    </div>
  );
}
