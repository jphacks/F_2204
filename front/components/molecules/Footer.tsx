import { Box } from "@chakra-ui/react";
import React, { FC } from "react";

type Props = {};

const Footer: FC<Props> = (props) => {
  return (
    <Box
      w="full"
      display="flex"
      justifyContent="space-between"
      justifyItems="end"
      height="50px"
      position="fixed"
      left="0"
      bottom="0"
      paddingX="20px"
      textAlign="center"
      alignItems="center"
      backgroundColor="gray.200"
    >
      <Box w="full"></Box>
      <Box w="full">ホーム</Box>
      <Box w="full">コミュニティ</Box>
    </Box>
  );
};

export default Footer;
