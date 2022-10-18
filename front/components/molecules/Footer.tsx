import { Box } from "@chakra-ui/react";
import React, { FC } from "react";

type Props = {
  //   title: string;
  //   userName: string;
  //   communityName: string;
  //   date: string;
};

const Footer: FC<Props> = (props) => {
  return (
    <Box
      w="full"
      display="flex"
      justifyItems="end"
      height="50px"
      position="fixed"
      left="0"
      bottom="0"
      paddingX="20px"
      textAlign="center"
      alignItems="center"
    >
      <Box flex="1"></Box>
      <Box flex="1">ホーム</Box>
      <Box flex="1">コミュニティ</Box>
    </Box>
  );
};

export default Footer;
