import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import styles from "../styles/Home.module.css";
import EventCard from "../components/molecules/EventCard";
import { css } from "@emotion/css";
import BaseLayout from "../components/templates/BaseLayout";

const Home: NextPage = () => {
  return (
    <BaseLayout>
      {Array(1)
        .fill("")
        .map((_, index) => (
          <div key={index}>
            <EventCard />
          </div>
        ))}
    </BaseLayout>
  );
};

export default Home;
