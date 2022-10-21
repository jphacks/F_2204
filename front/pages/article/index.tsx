import { Box } from "@chakra-ui/react";
import type { NextPage } from "next";
import { useRouter } from "next/router";
import EventCard from "../../components/molecules/EventCard";
import BaseLayout from "../../components/templates/BaseLayout";

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
      </Box>
    </BaseLayout>
  );
};

export default HomePage;
