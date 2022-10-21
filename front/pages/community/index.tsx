import { Box } from "@chakra-ui/react";
import type { NextPage } from "next";
import BottomFloatingButton from "../../components/atoms/BottomFloatingButton";
import BaseLayout from "../../components/templates/BaseLayout";

const CommunityPage: NextPage = () => {
  return (
    <BaseLayout>
      <Box marginTop="10px">
        {Array(10)
          .fill("")
          .map((_, index) => (
            <Box
              key={index}
              marginTop={index ? "15px" : "0"}
              borderWidth="1px"
              borderRadius="10px"
              width="350px"
              height="80px"
              display="flex"
              alignItems="center"
              justifyContent="center"
              fontSize="xl"
            >
              {`コミュニティ名_${index + 1}`}
            </Box>
          ))}
      </Box>
      <BottomFloatingButton
        text="新しいコミュニティを作成する"
        bottom="60px"
        height="70px"
        boxShadow={" 0 5px 10px 0 rgba(0, 0, 0, .3)"}
        onClick={() => console.log("作成")}
      />
    </BaseLayout>
  );
};

export default CommunityPage;
