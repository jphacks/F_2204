// endpoint: api/communities/<int:pk>/  (int:pkはcommunity_id)
export type CommunitysResponse = {
  community_id: number;
  community_name: string;
  users?: Array<User>;
};

export type User = {
  user_id: number;
  password: string;
  email: string;
  user_name: string;
  address: string;
  created_at: string;
};

// endpoint: api/communities/community_id/articles/
// example response
//{
//     "community_id": 1,
//     "articles": [],
//     "community_name": "test_community1",
//     "users": [
//         1
//     ]
// }
type UserID = number;
export type CommunityArticles = {
  community_id: number;
  articles?: Array<Article>;
  community_name: string;
  users?: Array<UserID>;
};

type CommunityID = number;
export type Article = {
  id: number;
  article: {
    article_id: number;
    uri: string;
    article_name: string;
    article_content: string;
    meeting_time: string;
    created_at: string;
    user: number;
    communities: Array<CommunityID>;
  };
  article_id: number;
  community_id: number;
};
