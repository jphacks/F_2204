import { Box, Button } from "@chakra-ui/react";
import type { NextPage } from "next";
import { useRouter } from "next/router";
import EventCard from "../../components/molecules/EventCard";
import BaseLayout from "../../components/templates/BaseLayout";
import { AddIcon } from "@chakra-ui/icons";

const HomePage: NextPage = () => {
  const router = useRouter();
  return (
    <BaseLayout>
      <Box marginTop="20px" marginBottom="40px">
        {Array(10)
          .fill("")
          .map((_, index) => (
            <Box key={index} marginTop={index ? "20px" : "0"}>
              <EventCard
                title="料理名"
                userName="ユーザー名"
                communityName="コミュニティ名"
                date="22/10/17"
                onClick={() => router.push(`/article/${index + 1}`)}
              />
            </Box>
          ))}
        <Button
          w={"50px"}
          h={"50px"}
          borderRadius="25px"
          boxShadow={" 0 0 7px 0 rgba(0, 0, 0, .5)"}
          position="fixed"
          bottom="65px"
          right="20px"
          backgroundColor="gray.400"
          onClick={() => router.push("/article/post")}
        >
          <AddIcon />
        </Button>
      </Box>
    </BaseLayout>
  );
};

export default HomePage;
