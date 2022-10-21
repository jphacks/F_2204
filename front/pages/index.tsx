import type { NextPage } from "next";
import { useRouter } from "next/router";
import { useEffect } from "react";
import { useRecoilState } from "recoil";
import { userState } from "../atoms/userAtom";

const IndexPage: NextPage = () => {
  const router = useRouter();
  useEffect(() => {
    router.replace("/home");
  }, []);
  return <></>;
};

export default IndexPage;
