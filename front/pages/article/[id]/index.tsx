import { Input, Textarea, Button, Box } from "@chakra-ui/react";
import type { NextPage } from "next";
import BottomFloatingButton from "../../../components/atoms/BottomFloatingButton";
import BaseLayout from "../../../components/templates/BaseLayout";

const DetailPage: NextPage = () => {
  return (
    <BaseLayout>
      <Box
        width="350px"
        display="flex"
        justifyContent="space-between"
        marginTop="20px"
        fontSize="xl"
      >
        <Box fontWeight="bold" marginRight="20px">
          日時
        </Box>
        <Box fontWeight="bold">2022/10/1 9:00 ～ 18:00</Box>
      </Box>
      <Box
        display="flex"
        justifyContent="space-between"
        marginTop="20px"
        fontSize="xl"
      >
        <Box fontWeight="bold" marginRight="20px">
          参加予定者
        </Box>
        <Box>
          <Box fontWeight="bold">@ユーザー名1</Box>
          <Box fontWeight="bold">@ユーザー名2</Box>
          <Box fontWeight="bold">@ユーザー名3</Box>
        </Box>
      </Box>
      <Textarea
        placeholder=""
        marginTop="20px"
        height="290px"
        resize="none"
        overflow="scroll"
        value="必要なもの1, 必要なもの2, 必要なもの3..."
        readOnly
      />
      <BottomFloatingButton
        text="参加する"
        bottomPos="65px"
        onClick={() => console.log("参加")}
      />
    </BaseLayout>
  );
};

export default DetailPage;
