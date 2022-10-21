import { Box, Button } from "@chakra-ui/react";
import type { NextPage } from "next";
import { useRouter } from "next/router";
import EventCard from "../../components/molecules/EventCard";
import BaseLayout from "../../components/templates/BaseLayout";
import { AddIcon } from "@chakra-ui/icons";
import { useEffect, useState } from "react";
import { axiosInstance } from "../../api.config";
import { Article, CommunitysResponse } from "../../types/community";
import { userState } from "../../atoms/userAtom";
import { useRecoilValue } from "recoil";
import { get } from "../../lib/fetchWrapper";

const HomePage: NextPage = () => {
  const router = useRouter();
  const user = useRecoilValue(userState);
  const [communities, setCommunities] = useState<CommunitysResponse[]>([]);

  useEffect(() => {
    const fetch = async () => {
      let articles = [];
      const res = await get<CommunitysResponse[]>("/api/communities/");
      for (const community of res?.data || []) {
        const articleRes = await get("/api/articles/");
      }

      res?.data.forEach((community) => {
        community.community_id;
      });
      console.log("/api/communities/");
    };
    fetch();
  }, []);

  return (
    <BaseLayout>
      <Box marginTop="20px" marginBottom="40px">
        {/* {Array(3)
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
          ))} */}
        <Box
          marginTop="20px"
          _hover={{
            transform: "translateY(-2px)",
            boxShadow: "md",
          }}
        >
          <EventCard
            title="ゲームパーティ"
            userName="Aniki"
            communityName="暇人集い会"
            date="22/10/17"
            onClick={() => router.push(`/article/1`)}
          />
        </Box>
        <Box
          marginTop="10"
          _hover={{
            transform: "translateY(-2px)",
            boxShadow: "md",
          }}
        >
          <EventCard
            title="おでん料理作ってみた"
            userName="Aniki"
            communityName="暇人集い会"
            date="22/11/20"
            onClick={() => router.push(`/article/2`)}
          />
        </Box>
        <Box
          marginTop="10"
          _hover={{
            transform: "translateY(-2px)",
            boxShadow: "md",
          }}
        >
          <EventCard
            title="ゲームパーティ"
            userName="Aniki"
            communityName="暇人集い会"
            date="22/12/24"
            onClick={() => router.push(`/article/3`)}
          />
        </Box>
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
function useRecoilState(userState: any): [any] {
  throw new Error("Function not implemented.");
}
