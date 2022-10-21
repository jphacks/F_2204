import { axiosInstance } from "../api.config";

export const get = async <T>(url: string) => {
  try {
    const res = await axiosInstance
      .get<T>(url, {
        headers: {
          Authorization: `Bearer ${
            JSON.parse(localStorage.getItem("token") || "{}").access
          }`,
        },
      })
      .catch((e) => console.log(e.response));
    return res;
  } catch (e) {
    return null;
  }
};

export const post = async <T>(url: string, data: any) => {
  try {
    const res = await axiosInstance.post<T>(url, {
      headers: {
        Authorization: `Bearer ${
          JSON.parse(localStorage.getItem("token") || "{}").access
        }`,
      },
      data,
    });
    return res;
  } catch (e) {
    return null;
  }
};
