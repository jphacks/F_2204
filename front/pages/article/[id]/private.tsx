import { Input, Textarea, Button, Box } from "@chakra-ui/react";
import type { NextPage } from "next";
import BaseLayout from "../../../components/templates/BaseLayout";

const DetailPage: NextPage = () => {
  return (
    <BaseLayout>
      <Box
        height="100%"
        display="flex"
        flexDirection="column"
        alignContent="center"
      >
        <Box
          marginTop="20px"
          height="70px"
          w="350px"
          borderWidth="1px"
          borderRadius="10px"
          paddingX="10px"
          paddingY="10px"
          overflow="hidden"
          display="flex"
          flexDirection="column"
          justifyContent="space-between"
          alignContent="center"
        >
          <Box>
            <Box
              display="flex"
              justifyContent="space-between"
              fontSize="sm"
              fontWeight="bold"
            >
              <Box> 住所: </Box>
              <Box> 〒123-4567 福岡県福岡市東区1-2</Box>
            </Box>
            <Box
              display="flex"
              justifyContent="space-between"
              fontSize="sm"
              fontWeight="bold"
            >
              <Box> 完成予定時刻: </Box>
              <Box> 10/10 17:30 </Box>
            </Box>
          </Box>
        </Box>
        <Box
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
            <Box fontWeight="bold">@Shunpei</Box>
          </Box>
        </Box>
        <Textarea
          placeholder=""
          marginTop="20px"
          height="250px"
          resize="none"
          overflow="scroll"
          value="今回はなし"
          readOnly
        />
      </Box>
    </BaseLayout>
  );
};

export default DetailPage;
