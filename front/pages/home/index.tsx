import { Box } from "@chakra-ui/react";
import type { NextPage } from "next";
import { useRouter } from "next/router";
import EventCard from "../../components/molecules/EventCard";
import BaseLayout from "../../components/templates/BaseLayout";

const HomePage: NextPage = () => {
  const router = useRouter();
  return (
    <BaseLayout>
      {Array(10)
        .fill("")
        .map((_, index) => (
          <Box key={index} marginBottom="20px">
            <EventCard
              title="料理名"
              userName="ユーザー名"
              communityName="コミュニティ名"
              date="22/10/17"
              onClick={() => router.push(`/detail/${index + 1}`)}
            />
          </Box>
        ))}
    </BaseLayout>
  );
};

export default HomePage;
