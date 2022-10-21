// endpoint: api/articles/
export type CreateArticleRequest = {
  uri?: string;
  article_name: string;
  article_content?: string;
};
