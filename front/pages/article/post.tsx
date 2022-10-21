import { Box, Button } from "@chakra-ui/react";
import { Input } from "@chakra-ui/react";
import { Textarea } from "@chakra-ui/react";
import type { NextPage } from "next";
import { useRouter } from "next/router";
import BottomFloatingButton from "../../components/atoms/BottomFloatingButton";
import BaseLayout from "../../components/templates/BaseLayout";

const PostPage: NextPage = () => {
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
        <Box display="flex" justifyContent="space-between" alignItems="center">
          <Box marginRight="20px">イベント名</Box>
          <Box>
            <Input placeholder="例:もつ煮会" alignSelf="end" />
          </Box>
        </Box>
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
        <Box
          display="flex"
          justifyContent="space-between"
          alignItems="center"
          marginTop="10px"
        >
          <Box marginRight="50px">日時</Box>
          <Box>
            <Input type="datetime-local" width="215px" />
          </Box>
        </Box>
        <Textarea
          placeholder="自由記述(買ってきてほしいものなど)"
          marginTop="10px"
          height="250px"
          resize="none"
          overflow="scroll"
        />
        <BottomFloatingButton
          text="作成する"
          bottom="65px"
          onClick={() => router.push("/article")}
        />
      </Box>
    </BaseLayout>
  );
};

export default PostPage;
