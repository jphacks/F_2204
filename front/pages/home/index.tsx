import { Box } from "@chakra-ui/react";
import type { NextPage } from "next";
import EventCard from "../../components/molecules/EventCard";
import BaseLayout from "../../components/templates/BaseLayout";

const HomePage: NextPage = () => {
  return (
    <BaseLayout>
      {Array(3)
        .fill("")
        .map((_, index) => (
          <Box key={index} marginBottom="20px">
            <EventCard
              title="料理名"
              userName="ユーザー名"
              communityName="コミュニティ名"
              date="22/10/17"
            />
          </Box>
        ))}
    </BaseLayout>
  );
};

export default HomePage;
