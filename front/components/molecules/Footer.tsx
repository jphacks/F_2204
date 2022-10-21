import { Box } from "@chakra-ui/react";
import { useRouter } from "next/router";
import React, { FC } from "react";

type Props = {};

const Footer: FC<Props> = (props) => {
  const router = useRouter();
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
      <Box w="full" onClick={() => router.push("/article")}>
        ホーム
      </Box>
      <Box w="full" onClick={() => router.push("/community")}>
        コミュニティ
      </Box>
    </Box>
  );
};

export default Footer;
