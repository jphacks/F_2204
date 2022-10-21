import { Box } from "@chakra-ui/react";
import React, { FC } from "react";

type Props = {};

const Footer: FC<Props> = (props) => {
  return (
    <Box
      width="100%"
      display="flex"
      justifyContent="center"
      height="50px"
      position="fixed"
      left="0"
      top="0"
      textAlign="center"
      alignItems="center"
      backgroundColor="gray.200"
    >
      ヘッダータイトル
    </Box>
  );
};

export default Footer;
