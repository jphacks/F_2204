import { Box, Button } from "@chakra-ui/react";
import { Input } from "@chakra-ui/react";
import { Textarea } from "@chakra-ui/react";
import { css } from "@emotion/css";
import type { NextPage } from "next";
import BaseLayout from "../../components/templates/BaseLayout";

const PostPage: NextPage = () => {
  return (
    <BaseLayout>
      <Box
        display="flex"
        justifyContent="space-between"
        alignItems="center"
        marginTop="20px"
      >
        <Box marginRight="20px">イベント名</Box>
        <Box>
          <Input placeholder="例:もつ煮会" />
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
      <Button width="100%" height="50px" marginTop="20px">
        作成する
      </Button>
    </BaseLayout>
  );
};

export default PostPage;
