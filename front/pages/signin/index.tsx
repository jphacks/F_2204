import { Box, Input } from "@chakra-ui/react";
import type { NextPage } from "next";
import router from "next/router";
import LargeButton from "../../components/atoms/LargeButton";
import BaseLayout from "../../components/templates/BaseLayout";

const SigninPage: NextPage = () => {
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
          <Box marginTop="20px">メールアドレス</Box>
          <Input placeholder="example@exmaple.com" />
          <Box marginTop="10px">パスワード</Box>
          <Input type="password" />
          <LargeButton
            margin="20px 0 0 0"
            text="ログインする"
            onClick={() => router.push("/article")}
          />
        </Box>
      </Box>
    </BaseLayout>
  );
};

export default SigninPage;
