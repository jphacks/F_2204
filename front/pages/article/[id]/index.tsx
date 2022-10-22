import type { NextPage } from "next";
import { useRouter } from "next/router";
import ConfirmModal from "../../../components/molecules/ConfirmModal";
import BaseLayout from "../../../components/templates/BaseLayout";
import { Textarea,Box } from '@chakra-ui/react';


const DetailPage: NextPage = () => {
  const router = useRouter();
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

        <Box fontWeight="bold">2022/10/7 9:00 ～ 18:00</Box>
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
        height="290px"
        resize="none"
        overflow="scroll"
        value=""
        readOnly/>

      <ConfirmModal
        buttonText="参加する"
        title=""
        text="参加しますか？"
        onConfirm={() =>
          router.push(`/article/${Number(router.query.id)}/private`)
        }
      />
    </BaseLayout>
  );
};

export default DetailPage;
