import { Box, Button } from "@chakra-ui/react";
import type { NextPage } from "next";
import { useRouter } from "next/router";
import LargeButton from "../../components/atoms/LargeButton";
import BaseLayout from "../../components/templates/BaseLayout";

const HomePage: NextPage = () => {
  const router = useRouter();
  return (
    <BaseLayout hideSidebar={true}>
      <Box w="full" height="80vh" display="flex" alignItems="center">
        <Box display="flex" flexDirection="column">
          <LargeButton
            text="新規登録"
            margin="0 0 20px 0"
            onClick={() => router.push("/signup")}
          />
          <LargeButton
            text="ログイン"
            margin="0 0 20px 0"
            onClick={() => router.push("/signin")}
          />
        </Box>
      </Box>
    </BaseLayout>
  );
};

export default HomePage;
