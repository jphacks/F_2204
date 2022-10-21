import { Box, Input } from "@chakra-ui/react";
import type { NextPage } from "next";
import router from "next/router";
import LargeButton from "../../components/atoms/LargeButton";
import BaseLayout from "../../components/templates/BaseLayout";

import { useRecoilState } from "recoil";
import { userState } from "../../atoms/userAtom";
import { axiosInstance } from "../../api.config";
import { useState } from "react";
import { SignInType } from "../../types/sign";

const SigninPage: NextPage = () => {
  const [, setUser] = useRecoilState(userState);
  const [isError, setIsError] = useState(false);
  const [inputState, setInputState] = useState({
    username: "",
    password: "",
  });

  const signin = async () => {
    try {
      const res = await axiosInstance.post<SignInType>("/api/token/", {
        username: inputState.username,
        password: inputState.password,
      });
      // tokenをatomにセット
      const data: SignInType = {
        access: res.data.access,
        refresh: res.data.refresh,
      };
      // TokenをLocalStorageとAtomに設定
      localStorage.setItem("token", JSON.stringify(data));
      console.log(JSON.stringify(localStorage.getItem("token")));
      setUser(data);
      setIsError(false);
      // /articleへ
      await router.push("/article");
    } catch (e) {
      setIsError(true);
    }
  };

  return (
    <BaseLayout hideSidebar>
      <Box
        w="full"
        height="80vh"
        display="flex"
        alignItems="center"
        alignSelf="center"
      >
        <Box
          display="flex"
          flexDirection="column"
          borderWidth="1px"
          borderRadius="10px"
          padding="15px"
        >
          <Box width="full" textAlign="center" fontSize="2xl" fontWeight="bold">
            ログイン
          </Box>
          <Box marginTop="20px">ユーザー名</Box>
          <Input
            value={inputState.username}
            onChange={(e) =>
              setInputState({ ...inputState, username: e.target.value })
            }
          />
          <Box marginTop="10px">パスワード</Box>
          <Input
            type="password"
            value={inputState.password}
            onChange={(e) =>
              setInputState({ ...inputState, password: e.target.value })
            }
          />
          {isError && (
            <Box marginTop="10px" color="red">
              ユーザ名またはパスワードが間違っています。
            </Box>
          )}
          <LargeButton
            margin="20px 0 0 0"
            text="ログインする"
            onClick={signin}
          />
        </Box>
      </Box>
    </BaseLayout>
  );
};

export default SigninPage;
