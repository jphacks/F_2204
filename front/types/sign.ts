// ユーザログイン
export type SignInType = {
  access: string;
  refresh: string;
};

// ユーザ新規登録
export type SignUpType = {
  user_name: string;
  email: string;
  password: string;
  address: string;
};
