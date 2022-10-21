import { atom } from "recoil";
import { SignInType } from "../types/sign";

export const userState = atom<SignInType>({
  key: "userState",
  default: {
    access: "",
    refresh: "",
  },
});
