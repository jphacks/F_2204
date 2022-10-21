import type { NextPage } from "next";
import BaseLayout from "../../components/templates/BaseLayout";
import { Box, Input } from "@chakra-ui/react";
import { useRouter } from "next/router";
import BottomFloatingButton from "../../components/atoms/BottomFloatingButton";

const CommunityPage: NextPage = () => {
  const router = useRouter();
  return (
    <BaseLayout>
      <Box
        marginTop="20px"
        width="360px"
        borderWidth="1px"
        borderRadius="10px"
        padding="10px"
        display="flex"
        flexDirection="column"
        fontSize="sm"
      >
        <Box
          display="flex"
          justifyContent="space-between"
          alignItems="center"
        ></Box>
        <Box
          display="flex"
          justifyContent="space-between"
          alignItems="center"
          marginTop="10px"
        >
          <Box marginRight="20px">コミュニティ名</Box>
          <Box>
            <Input placeholder="例:いつメン" alignSelf="end" />
          </Box>
        </Box>

        <BottomFloatingButton
          text="参加する"
          bottom="65px"
          onClick={() => router.push("/article")}
        />
      </Box>
    </BaseLayout>
  );
};

export default CommunityPage;
